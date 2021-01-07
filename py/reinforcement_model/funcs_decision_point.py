'''decision point functions'''

# pylint: disable=E0401, E1101, E1601, W0612
'''
import json
import sys

json_data = open(file='./settings.json', mode='r')
settings = json.load(json_data)
json_data.close()

sys.path.append(settings['deuces_path'])
sys.path.append(settings['holdem_calc_path'])

import deuces
from deuces import Evaluator as de
import holdem_calc
import parallel_holdem_calc
'''
import funcs_range as frange
import funcs_sql_ins as fsqli
import funcs_sql_sel as fsqls
import funcs_sql_upd as fsqlu
import numpy as np

def decision_point_based_action(poker_db, database, sql_path, phase, nr, step, position, stack, pot,
    flop1, flop2, flop3, turn, river, valid_actions, win_rate, small_blind_amount, seed):
    '''decision point calculations'''

    # np.random.seed(seed=seed) - using this call the same action is played in every round

    game_id = fsqls.sql_games_max_id(poker_db=poker_db, database=database, sql_path=sql_path)

    select_sql_file = open(sql_path + 'select_hand.sql')
    select_sql = select_sql_file.read()
    select_sql = eval(f'f"""{select_sql}"""')

    poker_cursor = poker_db.cursor()
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    hand_db_format = poker_result[0][0]
    
    select_sql_file.close()

    stack_range = frange.range_stack(stack=stack, small_blind_amount=small_blind_amount)
    pot_range = frange.range_pot(pot=pot, small_blind_amount=small_blind_amount)

    select_sql_file = open(sql_path + 'select_decision_points.sql')
    select_sql = select_sql_file.read()
    select_sql = eval(f'f"""{select_sql}"""')
    select_sql = select_sql.replace('s.*', 'REPLACE(REPLACE(REPLACE(' +\
        ' CONCAT(\'{\',' +\
        ' GROUP_CONCAT(s.jobj SEPARATOR \',\\' + 'n\'),' +\
        ' \'}\'), \'[\"\', \'[\'), \'\"]\', \']\'), \'\\\\\', \'\') as jobj')
    
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    select_sql_file.close()

    if poker_result[0][0] != -1:
        decision_point_id = poker_result[0][0]

        select_sql_file = open(sql_path + 'select_possible_moves.sql')
        select_sql = select_sql_file.read()
        select_sql = eval(f'f"""{select_sql}"""')

        poker_cursor.execute(select_sql)
        possible_actions_list = poker_cursor.fetchall()

        select_sql_file.close()
        
        POSSIBLE_ACTIONS_LIST = [[*elem] for elem in zip(*possible_actions_list)]
        ID = POSSIBLE_ACTIONS_LIST[0]
        ACTION = POSSIBLE_ACTIONS_LIST[1]
        BET_AMOUNT = POSSIBLE_ACTIONS_LIST[2]
        EV = POSSIBLE_ACTIONS_LIST[3]
        if min(EV) <= 0:
            NEWEV = [elem + abs(min(EV)) + 1 for elem in EV]
        else:
            NEWEV = EV

        EVPROB = [elem / sum(NEWEV) for elem in NEWEV]
        
        final_action_id = np.random.choice(ID, p=EVPROB)      
        final_action = ACTION[final_action_id]
        if final_action != 'call':
            final_action_amount = BET_AMOUNT[final_action_id]
        else:
            for action in valid_actions:
                if action['action'] == 'call':
                    final_action_amount = action['amount']

        return final_action, int(final_action_amount)
    else:
        select_sql_file = open(sql_path + 'select_decision_points_history.sql')
        select_sql = select_sql_file.read()
        select_sql = eval(f'f"""{select_sql}"""')
        select_sql = select_sql.replace('s.*', 'REPLACE(REPLACE(REPLACE(' +\
            ' CONCAT(\'{\',' +\
            ' GROUP_CONCAT(s.jobj SEPARATOR \',\\' + 'n\'),' +\
            ' \'}\'), \'[\"\', \'[\'), \'\"]\', \']\'), \'\\\\\', \'\') as jobj')
        
        poker_cursor.execute(select_sql)
        history = poker_cursor.fetchall()

        select_sql_file.close()
        
        fsqli.sql_insert_decision_points(poker_db=poker_db, database=database, sql_path=sql_path,
            phase=phase, nr=nr, position=position, hand_db_format=hand_db_format,
            win_rate=win_rate, stack_range=stack_range, pot_range=pot_range, history=history[0][0])

        validity_for_fold = 1
        for action in valid_actions:
            if action['action'] == 'call' and action['amount'] == 0:
                validity_for_fold = 0

        for action in valid_actions:
            if action['action'] == 'fold' and validity_for_fold == 1:
                fsqli.sql_insert_possible_moves(poker_db=poker_db, database=database,
                    sql_path=sql_path, action=action['action'], bet_amount_range=action['amount'])
            elif action['action'] == 'call':
                fsqli.sql_insert_possible_moves(poker_db=poker_db, database=database,
                    sql_path=sql_path, action=action['action'], bet_amount_range=-1)
            elif action['action'] == 'raise':
                if action['amount']['min'] != -1 and action['amount']['max'] != -1:
                    for i in range(1, int(action['amount']['max'] / action['amount']['min']) + 1):
                        fsqli.sql_insert_possible_moves(poker_db=poker_db, database=database,
                            sql_path=sql_path, action=action['action'],
                            bet_amount_range=action['amount']['min'] * i)
                
                    if action['amount']['max'] % action['amount']['min'] != 0:
                        fsqli.sql_insert_possible_moves(poker_db=poker_db, database=database,
                            sql_path=sql_path, action=action['action'],
                            bet_amount_range=action['amount']['max'])
            else:
                pass

        return decision_point_based_action(poker_db=poker_db, database=database, sql_path=sql_path,
            phase=phase, nr=nr, step=step, position=position, pot=pot, stack=stack,
            flop1=flop1, flop2=flop2, flop3=flop3, turn=turn, river=river,
            valid_actions=valid_actions, win_rate=win_rate, small_blind_amount=small_blind_amount,
            seed=seed)

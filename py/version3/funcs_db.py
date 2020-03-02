'''database functions'''

# pylint: disable=E0401, E1101, E1601, W0612

import json
import numpy as np
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

sql_path = settings['sql_path']

def sql_delete_allrows(poker_db, database, table):
    '''delete all rows from table'''

    delete_sql_file = open(sql_path + 'delete_allrows.sql')
    delete_sql = delete_sql_file.read()
    delete_sql = eval(f'f"""{delete_sql}"""')

    # poker_db = mysql.connector.connect(user=settings['sql_user'],\
    #                                    host=settings['sql_host'],\
    #                                    database=settings['sql_database'])
    poker_cursor = poker_db.cursor()
    poker_cursor.execute(delete_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    delete_sql_file.close()

    return None

def sql_select_tables(poker_db, database):
    '''query name of all tables from database'''

    select_sql_file = open(sql_path + 'select_tables.sql')
    select_sql = select_sql_file.read()
    select_sql = eval(f'f"""{select_sql}"""')

    # poker_db = mysql.connector.connect(user=settings['sql_user'],\
    #                                    host=settings['sql_host'],\
    #                                    database=settings['sql_database'])
    poker_cursor = poker_db.cursor()
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()
    tables = [[*table] for table in zip(*poker_result)]
    # poker_db.close()

    select_sql_file.close()

    return tables[0]

def sql_games_max_id(poker_db, database):
    '''query max id from games table'''

    select_sql_file = open(sql_path + 'select_games_max_id.sql')
    select_sql = select_sql_file.read()
    select_sql = eval(f'f"""{select_sql}"""')

    # poker_db = mysql.connector.connect(user=settings['sql_user'],\
    #                                    host=settings['sql_host'],\
    #                                    database=settings['sql_database'])
    poker_cursor = poker_db.cursor()
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()
    # poker_db.close()

    select_sql_file.close()

    return poker_result[0][0]

def sql_decision_points_max_id(poker_db, database):
    '''query max id from decision_points table'''

    select_sql_file = open(sql_path + 'select_decision_points_max_id.sql')
    select_sql = select_sql_file.read()
    select_sql = eval(f'f"""{select_sql}"""')

    # poker_db = mysql.connector.connect(user=settings['sql_user'],\
    #                                    host=settings['sql_host'],\
    #                                    database=settings['sql_database'])
    poker_cursor = poker_db.cursor()
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()
    # poker_db.close()

    select_sql_file.close()

    return poker_result[0][0]

def sql_possible_moves_max_id(poker_db, database, decision_point_id):
    '''query max id from possible_moves table'''

    select_sql_file = open(sql_path + 'select_possible_moves_max_id.sql')
    select_sql = select_sql_file.read()
    select_sql = eval(f'f"""{select_sql}"""')

    # poker_db = mysql.connector.connect(user=settings['sql_user'],\
    #                                    host=settings['sql_host'],\
    #                                    database=settings['sql_database'])
    poker_cursor = poker_db.cursor()
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()
    # poker_db.close()

    select_sql_file.close()

    return poker_result[0][0]

def sql_stack_result(poker_db, database, position):
    '''calculate result of game for given position'''

    index = sql_games_max_id(poker_db=poker_db, database=database)

    select_sql_file = open(sql_path + 'select_stack_result.sql')
    select_sql = select_sql_file.read()
    select_sql = eval(f'f"""{select_sql}"""')

    # poker_db = mysql.connector.connect(user=settings['sql_user'],\
    #                                    host=settings['sql_host'],\
    #                                    database=settings['sql_database'])
    poker_cursor = poker_db.cursor()
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()
    # poker_db.close()

    select_sql_file.close()
    
    return poker_result[0][0]

def sql_possible_moves_features(poker_db, database, decision_point_id, action):
    '''select current values of possible_moves.counter and possible_moves.total_profit'''

    select_sql_file = open(sql_path + 'select_possible_moves_features.sql')
    select_sql = select_sql_file.read()
    select_sql = eval(f'f"""{select_sql}"""')

    # poker_db = mysql.connector.connect(user=settings['sql_user'],\
    #                                    host=settings['sql_host'],\
    #                                    database=settings['sql_database'])
    poker_cursor = poker_db.cursor()
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()
    # poker_db.close()

    select_sql_file.close()

    return poker_result[0][0], poker_result[0][1]

def sql_insert_games(poker_db, database, index, player_num, small_blind_amount, ante_amount,\
    uuid, name, stack, position, card1, card2, hand_db_format, flop1, flop2,flop3, turn,\
    river, final_stack):
    '''insert rows into games table'''

    if position == 1:
        position_name = 'SB'
    elif position == 2:
        position_name = 'BB'
    elif position == 3:
        position_name = 'UTG'
    elif position == 4:
        position_name = 'MIDDLE'
    elif position == 5:
        position_name = 'TAIL'
    else:
        position_name = 'DEALER'

    insert_sql_file = open(sql_path + 'insert_games.sql')
    insert_sql = insert_sql_file.read()
    insert_sql = eval(f'f"""{insert_sql}"""')
    
    # poker_db = mysql.connector.connect(user=settings['sql_user'],\
    #                                    host=settings['sql_host'],\
    #                                    database=settings['sql_database'])
    poker_cursor = poker_db.cursor()
    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    insert_sql_file.close()

    return None

def sql_insert_history(poker_db, database, phase, nr, step, uuid, position, stack, stack_range,\
    pot, pot_range, flop1, flop2, flop3, turn, river, action, amount, amount_potrate,\
    new_stack, new_stack_range, new_pot, new_pot_range):
    '''insert rows into games table'''

    game_id = sql_games_max_id(poker_db=poker_db, database=database)

    insert_sql_file = open(sql_path + 'insert_history.sql')
    insert_sql = insert_sql_file.read()
    insert_sql = eval(f'f"""{insert_sql}"""')

    # poker_db = mysql.connector.connect(user=settings['sql_user'],\
    #                                    host=settings['sql_host'],\
    #                                    database=settings['sql_database'])
    poker_cursor = poker_db.cursor()
    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')

    sql_update_games_board(poker_db=poker_db, database=database, index=game_id,\
        flop1=flop1, flop2=flop2, flop3=flop3, turn=turn, river=river)
    # poker_db.close()

    insert_sql_file.close()

    return None

def sql_insert_decision_points(poker_db, database, phase, nr, position, hand_db_format,\
    hand_strength, improv_rate, stack_range, pot_range, history):
    '''insert rows into decision_points table'''

    index = sql_decision_points_max_id(poker_db=poker_db, database=database) + 1

    insert_sql_file = open(sql_path + 'insert_decision_points.sql')
    insert_sql = insert_sql_file.read()
    insert_sql = eval(f'f"""{insert_sql}"""')

    # poker_db = mysql.connector.connect(user=settings['sql_user'],\
    #                                    host=settings['sql_host'],\
    #                                    database=settings['sql_database'])
    poker_cursor = poker_db.cursor()
    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    insert_sql_file.close()

    return None

def sql_insert_possible_moves(poker_db, database, action, bet_amount, counter=1, total_profit=1,\
    expected_value=1):
    '''insert rows into possible_moves table'''

    decision_point_id = sql_decision_points_max_id(poker_db=poker_db, database=database)
    index = sql_possible_moves_max_id(poker_db=poker_db, database=database,\
        decision_point_id=decision_point_id) + 1

    insert_sql_file = open(sql_path + 'insert_possible_moves.sql')
    insert_sql = insert_sql_file.read()
    insert_sql = eval(f'f"""{insert_sql}"""')
    
    # poker_db = mysql.connector.connect(user=settings['sql_user'],\
    #                                    host=settings['sql_host'],\
    #                                    database=settings['sql_database'])
    poker_cursor = poker_db.cursor()
    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    insert_sql_file.close()

    return None

def decision_point_based_action(poker_db, database, phase, nr, step, position, stack, pot, \
    flop1, flop2, flop3, turn, river, valid_actions):
    '''decision point calculations'''

    game_id = sql_games_max_id(poker_db=poker_db, database=database)

    select_sql_file = open(sql_path + 'select_hand.sql')
    select_sql = select_sql_file.read()
    select_sql = eval(f'f"""{select_sql}"""')

    # poker_db = mysql.connector.connect(user=settings['sql_user'],\
    #                                    host=settings['sql_host'],\
    #                                    database=settings['sql_database'])
    poker_cursor = poker_db.cursor()
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    hand_db_format = poker_result[0][0]
    
    if phase == 'preflop':
        hand_strength = 0
        improv_rate = dict()
    else:
        board_hs = []
        board_ir = []
        if flop1 != '':
            flop1_new = flop1[1:] + flop1[:1].lower()
            board_hs.append(deuces.Card.new(flop1_new))
            board_ir.append(flop1_new)
        if flop2 != '':
            flop2_new = flop2[1:] + flop2[:1].lower()
            board_hs.append(deuces.Card.new(flop2_new))
            board_ir.append(flop2_new)
        if flop3 != '':
            flop3_new = flop3[1:] + flop3[:1].lower()
            board_hs.append(deuces.Card.new(flop3_new))
            board_ir.append(flop3_new)
        if turn != '':
            turn_new = turn[1:] + turn[:1].lower()
            board_hs.append(deuces.Card.new(turn_new))
            board_ir.append(turn_new)
        if river != '':
            river_new = river[1:] + river[:1].lower()
            board_hs.append(deuces.Card.new(river_new))
            board_ir.append(river_new)
        
        crd1 = poker_result[0][1].replace(poker_result[0][1][-1:], poker_result[0][1][-1:].lower())
        crd2 = poker_result[0][2].replace(poker_result[0][2][-1:], poker_result[0][2][-1:].lower())
        hand_hs = [deuces.Card.new(crd1), deuces.Card.new(crd2)]
        hand_ir = [crd1, crd2]
        
        hand_strength = de().evaluate(board_hs, hand_hs)
        improv_rate = holdem_calc.calculate(board_ir, False, 1, None, hand_ir, True)[1]
        for key in improv_rate.keys():
            improv_rate[key] = round(improv_rate[key], 4)

    select_sql_file.close()

    stack_range = range_stack(stack=stack, small_blind_amount=settings['small_blind_amount'])
    pot_range = range_pot(pot=pot, small_blind_amount=settings['small_blind_amount'])

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
            EV = [elem + abs(min(EV)) + 1 for elem in EV]

        EV = [elem / sum(EV) for elem in EV]
        final_action_id = np.random.choice(ID, p=EV)
        final_action = ACTION[final_action_id]
        final_action_amount = BET_AMOUNT[final_action_id]

        decision = {
            'position': position,
            'decision_point_id': decision_point_id,
            'action': final_action
        }

        return final_action, final_action_amount, decision
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
        
        sql_insert_decision_points(poker_db=poker_db, database=database, phase=phase, nr=nr,\
            position=position, hand_db_format=hand_db_format, hand_strength=hand_strength,\
            improv_rate=improv_rate, stack_range=stack_range, pot_range=pot_range,\
            history=history[0][0])
        
        for action in valid_actions:
            if action['action'] != 'raise':
                sql_insert_possible_moves(poker_db=poker_db, database=database,\
                    action=action['action'], bet_amount=action['amount'])
            else:
                # amount = np.random.randint(action['amount']['min'], action['amount']['max'] + 1)
                sql_insert_possible_moves(poker_db=poker_db, database=database,\
                    action=action['action'], bet_amount=action['amount']['min'])

    # poker_db.close()

        return decision_point_based_action(poker_db=poker_db, database=database, phase=phase,\
            nr=nr, step=step, position=position, pot=pot, stack=stack,\
            flop1=flop1, flop2=flop2, flop3=flop3, turn=turn, river=river,\
            valid_actions=valid_actions)

def sql_update_games_cards(poker_db, database, index, uuid, card1, card2, hand_db_format):
    '''update card info in games table'''

    update_sql_file = open(sql_path + 'update_games_cards.sql')
    update_sql = update_sql_file.read()
    update_sql = eval(f'f"""{update_sql}"""')

    # poker_db = mysql.connector.connect(user=settings['sql_user'],\
    #                                    host=settings['sql_host'],\
    #                                    database=settings['sql_database'])
    poker_cursor = poker_db.cursor()
    poker_cursor.execute(update_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    update_sql_file.close()

    return None

def sql_update_games_board(poker_db, database, index, flop1, flop2, flop3, turn, river):
    '''update card info in games table'''

    update_sql_file = open(sql_path + 'update_games_board.sql')
    update_sql = update_sql_file.read()
    update_sql = eval(f'f"""{update_sql}"""')

    # poker_db = mysql.connector.connect(user=settings['sql_user'],\
    #                                    host=settings['sql_host'],\
    #                                    database=settings['sql_database'])
    poker_cursor = poker_db.cursor()
    poker_cursor.execute(update_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    update_sql_file.close()

    return None

def sql_update_games_final_stack(poker_db, database, index, uuid, final_stack):
    '''update final stack info in games table at end of game'''

    update_sql_file = open(sql_path + 'update_games_final_stack.sql')
    update_sql = update_sql_file.read()
    update_sql = eval(f'f"""{update_sql}"""')

    # poker_db = mysql.connector.connect(user=settings['sql_user'],\
    #                                    host=settings['sql_host'],\
    #                                    database=settings['sql_database'])
    poker_cursor = poker_db.cursor()
    poker_cursor.execute(update_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    update_sql_file.close()

    return None

def sql_update_possible_moves(poker_db, database, position, decision_point_id, action):
    '''update columns in possible_moves table'''

    result = sql_stack_result(poker_db=poker_db, database=database, position=position)
    counter, total_profit = sql_possible_moves_features(poker_db=poker_db, database=database,\
        decision_point_id=decision_point_id, action=action)

    if counter == 1 and total_profit == 1:
        total_profit = result
    else:
        counter = counter + 1
        total_profit = total_profit + result
    
    expected_value = total_profit / counter

    update_sql_file = open(sql_path + 'update_possible_moves.sql')
    update_sql = update_sql_file.read()
    update_sql = eval(f'f"""{update_sql}"""')

    # poker_db = mysql.connector.connect(user=settings['sql_user'],\
    #                                    host=settings['sql_host'],\
    #                                    database=settings['sql_database'])
    poker_cursor = poker_db.cursor()
    poker_cursor.execute(update_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    update_sql_file.close()

    return None

def community_cards_eval(board):
    '''function to evaluate community cards'''

    if board == []:
        final_board = ['', '', '', '', '']
    elif board != [] and len(board) == 3:
        board.sort()
        for i in range(2):
            board.append('')
        final_board = board
    elif board != [] and len(board) == 4:
        final_board = board[:3]
        final_board.sort()
        final_board.append(board[3])
        final_board.append('')
    elif board != [] and len(board) == 5:
        final_board = board[:3]
        final_board.sort()
        for i in range(3, 5):
            final_board.append(board[i])
    else:
        pass

    return final_board

def valid_actions_check(actions, phase, position, stack, small_blind_amount):
    '''function to check and return truly valid actions'''

    fold_actions = fold_check(actions=actions, phase=phase, position=position,\
        small_blind_amount=small_blind_amount)
    call_actions = call_check(actions=fold_actions, stack=stack)
    final_actions = raise_check(actions=call_actions, stack=stack)

    return final_actions

def fold_check(actions, phase, position, small_blind_amount):
    '''check fold action'''

    remove_fold_flag = 0
    for action in actions:
        if action['action'] == 'call' and (action['amount'] == 0\
        or (action['amount'] == small_blind_amount * 2 and phase == 'preflop'\
        and position == 2)):
            remove_fold_flag = 1
    
    fold_actions = []
    for action in actions:
        if action['action'] == 'fold' and remove_fold_flag == 1:
            pass
        else:
            fold_actions.append(action)

    return fold_actions

def call_check(actions, stack):
    '''check fold action'''

    for action in actions:
        if action['action'] == 'call' and action['amount'] > stack:
            action['amount'] = stack

    call_actions = actions

    return call_actions

def raise_check(actions, stack):
    '''check fold action'''

    for action in actions:
        if action['action'] == 'raise' and action['amount']['min'] == -1\
        and action['amount']['max'] == -1:
            action['amount']['min'] = stack
            action['amount']['max'] = stack
    
    raise_actions = actions

    return raise_actions

def summarize(poker_db, database, final_stacks, summary):
    '''summarize the result of round'''

    index = sql_games_max_id(poker_db=poker_db, database=database)

    for final_stack in final_stacks:
        sql_update_games_final_stack(poker_db=poker_db, database=database, index=index,\
            uuid=final_stack['uuid'], final_stack=final_stack['stack'])
    
    for decision in summary:
        sql_update_possible_moves(poker_db=poker_db, database=database,\
            position=decision['position'], decision_point_id=decision['decision_point_id'],\
            action=decision['action'])

    return None

def range_stack(stack, small_blind_amount):
    '''create ranges from stack'''

    stack = stack / small_blind_amount
    if stack < 200:
        rng = str(int(stack / 10) * 10) + '-' + str((int(stack / 10) + 1) * 10)
    elif stack >= 200 and stack < 1000:
        rng = str(int(stack / 50) * 50) + '-' + str((int(stack / 50) + 1) * 50)
    elif stack >= 1000 and stack < 2000:
        rng = str(int(stack / 100) * 100) + '-' + str((int(stack / 100) + 1) * 100)
    else:
        rng = '2000+'
    
    return rng

def range_pot(pot, small_blind_amount):
    '''create ranges from spot'''

    pot = pot /small_blind_amount
    if pot < 50:
        rng = str(int(pot / 5) * 5) + '-' + str((int(pot / 5) + 1) * 5)
    elif pot >= 50 and pot < 100:
        rng = str(int(pot / 10) * 10) + '-' + str((int(pot / 10) + 1) * 10)
    elif pot >= 100 and pot < 200:
        rng = str(int(pot / 20) * 20) + '-' + str((int(pot / 20) + 1) * 20)
    elif pot >= 200 and pot < 1000:
        rng = str(int(pot / 50) * 50) + '-' + str((int(pot / 50) + 1) * 50)
    else:
        rng = '1000+'
    
    return rng

def range_potrate(amount, pot, action):
    '''create ranges from action amount'''

    if pot != 0:
        rate = amount / pot

    if action == 'CALL' or (action != 'CALL' and pot == 0):
        rng = '1'
    elif action != 'CALL' and pot != 0 and rate < 2:
        rng = str(round(int(rate / 0.2) * 0.2, 1)) + '-' +\
            str(round((int(rate / 0.2) + 1) * 0.2, 1))
    elif action != 'CALL' and pot != 0 and rate >= 2 and rate < 3:
        rng = str(round(int(rate / 0.5) * 0.5, 1)) + '-' +\
            str(round((int(rate / 0.5) + 1) * 0.5, 1))
    else:
        rng = '3+'
    
    return rng

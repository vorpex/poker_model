'''database functions'''

# pylint: disable=E1101, E1601, W0612

import numpy as np

import funcs_poker

import pplayer
import ppot

sql_path = 'c:\\Users\\adam.sohonyai\\Documents\\GitHub\\poker_model\\sql\\'

def sql_delete_all(poker_db, table):
    '''delete all rows from table'''

    TABLE = table

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker')
    poker_cursor = poker_db.cursor()
    delete_sql_file = open(sql_path + 'delete_all.sql').read()
    delete_sql = eval(f'f"""{delete_sql_file}"""')
    poker_cursor.execute(delete_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    return None

def sql_insert_games(poker_db, number_of_players, player0_stack, player1_stack, player2_stack, player3_stack, \
    player4_stack, player5_stack, small_blind, big_blind):
    '''insert row into games table'''

    NUMBER_OF_PLAYERS = number_of_players
    PLAYER0_STACK = player0_stack
    PLAYER1_STACK = player1_stack
    PLAYER2_STACK = player2_stack
    PLAYER3_STACK = player3_stack
    PLAYER4_STACK = player4_stack
    PLAYER5_STACK = player5_stack
    SMALL_BLIND = small_blind
    BIG_BLIND = big_blind

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker')
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'games_max_id.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()
    
    ID = poker_result[0][0] + 1
    insert_sql_file = open(sql_path + 'insert_games.sql').read()
    insert_sql = eval(f'f"""{insert_sql_file}"""')
    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    return None

def sql_insert_history(poker_db, phase, nr, player_name, position, stack, pot, flop1, flop2, flop3, turn, \
    river, move, amount, new_stack, new_pot):
    '''insert row into history table'''

    PHASE = phase
    NR = nr
    PLAYER_NAME = player_name
    POSITION = position
    STACK = stack
    POT = pot
    FLOP1 = flop1
    FLOP2 = flop2
    FLOP3 = flop3
    TURN = turn
    RIVER = river
    MOVE = move
    AMOUNT = amount
    NEW_STACK = new_stack
    NEW_POT = new_pot

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker')
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'games_max_id.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    GAME_ID = poker_result[0][0]
    insert_sql_file = open(sql_path + 'insert_history.sql').read()
    insert_sql = eval(f'f"""{insert_sql_file}"""')
    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    return None

def sql_insert_decision_points(poker_db, hand, stack, pot, position, phase, nr, history):
    '''insert row into decision points table'''

    HAND = hand
    STACK = stack
    POT = pot
    POSITION = position
    PHASE = phase
    NR = nr
    HISTORY = history

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker')
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'decision_points_max_id.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    ID = poker_result[0][0] + 1
    insert_sql_file = open(sql_path + 'insert_decision_points.sql').read()
    insert_sql = eval(f'f"""{insert_sql_file}"""')
    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    return None

def sql_insert_possible_moves(poker_db, move, amount, total_profit=1, played_counter=1, \
    expected_value=1):
    '''insert row into possible moves table'''

    MOVE = move
    AMOUNT = amount
    TOTAL_PROFIT = total_profit
    PLAYED_COUNTER = played_counter
    EXPECTED_VALUE = expected_value

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker')
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'decision_points_max_id.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    DECISION_POINT_ID = poker_result[0][0]
    select_sql_file = open(sql_path + 'possible_moves_max_id.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    ID = poker_result[0][0] + 1
    insert_sql_file = open(sql_path + 'insert_possible_moves.sql').read()
    insert_sql = eval(f'f"""{insert_sql_file}"""')
    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    return None

def decision_point(poker_db, player_name, hand, stack, pot, position=2, phase=0, nr=2):
    '''decision point calculations'''

    PLAYER_NAME = player_name
    HAND = hand
    STACK = stack
    POT = pot
    POSITION = position
    PHASE = phase
    NR = nr

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker')
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'games_max_id.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    max_id = poker_cursor.fetchall()

    GAME_ID = max_id[0][0]
    select_sql_file = open(sql_path + 'select_decision_points.sql').read()    
    select_sql = eval(f'f"""{select_sql_file}"""')
    select_sql = select_sql.replace('*', 'REPLACE(REPLACE(REPLACE(' +\
        ' CONCAT(\'{\',' +\
        ' GROUP_CONCAT(s.jobj SEPARATOR \',\\' + 'n\'),' +\
        ' \'}\'), \'[\"\', \'[\'), \'\"]\', \']\'), \'\\\\\', \'\') as jobj')
    poker_cursor.execute(select_sql)
    decision_point_id = poker_cursor.fetchall()

    if decision_point_id[0][0] != -1:
        DECISION_POINT_ID = decision_point_id[0][0]
        select_sql_file = open(sql_path + 'select_possible_moves.sql').read()
        select_sql = eval(f'f"""{select_sql_file}"""')
        poker_cursor.execute(select_sql)
        possible_moves_list = poker_cursor.fetchall()
        possible_moves_list = [[*elem] for elem in zip(*possible_moves_list)]

        ID = possible_moves_list[0]
        MOVES = possible_moves_list[1]
        AMOUNT = possible_moves_list[2]
        EV = possible_moves_list[3]
        if min(EV) <= 0:
            EV = [elem + abs(min(EV)) + 1 for elem in EV]
        else:
            pass
        EV = [elem / sum(EV) for elem in EV]
        final_move_id = np.random.choice(ID, p=EV)
        final_move = MOVES[final_move_id]
        final_move_amount = AMOUNT[final_move_id]

        # poker_db.close()

        return final_move, final_move_amount
    else:
        select_sql_file = open(sql_path + 'select_decision_points_history.sql').read()
        select_sql = eval(f'f"""{select_sql_file}"""')
        select_sql = select_sql.replace('*', 'REPLACE(REPLACE(REPLACE(' +\
            ' CONCAT(\'{\',' +\
            ' GROUP_CONCAT(s.jobj SEPARATOR \',\\' + 'n\'),' +\
            ' \'}\'), \'[\"\', \'[\'), \'\"]\', \']\'), \'\\\\\', \'\') as jobj')
        poker_cursor.execute(select_sql)
        history = poker_cursor.fetchall()
        
        sql_insert_decision_points(poker_db=poker_db, hand=hand, stack=stack, pot=pot, position=position, \
            phase=phase, nr=nr, history=history[0][0])

        select_sql_file = open(sql_path + 'select_history_move.sql').read()
        select_sql = eval(f'f"""{select_sql_file}"""')
        poker_cursor.execute(select_sql)
        last_move = poker_cursor.fetchall()

        select_sql_file = open(sql_path + 'select_history_amount.sql').read()
        select_sql = eval(f'f"""{select_sql_file}"""')
        poker_cursor.execute(select_sql)
        sum_amount = poker_cursor.fetchall()
        
        for key, value in funcs_poker.check_moves(last_move=last_move[0][0], sum_amount=sum_amount[0][0], \
            stack=stack, position=position).items():
            sql_insert_possible_moves(poker_db=poker_db, move=key, amount=value)

        # poker_db.close()

        return decision_point(poker_db, player_name, hand, stack, pot, position, phase, nr)

def details_to_move(poker_db, phase, position):
    '''gather details to check move possibility'''

    POSITION = position
    PHASE = phase

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker')
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'games_max_id.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    GAME_ID = poker_result[0][0]
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'select_details_to_move.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall() 

    return poker_result[0][0], poker_result[1][0]

'''database functions'''

# pylint: disable=E1101, E1601, W0612

import numpy as np

sql_path = 'c:\\Users\\adam.sohonyai\\Documents\\GitHub\\poker_model\\sql\\version2\\'

def sql_delete_all(poker_db, table):
    '''delete all rows from table'''

    TABLE = table

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    delete_sql_file = open(sql_path + 'delete_all.sql').read()
    delete_sql = eval(f'f"""{delete_sql_file}"""')
    poker_cursor.execute(delete_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    return None

def sql_insert_games(poker_db, index, player_num, small_blind_amount, ante_amount, player, stack, position, \
                    position_name, card1, card2, hand_db_format):
    '''insert rows into poker_version2.games table'''

    ID = index
    PLAYER_NUM = player_num
    SMALL_BLIND_AMOUNT = small_blind_amount
    ANTE_AMOUNT = ante_amount
    PLAYER = player
    STACK = stack
    POSITION = position
    POSITION_NAME = position_name
    CARD1 = card1
    CARD2 = card2
    HAND_DB_FORMAT = hand_db_format

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    insert_sql_file = open(sql_path + 'insert_games.sql').read()
    insert_sql = eval(f'f"""{insert_sql_file}"""')
    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    return None

def sql_update_games_cards(poker_db, player, card1, card2, hand_db_format):
    '''update card info in poker_version2.games table'''

    PLAYER = player
    CARD1 = card1
    CARD2 = card2
    HAND_DB_FORMAT = hand_db_format

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'select_games_max_id.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    ID = poker_result[0][0]

    update_sql_file = open(sql_path + 'update_games_cards.sql').read()
    update_sql = eval(f'f"""{update_sql_file}"""')
    poker_cursor.execute(update_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    return None

def sql_insert_history(poker_db, phase, nr, player, position, stack, pot, flop1, flop2, flop3, turn, river, \
                        move, amount, new_stack, new_pot):
    '''insert rows into poker_version2.games table'''

    PHASE = phase
    NR = nr
    PLAYER = player
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


    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'select_games_max_id.sql').read()
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

def sql_insert_decision_points(poker_db, hand_db_format, stack, pot, position, phase, nr, history):
    '''insert rows into poker_version2.decision_points table'''

    HAND_DB_FORMAT = hand_db_format
    STACK = stack
    POT = pot
    POSITION = position
    PHASE = phase
    NR = nr
    HISTORY = history

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'select_decision_points_max_id.sql').read()
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

def sql_insert_possible_moves(poker_db, move, amount, total_profit=1, played_counter=1, expected_value=1):
    '''insert rows into poker_version2.possible_moves table'''

    MOVE = move
    AMOUNT = amount
    TOTAL_PROFIT = total_profit
    PLAYED_COUNTER = played_counter
    EXPECTED_VALUE = expected_value

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'select_decision_points_max_id.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    DECISION_POINT_ID = poker_result[0][0]
    
    select_sql_file = open(sql_path + 'select_possible_moves_max_id.sql').read()
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

def decision_point_based_move(poker_db, phase, nr, pot, position, stack, possible_moves):
    '''decision point calculations'''

    PHASE = phase
    NR = nr
    POT = pot
    POSITION = position
    STACK = stack

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'select_games_max_id.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    GAME_ID = poker_result[0][0]

    select_sql_file = open(sql_path + 'select_hand.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    HAND_DB_FORMAT = poker_result[0][0]

    select_sql_file = open(sql_path + 'select_decision_points.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    select_sql = select_sql.replace('*', 'REPLACE(REPLACE(REPLACE(' +\
        ' CONCAT(\'{\',' +\
        ' GROUP_CONCAT(s.jobj SEPARATOR \',\\' + 'n\'),' +\
        ' \'}\'), \'[\"\', \'[\'), \'\"]\', \']\'), \'\\\\\', \'\') as jobj')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    if poker_result[0][0] != -1:
        DECISION_POINT_ID = poker_result[0][0]

        select_sql_file = open(sql_path + 'select_possible_moves.sql').read()
        select_sql = eval(f'f"""{select_sql_file}"""')
        poker_cursor.execute(select_sql)
        possible_moves_list = poker_cursor.fetchall()
        
        POSSIBLE_MOVE_LIST = [[*elem] for elem in zip(*possible_moves_list)]

        ID = POSSIBLE_MOVE_LIST[0]
        MOVES = POSSIBLE_MOVE_LIST[1]
        AMOUNT = POSSIBLE_MOVE_LIST[2]
        EV = POSSIBLE_MOVE_LIST[3]
        if min(EV) <= 0:
            EV = [elem + abs(min(EV)) + 1 for elem in EV]
        else:
            pass
        EV = [elem / sum(EV) for elem in EV]
        final_move_id = np.random.choice(ID, p=EV)
        final_move = MOVES[final_move_id]
        final_move_amount = AMOUNT[final_move_id]

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
        
        sql_insert_decision_points(poker_db=poker_db, hand_db_format=HAND_DB_FORMAT, stack=stack, pot=pot, \
                                    position=position, phase=phase, nr=nr, history=history[0][0])
        
        for move in possible_moves:
            if move['action'] != 'raise':
                sql_insert_possible_moves(poker_db, move=move['action'], amount=move['amount'])
            else:
                amount = np.random.random_integers(move['amount']['min'], move['amount']['max'])
                sql_insert_possible_moves(poker_db, move=move['action'], amount=amount)

    # poker_db.close()

        return decision_point_based_move(poker_db, phase, nr, pot, position, stack, possible_moves)

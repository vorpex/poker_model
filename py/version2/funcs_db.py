'''database functions'''

# pylint: disable=E1101, E1601, W0612

import numpy as np

sql_path = 'c:\\Users\\adam.sohonyai\\Documents\\GitHub\\poker_model\\sql\\version2\\'

def sql_delete_all(poker_db, table):
    '''delete all rows from table'''

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    delete_sql_file = open(sql_path + 'delete_all.sql').read()
    delete_sql = eval(f'f"""{delete_sql_file}"""')
    poker_cursor.execute(delete_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    return None

def sql_select_tables(poker_db):
    '''query name of all tables from poker_version2 database'''

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'select_tables.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()
    tables = [[*table] for table in zip(*poker_result)]
    # poker_db.close()

    return tables[0]

def sql_games_max_id(poker_db):
    '''query max id from poker_version2.games table'''

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'select_games_max_id.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()
    # poker_db.close()

    return poker_result[0][0]

def sql_insert_games(poker_db, index, player_num, small_blind_amount, ante_amount, uuid, name, stack, position, \
    card1, card2, hand_db_format):
    '''insert rows into poker_version2.games table'''

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

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    insert_sql_file = open(sql_path + 'insert_games.sql').read()
    insert_sql = eval(f'f"""{insert_sql_file}"""')
    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    return None

def sql_insert_history(poker_db, phase, nr, uuid, position, stack, pot, flop1, flop2, flop3, turn, river, \
    action, amount, new_stack, new_pot):
    '''insert rows into poker_version2.games table'''

    game_id = sql_games_max_id(poker_db)

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
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

def decision_point_based_action(poker_db, phase, nr, position, stack, pot, valid_actions):
    '''decision point calculations'''

    game_id = sql_games_max_id(poker_db)
    
    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
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
        
        for move in valid_actions:
            if move['action'] != 'raise':
                sql_insert_possible_moves(poker_db, move=move['action'], amount=move['amount'])
            else:
                amount = np.random.random_integers(move['amount']['min'], move['amount']['max'])
                sql_insert_possible_moves(poker_db, move=move['action'], amount=amount)

    # poker_db.close()

        return decision_point_based_action(poker_db, phase, nr, pot, position, stack, valid_actions)

def sql_update_games_cards(poker_db, index, uuid, card1, card2, hand_db_format):
    '''update card info in poker_version2.games table'''

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    update_sql_file = open(sql_path + 'update_games_cards.sql').read()
    update_sql = eval(f'f"""{update_sql_file}"""')
    poker_cursor.execute(update_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    return None

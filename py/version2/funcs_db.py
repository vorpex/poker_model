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

def sql_insert_decision_points(poker_db, phase, nr, position, hand_db_format, stack, pot, history):
    '''insert rows into poker_version2.decision_points table'''

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'select_decision_points_max_id.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    index = poker_result[0][0] + 1

    insert_sql_file = open(sql_path + 'insert_decision_points.sql').read()
    insert_sql = eval(f'f"""{insert_sql_file}"""')
    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    return None

def sql_insert_possible_moves(poker_db, action, amount, counter=1, total_profit=1, expected_value=1):
    '''insert rows into poker_version2.possible_moves table'''

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'select_decision_points_max_id.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    decision_point_id = poker_result[0][0]
    
    select_sql_file = open(sql_path + 'select_possible_moves_max_id.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    index = poker_result[0][0] + 1
    
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

    hand_db_format = poker_result[0][0]

    select_sql_file = open(sql_path + 'select_decision_points.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    select_sql = select_sql.replace('s.*', 'REPLACE(REPLACE(REPLACE(' +\
        ' CONCAT(\'{\',' +\
        ' GROUP_CONCAT(s.jobj SEPARATOR \',\\' + 'n\'),' +\
        ' \'}\'), \'[\"\', \'[\'), \'\"]\', \']\'), \'\\\\\', \'\') as jobj')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    if poker_result[0][0] != -1:
        decision_point_id = poker_result[0][0]

        select_sql_file = open(sql_path + 'select_possible_moves.sql').read()
        select_sql = eval(f'f"""{select_sql_file}"""')
        poker_cursor.execute(select_sql)
        possible_actions_list = poker_cursor.fetchall()
        
        POSSIBLE_ACTIONS_LIST = [[*elem] for elem in zip(*possible_actions_list)]
        ID = POSSIBLE_ACTIONS_LIST[0]
        ACTION = POSSIBLE_ACTIONS_LIST[1]
        AMOUNT = POSSIBLE_ACTIONS_LIST[2]
        EV = POSSIBLE_ACTIONS_LIST[3]
        if min(EV) <= 0:
            EV = [elem + abs(min(EV)) + 1 for elem in EV]
        else:
            pass
        EV = [elem / sum(EV) for elem in EV]
        final_action_id = np.random.choice(ID, p=EV)
        final_action = ACTION[final_action_id]
        final_action_amount = AMOUNT[final_action_id]

        return final_action, final_action_amount
    else:
        select_sql_file = open(sql_path + 'select_decision_points_history.sql').read()
        select_sql = eval(f'f"""{select_sql_file}"""')
        select_sql = select_sql.replace('s.*', 'REPLACE(REPLACE(REPLACE(' +\
            ' CONCAT(\'{\',' +\
            ' GROUP_CONCAT(s.jobj SEPARATOR \',\\' + 'n\'),' +\
            ' \'}\'), \'[\"\', \'[\'), \'\"]\', \']\'), \'\\\\\', \'\') as jobj')
        poker_cursor.execute(select_sql)
        history = poker_cursor.fetchall()
        
        sql_insert_decision_points(poker_db=poker_db, phase=phase, nr=nr, position=position, \
        hand_db_format=hand_db_format, stack=stack, pot=pot, history=history[0][0])
        
        for action in valid_actions:
            if action['action'] != 'raise':
                sql_insert_possible_moves(poker_db, action=action['action'], amount=action['amount'])
            else:
                amount = np.random.randint(action['amount']['min'], action['amount']['max'] + 1)
                sql_insert_possible_moves(poker_db, action=action['action'], amount=amount)

    # poker_db.close()

        return decision_point_based_action(poker_db=poker_db, phase=phase, nr=nr, position=position, pot=pot, \
        stack=stack, valid_actions=valid_actions)

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

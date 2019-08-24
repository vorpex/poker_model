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

def sql_decision_points_max_id(poker_db):
    '''query max id from poker_version2.decision_points table'''

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'select_decision_points_max_id.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()
    # poker_db.close()

    return poker_result[0][0]

def sql_possible_moves_max_id(poker_db, decision_point_id):
    '''query max id from poker_version2.possible_moves table'''

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'select_possible_moves_max_id.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()
    # poker_db.close()

    return poker_result[0][0]

def sql_stack_result(poker_db, position):
    '''calculate result of game for given position'''

    index = sql_games_max_id(poker_db=poker_db)

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'select_stack_result.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()
    # poker_db.close()
    
    return poker_result[0][0]

def sql_possible_moves_features(poker_db, decision_point_id, action):
    '''select current values of poker_version2.possible_moves.counter and
    poker_version2.possible_moves.total_profit'''

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    select_sql_file = open(sql_path + 'select_possible_moves_features.sql').read()
    select_sql = eval(f'f"""{select_sql_file}"""')
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()
    # poker_db.close()

    return poker_result[0][0], poker_result[0][1]

def sql_insert_games(poker_db, index, player_num, small_blind_amount, ante_amount, uuid, name, stack, position, \
    card1, card2, hand_db_format, flop1, flop2, flop3, turn, river, final_stack):
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

    game_id = sql_games_max_id(poker_db=poker_db)

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    insert_sql_file = open(sql_path + 'insert_history.sql').read()
    insert_sql = eval(f'f"""{insert_sql_file}"""')
    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')

    sql_update_games_board(poker_db=poker_db, index=game_id, flop1=flop1, flop2=flop2, flop3=flop3, \
    turn=turn, river=river)
    # poker_db.close()

    return None

def sql_insert_decision_points(poker_db, phase, nr, position, hand_db_format, stack, pot, history):
    '''insert rows into poker_version2.decision_points table'''

    index = sql_decision_points_max_id(poker_db=poker_db) + 1

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    insert_sql_file = open(sql_path + 'insert_decision_points.sql').read()
    insert_sql = eval(f'f"""{insert_sql_file}"""')
    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    return None

def sql_insert_possible_moves(poker_db, action, bet_amount, counter=1, total_profit=1, expected_value=1):
    '''insert rows into poker_version2.possible_moves table'''

    decision_point_id = sql_decision_points_max_id(poker_db=poker_db)
    index = sql_possible_moves_max_id(poker_db=poker_db, decision_point_id=decision_point_id) + 1
    
    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
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
        BET_AMOUNT = POSSIBLE_ACTIONS_LIST[2]
        EV = POSSIBLE_ACTIONS_LIST[3]
        if min(EV) <= 0:
            EV = [elem + abs(min(EV)) + 1 for elem in EV]

        EV = [elem / sum(EV) for elem in EV]
        final_action_id = np.random.choice(ID, p=EV)
        final_action = ACTION[final_action_id]
        final_action_amount = BET_AMOUNT[final_action_id]

        decision = {'position': position, 'decision_point_id': decision_point_id, 'action': final_action}

        return final_action, final_action_amount, decision
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
                sql_insert_possible_moves(poker_db, action=action['action'], bet_amount=action['amount'])
            else:
                # amount = np.random.randint(action['amount']['min'], action['amount']['max'] + 1)
                sql_insert_possible_moves(poker_db, action=action['action'], bet_amount=action['amount']['min'])

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

def sql_update_games_board(poker_db, index, flop1, flop2, flop3, turn, river):
    '''update card info in poker_version2.games table'''

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    update_sql_file = open(sql_path + 'update_games_board.sql').read()
    update_sql = eval(f'f"""{update_sql_file}"""')
    poker_cursor.execute(update_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    return None

def sql_update_games_final_stack(poker_db, index, uuid, final_stack):
    '''update final stack info in poker_version2.games table at end of game'''

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    update_sql_file = open(sql_path + 'update_games_final_stack.sql').read()
    update_sql = eval(f'f"""{update_sql_file}"""')
    poker_cursor.execute(update_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

    return None

def sql_update_possible_moves(poker_db, position, decision_point_id, action):
    '''update columns in poker_version2.possible_moves table'''

    result = sql_stack_result(poker_db=poker_db, position=position)
    counter, total_profit = sql_possible_moves_features(poker_db=poker_db, \
    decision_point_id = decision_point_id, action=action)

    if counter == 1 and total_profit == 1:
        total_profit = result
    else:
        counter = counter + 1
        total_profit = total_profit + result
    
    expected_value = total_profit / counter

    # poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker_version2')
    poker_cursor = poker_db.cursor()
    update_sql_file = open(sql_path + 'update_possible_moves.sql').read()
    update_sql = eval(f'f"""{update_sql_file}"""')
    poker_cursor.execute(update_sql)
    poker_cursor.execute('COMMIT')
    # poker_db.close()

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

    fold_actions = fold_check(actions=actions, phase=phase, position=position, \
    small_blind_amount=small_blind_amount)
    call_actions = call_check(actions=fold_actions, stack=stack)
    final_actions = raise_check(actions=call_actions, stack=stack)

    return final_actions

def fold_check(actions, phase, position, small_blind_amount):
    '''check fold action'''

    remove_fold_flag = 0
    for action in actions:

        if action['action'] == 'call' and (action['amount'] == 0 or (action['amount'] == small_blind_amount * 2 \
        and phase == 'preflop' and position == 2)):
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

        if action['action'] == 'raise' and action['amount']['min'] == -1 and action['amount']['max'] == -1:
            action['amount']['min'] = stack
            action['amount']['max'] = stack
    
    raise_actions = actions

    return raise_actions

def summarize(poker_db, final_stacks, summary):
    '''summarize the result of round'''

    index = sql_games_max_id(poker_db)

    for final_stack in final_stacks:

        sql_update_games_final_stack(poker_db=poker_db, index=index, uuid=final_stack['uuid'], \
        final_stack=final_stack['stack'])
    
    for decision in summary:

        sql_update_possible_moves(poker_db=poker_db, position=decision['position'], \
        decision_point_id=decision['decision_point_id'], action=decision['action'])

    return None

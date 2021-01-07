'''database functions - insert'''

# pylint: disable=E0401, E1101, E1601, W0612

import funcs_sql_sel as fsqls
import funcs_sql_upd as fsqlu

def sql_insert_games(poker_db, database, sql_path, index, player_num,
    small_blind_amount, ante_amount, uuid, name, stack, position, card1, card2, hand_db_format,
    flop1, flop2,flop3, turn, river, final_stack):
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
    
    poker_cursor = poker_db.cursor()
    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')

    insert_sql_file.close()

    return None

def sql_insert_history(poker_db, database, sql_path, phase, nr, step, uuid, position, stack,
    stack_range, pot, pot_range, flop1, flop2, flop3, turn, river, action, amount,
    new_stack, new_stack_range, new_pot, new_pot_range, amount_potrate):
    '''insert rows into games table'''

    game_id = fsqls.sql_games_max_id(poker_db=poker_db, database=database, sql_path=sql_path)

    insert_sql_file = open(sql_path + 'insert_history.sql')
    insert_sql = insert_sql_file.read()
    insert_sql = eval(f'f"""{insert_sql}"""')

    poker_cursor = poker_db.cursor()
    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')

    fsqlu.sql_update_games_board(poker_db=poker_db, database=database, sql_path=sql_path,
        index=game_id, flop1=flop1, flop2=flop2, flop3=flop3, turn=turn, river=river)

    insert_sql_file.close()

    return None

def sql_insert_decision_points(poker_db, database, sql_path, phase, nr, position, hand_db_format,
    win_rate, stack_range, pot_range, history):
    '''insert rows into decision_points table'''

    index = fsqls.sql_decision_points_max_id(poker_db=poker_db, database=database,
        sql_path=sql_path) + 1

    insert_sql_file = open(sql_path + 'insert_decision_points.sql')
    insert_sql = insert_sql_file.read()
    insert_sql = eval(f'f"""{insert_sql}"""')

    poker_cursor = poker_db.cursor()
    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')

    insert_sql_file.close()

    return None

def sql_insert_possible_moves(poker_db, database, sql_path, action, bet_amount_range, counter=1,
    total_profit=1, expected_value=1):
    '''insert rows into possible_moves table'''

    decision_point_id = fsqls.sql_decision_points_max_id(poker_db=poker_db, database=database,
        sql_path=sql_path)
    index = fsqls.sql_possible_moves_max_id(poker_db=poker_db, database=database,
        sql_path=sql_path, decision_point_id=decision_point_id) + 1

    insert_sql_file = open(sql_path + 'insert_possible_moves.sql')
    insert_sql = insert_sql_file.read()
    insert_sql = eval(f'f"""{insert_sql}"""')

    poker_cursor = poker_db.cursor()
    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')

    insert_sql_file.close()

    return None

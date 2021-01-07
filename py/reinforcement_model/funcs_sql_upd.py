'''database functions - update'''

# pylint: disable=E0401, E1101, E1601, W0612

import funcs_sql_sel as fsqls

def sql_update_games_cards(poker_db, database, sql_path, index, uuid, card1, card2, hand_db_format):
    '''update card info in games table'''

    update_sql_file = open(sql_path + 'update_games_cards.sql')
    update_sql = update_sql_file.read()
    update_sql = eval(f'f"""{update_sql}"""')

    poker_cursor = poker_db.cursor()
    poker_cursor.execute(update_sql)
    poker_cursor.execute('COMMIT')

    update_sql_file.close()

    return None

def sql_update_games_board(poker_db, database, sql_path, index, flop1, flop2, flop3, turn, river):
    '''update card info in games table'''

    update_sql_file = open(sql_path + 'update_games_board.sql')
    update_sql = update_sql_file.read()
    update_sql = eval(f'f"""{update_sql}"""')

    poker_cursor = poker_db.cursor()
    poker_cursor.execute(update_sql)
    poker_cursor.execute('COMMIT')

    update_sql_file.close()

    return None

def sql_update_games_final_stack(poker_db, database, sql_path, index, uuid, final_stack):
    '''update final stack info in games table at end of game'''

    update_sql_file = open(sql_path + 'update_games_final_stack.sql')
    update_sql = update_sql_file.read()
    update_sql = eval(f'f"""{update_sql}"""')

    poker_cursor = poker_db.cursor()
    poker_cursor.execute(update_sql)
    poker_cursor.execute('COMMIT')

    update_sql_file.close()

    return None

def sql_update_possible_moves(poker_db, database, sql_path, index):
    '''update columns in possible_moves table'''

    select_sql_file = open(sql_path + 'select_possible_moves_history.sql')
    select_sql = select_sql_file.read()
    select_sql = eval(f'f"""{select_sql}"""')

    poker_cursor = poker_db.cursor()
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    select_sql_file.close()

    for item in poker_result:
        decision_point_id = item[1]
        id = item[2]
        counter = item[7]
        total_profit = item[8]
        result = item[11]
    
        if counter == 1 and total_profit == 1:
            total_profit = result
        else:
            counter = counter + 1
            total_profit = total_profit + result
    
        expected_value = total_profit / counter

        update_sql_file = open(sql_path + 'update_possible_moves.sql')
        update_sql = update_sql_file.read()
        update_sql = eval(f'f"""{update_sql}"""')

        poker_cursor = poker_db.cursor()
        poker_cursor.execute(update_sql)
        poker_cursor.execute('COMMIT')

        update_sql_file.close()

    return None

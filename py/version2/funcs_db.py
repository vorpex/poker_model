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

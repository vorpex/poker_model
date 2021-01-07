'''database functions - select'''

# pylint: disable=E0401, E1101, E1601, W0612

def sql_select_tables(poker_db, database, sql_path):
    '''query name of all tables from database'''

    select_sql_file = open(sql_path + 'select_tables.sql')
    select_sql = select_sql_file.read()
    select_sql = eval(f'f"""{select_sql}"""')

    poker_cursor = poker_db.cursor()
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()
    tables = [[*table] for table in zip(*poker_result)]

    select_sql_file.close()

    return tables[0]

def sql_games_max_id(poker_db, database, sql_path):
    '''query max id from games table'''

    select_sql_file = open(sql_path + 'select_games_max_id.sql')
    select_sql = select_sql_file.read()
    select_sql = eval(f'f"""{select_sql}"""')

    poker_cursor = poker_db.cursor()
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    select_sql_file.close()

    return poker_result[0][0]

def sql_decision_points_max_id(poker_db, database, sql_path):
    '''query max id from decision_points table'''

    select_sql_file = open(sql_path + 'select_decision_points_max_id.sql')
    select_sql = select_sql_file.read()
    select_sql = eval(f'f"""{select_sql}"""')

    poker_cursor = poker_db.cursor()
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    select_sql_file.close()

    return poker_result[0][0]

def sql_possible_moves_max_id(poker_db, database, sql_path, decision_point_id):
    '''query max id from possible_moves table'''

    select_sql_file = open(sql_path + 'select_possible_moves_max_id.sql')
    select_sql = select_sql_file.read()
    select_sql = eval(f'f"""{select_sql}"""')

    poker_cursor = poker_db.cursor()
    poker_cursor.execute(select_sql)
    poker_result = poker_cursor.fetchall()

    select_sql_file.close()

    return poker_result[0][0]

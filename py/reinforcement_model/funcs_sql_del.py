'''database functions - delete'''

# pylint: disable=E0401, E1101, E1601, W0612

def sql_delete_allrows(poker_db, database, table, sql_path):
    '''delete all rows from table'''

    delete_sql_file = open(sql_path + 'delete_allrows.sql')
    delete_sql = delete_sql_file.read()
    delete_sql = eval(f'f"""{delete_sql}"""')

    poker_cursor = poker_db.cursor()
    poker_cursor.execute(delete_sql)
    poker_cursor.execute('COMMIT')

    delete_sql_file.close()

    return None

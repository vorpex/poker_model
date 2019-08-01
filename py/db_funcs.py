'''database functions'''

# pylint: disable=E1101, E1601, W0612

import mysql.connector

import pplayer
import ppot

def sql_delete_all(table):
    '''delete all rows from table'''

    poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker')
    poker_cursor = poker_db.cursor()

    delete_sql = 'DELETE FROM poker.' + str(table) + ' WHERE 1 = 1'
    poker_cursor.execute(delete_sql)
    poker_cursor.execute('COMMIT')

    poker_db.close()

    return None

def sql_insert_games(values_list):
    '''insert row into games table'''

    poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker')
    poker_cursor = poker_db.cursor()

    poker_cursor.execute('SELECT NVL(MAX(t.id), -1) AS max_id FROM poker.games t')
    poker_result = poker_cursor.fetchall()
    
    insert_sql = 'INSERT INTO poker.games VALUES (' + str(poker_result[0][0] + 1) + ', '
    for value in values_list:
        insert_sql = insert_sql + str(value) + ', '
    
    insert_sql = insert_sql[:-2] + ')'
    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')

    poker_db.close()

    return None

def sql_insert_history(values_list):
    '''insert row into history table'''

    poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker')
    poker_cursor = poker_db.cursor()

    poker_cursor.execute('SELECT MAX(t.id) AS max_id FROM poker.games t')
    poker_result = poker_cursor.fetchall()

    insert_sql = 'INSERT INTO poker.history VALUES (' + str(poker_result[0][0]) + ', ' + \
        str(values_list[0]) + ', ' + \
        str(values_list[1]) + ', ' + \
        '\'' + str(values_list[2]) + '\', ' + \
        str(values_list[3]) + ', ' + \
        str(values_list[4]) + ', ' + \
        str(values_list[5]) + ', ' + \
        '\'' + str(values_list[6]) + '\', ' + \
        '\'' + str(values_list[7]) + '\', ' + \
        '\'' + str(values_list[8]) + '\', ' + \
        '\'' + str(values_list[9]) + '\', ' + \
        '\'' + str(values_list[10]) + '\', ' + \
        '\'' + str(values_list[11]) + '\', ' + \
        str(values_list[12]) + ', '  + \
        str(values_list[13]) + ', '  + \
        str(values_list[14]) + ')'

    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')

    poker_db.close()

    return None

def table_init(nr_of_players, starting_stack):
    '''players initialization'''

    pot = ppot.Pot()

    players = []
    for i in range(nr_of_players):

        players.append(pplayer.Player(i, starting_stack))
        players[i].add_position(i)

    return pot, players

def descision_point(hand, stack, pot, position=2, phase=0, nr=2):
    '''decision point calculations'''

    return None

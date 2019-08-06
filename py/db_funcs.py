'''database functions'''

# pylint: disable=E1101, E1601, W0612

import mysql.connector
import numpy as np

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

    poker_cursor.execute('SELECT NVL(MAX(g.id), -1) AS max_id FROM poker.games g')
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

    poker_cursor.execute('SELECT MAX(g.id) AS max_id FROM poker.games g')
    poker_result = poker_cursor.fetchall()

    insert_sql = 'INSERT INTO poker.history VALUES (' + str(poker_result[0][0]) + ', ' +\
        str(values_list[0]) + ', ' +\
        str(values_list[1]) + ', ' +\
        '\'' + str(values_list[2]) + '\', ' +\
        str(values_list[3]) + ', ' +\
        str(values_list[4]) + ', ' +\
        str(values_list[5]) + ', ' +\
        '\'' + str(values_list[6]) + '\', ' +\
        '\'' + str(values_list[7]) + '\', ' +\
        '\'' + str(values_list[8]) + '\', ' +\
        '\'' + str(values_list[9]) + '\', ' +\
        '\'' + str(values_list[10]) + '\', ' +\
        '\'' + str(values_list[11]) + '\', ' +\
        str(values_list[12]) + ', '  +\
        str(values_list[13]) + ', '  +\
        str(values_list[14]) + ')'

    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')

    poker_db.close()

    return None

def sql_insert_decision_points(values_list):
    '''insert row into decision points table'''

    poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker')
    poker_cursor = poker_db.cursor()

    poker_cursor.execute('SELECT NVL(MAX(d.id), -1) AS max_id FROM poker.decision_points d')
    poker_result = poker_cursor.fetchall()

    insert_sql = 'INSERT INTO poker.decision_points VALUES (' + str(poker_result[0][0] + 1) + ', ' +\
        '\'' + str(values_list[0]) + '\', ' +\
        str(values_list[1]) + ', ' +\
        str(values_list[2]) + ', ' +\
        str(values_list[3]) + ', ' +\
        str(values_list[4]) + ', ' +\
        str(values_list[5]) + ', ' +\
        '\'' + str(values_list[6]) + '\')'

    poker_cursor.execute(insert_sql)
    poker_cursor.execute('COMMIT')

    poker_db.close()

    return None

def sql_insert_possible_moves(values_list):
    '''insert row into possible moves table'''

    poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker')
    poker_cursor = poker_db.cursor()

    poker_cursor.execute('SELECT NVL(MAX(d.id), -1) AS max_id FROM poker.decision_points d')
    poker_result = poker_cursor.fetchall()

    insert_sql = 'INSERT INTO poker.possible_moves VALUES (' + str(poker_result[0][0]) + ', ' +\
        '\'' + str(values_list[0]) + '\', ' +\
        str(values_list[1]) + ', ' +\
        '1, ' +\
        '1, ' +\
        '1)'

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

def check_moves(last_move):
    '''check possibile moves'''

    if last_move is None:
        moves = ['check', 'bet', 'allin']
    elif last_move == 'small_blind':
        moves = ['fold', 'call', 'raise', 'allin']
    elif last_move == 'big_blind':
        moves = ['fold', 'call', 'raise', 'allin']
    elif last_move == 'fold':
        moves = ['call', 'raise', 'allin']
    elif last_move == 'check':
        moves = ['check', 'bet', 'allin']
    elif last_move == 'call':
        moves = ['fold', 'call', 'raise', 'allin']
    elif last_move == 'bet':
        moves = ['fold', 'call', 'raise', 'allin']
    elif last_move == 'raise':
        moves = ['fold', 'call', 'raise', 'allin']
    elif last_move == 'allin':
        moves = ['fold', 'call', 'raise', 'allin']
    else:
        pass

    return moves

def decision_point(hand, stack, pot, position=2, phase=0, nr=2):
    '''decision point calculations'''

    poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker')
    poker_cursor = poker_db.cursor()

    poker_cursor.execute('SELECT MAX(g.id) AS max_id FROM poker.games g')
    max_id = poker_cursor.fetchall()

    poker_cursor.execute(
        'SELECT\n' +\
        '  NVL(MAX(d.id), -1) AS id\n' +\
        '\n' +\
        'FROM\n' +\
        '  poker.decision_points d\n' +\
        '\n' +\
        'WHERE\n' +\
        '  1 = 1\n' +\
        '  AND d.hand = \'' + str(hand) + '\'\n' +\
        '  AND d.stack = ' + str(stack) + '\n' +\
        '  AND d.pot = ' + str(pot) + '\n' +\
        '  AND d.position = ' + str(position) + '\n' +\
        '  AND d.phase = ' + str(phase) + '\n' +\
        '  AND d.nr = ' + str(nr) + '\n' +\
        '  AND d.history in (\n' +\
        '\n' +\
        '  SELECT\n' +\
        '    REPLACE(REPLACE(REPLACE(\n' +\
        '      concat(\'{\',\n' +\
        '      GROUP_CONCAT(s.jobj SEPARATOR \',\\' + 'n' + '\'),\n' +\
        '      \'}\'), \'[\"\', \'[\'), \'\"]\', \']\'), \'\\\\\', \'\') as jobj\n' +\
        '\n' +\
        '  FROM (\n' +\
        '    SELECT concat(\'\"phase\":\', json_array(GROUP_CONCAT(h.phase))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
        '    UNION\n' +\
        '    SELECT concat(\'\"nr\":\', json_array(GROUP_CONCAT(h.nr))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
        '    UNION\n' +\
        '    SELECT concat(\'\"position\":\', json_array(GROUP_CONCAT(h.position))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
        '    UNION\n' +\
        '    SELECT concat(\'\"stack\":\', json_array(GROUP_CONCAT(h.stack))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
        '    UNION\n' +\
        '    SELECT concat(\'\"pot\":\', json_array(GROUP_CONCAT(h.pot))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
        '    UNION\n' +\
        '    SELECT concat(\'\"flop1\":\', json_array(GROUP_CONCAT(concat(\'\"\', h.flop1, \'\"\')))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
        '    UNION\n' +\
        '    SELECT concat(\'\"flop2\":\', json_array(GROUP_CONCAT(concat(\'\"\', h.flop2, \'\"\')))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
        '    UNION\n' +\
        '    SELECT concat(\'\"flop3\":\', json_array(GROUP_CONCAT(concat(\'\"\', h.flop3, \'\"\')))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
        '    UNION\n' +\
        '    SELECT concat(\'\"turn\":\', json_array(GROUP_CONCAT(concat(\'\"\', h.turn, \'\"\')))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
        '    UNION\n' +\
        '    SELECT concat(\'\"river\":\', json_array(GROUP_CONCAT(concat(\'\"\', h.river, \'\"\')))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
        '    UNION\n' +\
        '    SELECT concat(\'\"move\":\', json_array(GROUP_CONCAT(concat(\'\"\', h.move, \'\"\')))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
        '    UNION\n' +\
        '    SELECT concat(\'\"amount\":\', json_array(GROUP_CONCAT(h.amount))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
        '  ) s\n' +\
        '\n' +\
        ')'
    )
    decision_point_id = poker_cursor.fetchall()

    if decision_point_id[0][0] != -1:
        poker_cursor.execute(
            'SELECT\n' +\
            '  p.move,\n' +\
            '  p.expected_value\n' +\
            '\n' +\
            'FROM\n' +\
            '  poker.possible_moves p\n' +\
            '\n' +\
            'WHERE\n' +\
            '  1 = 1\n' +\
            '  AND p.decision_point_id = ' + str(decision_point_id[0][0])
        )
        possible_moves_list = poker_cursor.fetchall()
        possible_moves_list = [[*elem] for elem in zip(*possible_moves_list)]

        MOVES = possible_moves_list[0]
        EV = possible_moves_list[1]
        if min(EV) <= 0:
            EV = [elem + abs(min(EV)) + 1 for elem in EV]
        else:
            pass
        EV = [elem / sum(EV) for elem in EV]
        final_move = np.random.choice(MOVES, p=EV)

        poker_db.close()

        return final_move
    else:
        poker_cursor.execute(
            'SELECT\n' +\
            '  REPLACE(REPLACE(REPLACE(\n' +\
            '    concat(\'{\',\n' +\
            '    GROUP_CONCAT(s.jobj SEPARATOR \',\\' + 'n' + '\'),\n' +\
            '    \'}\'), \'[\"\', \'[\'), \'\"]\', \']\'), \'\\\\\', \'\') as jobj\n' +\
            '\n' +\
            'FROM (\n' +\
            '  SELECT concat(\'\"phase\":\', json_array(GROUP_CONCAT(h.phase))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
            '  UNION\n' +\
            '  SELECT concat(\'\"nr\":\', json_array(GROUP_CONCAT(h.nr))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
            '  UNION\n' +\
            '  SELECT concat(\'\"position\":\', json_array(GROUP_CONCAT(h.position))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
            '  UNION\n' +\
            '  SELECT concat(\'\"stack\":\', json_array(GROUP_CONCAT(h.stack))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
            '  UNION\n' +\
            '  SELECT concat(\'\"pot\":\', json_array(GROUP_CONCAT(h.pot))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
            '  UNION\n' +\
            '  SELECT concat(\'\"flop1\":\', json_array(GROUP_CONCAT(concat(\'\"\', h.flop1, \'\"\')))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
            '  UNION\n' +\
            '  SELECT concat(\'\"flop2\":\', json_array(GROUP_CONCAT(concat(\'\"\', h.flop2, \'\"\')))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
            '  UNION\n' +\
            '  SELECT concat(\'\"flop3\":\', json_array(GROUP_CONCAT(concat(\'\"\', h.flop3, \'\"\')))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
            '  UNION\n' +\
            '  SELECT concat(\'\"turn\":\', json_array(GROUP_CONCAT(concat(\'\"\', h.turn, \'\"\')))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
            '  UNION\n' +\
            '  SELECT concat(\'\"river\":\', json_array(GROUP_CONCAT(concat(\'\"\', h.river, \'\"\')))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
            '  UNION\n' +\
            '  SELECT concat(\'\"move\":\', json_array(GROUP_CONCAT(concat(\'\"\', h.move, \'\"\')))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
            '  UNION\n' +\
            '  SELECT concat(\'\"amount\":\', json_array(GROUP_CONCAT(h.amount))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = ' + str(max_id[0][0]) + ' AND h.nr < ' + str(nr) + '\n' +\
            ') s'
        )
        history = poker_cursor.fetchall()
        
        values_list = [hand, stack, pot, position, phase, nr, history[0][0]]
        sql_insert_decision_points(values_list=values_list)

        poker_cursor.execute(
            'SELECT\n' +\
            '  h.move' +\
            '\n' +\
            'FROM\n' +\
            '  poker.history h\n' +\
            '\n' +\
            'WHERE\n' +\
            '  1 = 1\n' +\
            '  AND h.game_id = ' + str(max_id[0][0]) + '\n' +\
            '  AND h.phase = ' + str(phase) + '\n' +\
            '\n' +\
            'ORDER BY\n' +\
            '  h.nr DESC\n' +\
            '\n' +\
            'LIMIT 1'
        )
        last_move = poker_cursor.fetchall()
        for move in check_moves(last_move=last_move[0][0]):
            if move in ['fold', 'check']:
                amount = 0
            else:
                amount = 5
            sql_insert_possible_moves(values_list=[move, amount])

        poker_db.close()

        return decision_point(hand, stack, pot, position, phase, nr)

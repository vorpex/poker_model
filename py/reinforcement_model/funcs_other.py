'''other functions'''

# pylint: disable=E0401, E1101, E1601, W0612

import os
from pypokerengine.utils.card_utils import gen_cards, estimate_hole_card_win_rate

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

def winrate_calc(hole_cards, community_cards, nb_player):
    '''function to calculate win rate'''

    board = []
    if community_cards[0] != '':
        board.append(community_cards[0])
    
    if community_cards[1] != '':
        board.append(community_cards[1])
    
    if community_cards[2] != '':
        board.append(community_cards[2])
    
    if community_cards[3] != '':
        board.append(community_cards[3])
    
    if community_cards[4] != '':
        board.append(community_cards[4])

    if len(board) >= 3:
        win_rate = estimate_hole_card_win_rate(nb_simulation=1000, nb_player=nb_player, 
            hole_card=gen_cards([hole_cards[0], hole_cards[1]]), community_card=gen_cards(board))
        win_rate = str(round(int(win_rate / 0.05) * 0.05, 2)) + '-' + \
                    str(round((int(win_rate / 0.05) + 1) * 0.05, 2))
    else:
        win_rate = '-1'
    
    return win_rate

def run_checksum(poker_db, database, sql_checksum):
    '''function to check the generated games in database'''

    checksums = {}
    checksum_counter = 0

    files = os.listdir(sql_checksum)
    for file in files:
        checksums[file[:-4]] = ''
        select_sql_file = open(sql_checksum + file)
        select_sql = select_sql_file.read()
        select_sql = eval(f'f"""{select_sql}"""')

        checksum_cursor = poker_db.cursor()
        checksum_cursor.execute(select_sql)
        checksum_result = checksum_cursor.fetchall()

        checksums[file[:-4]] = float(checksum_result[0][0])
        checksum_counter = checksum_counter + float(checksum_result[0][0])
        
        select_sql_file.close()

    # print('Sum of checksums:', checksum_counter, '(If it is zero then everything is OK)')

    return checksums, checksum_counter

'''check poker moves'''

# pylint: disable=E1101, E1601, W0612

import sys
sys.path.append('c:\\ProgramData\\Anaconda3\\Lib\\site-packages\\deuces\\')

import pcard
import pboard
import pdeck
import phand
import pplayer
import ppot

def check_fold_move(player):
    '''check fold move possibility
    
    - Extend with game_id for game history

    Select the previouse move from database
    '''

    if isinstance(player, pplayer.Player):
        previouse_move = '...'
        if previouse_move in ['small_blind_move', 'big_blind_move', 'fold_move', 'call_move', \
                            'bet_move', 'raise_move', 'allin_move']:
            move_flag = 1
        else:
            move_flag = 0
    else:
        raise TypeError('Wrong type')

    return move_flag

def check_check_move(player):
    '''check check move possibility
    
    - Extend with game_id for game history

    Select the previouse move from database
    '''

    if isinstance(player, pplayer.Player):
        previouse_move = '...'
        if previouse_move in ['', 'check']:
            move_flag = 1
        else:
            move_flag = 0
    else:
        raise TypeError('Wrong type')                                    

    return move_flag

def check_call_move(player):
    '''check call move possibility
    
    - Extend with game_id for game history

    Select the previouse move from database
    '''

    if isinstance(player, pplayer.Player):
        previouse_move = '...'
        if previouse_move in ['small_blind_move', 'big_blind_move', 'fold', 'call', 'bet', 'raise', 'allin']:
            move_flag = 1
        else:
            move_flag = 0
    else:
        raise TypeError('Wrong type')

    return move_flag

def check_bet_move(player):
    '''check bet move possibility
    
    - Extend with game_id for game history

    Select the previouse move from database
    '''

    if isinstance(player, pplayer.Player):
        previouse_move = '...'
        if previouse_move in ['', 'check']:
            move_flag = 1
        else:
            move_flag = 0
    else:
        raise TypeError('Wrong type')

    return move_flag

def check_raise_move(player):
    '''check raise move possibility
    
    - Extend with game_id for game history

    Select the previouse move from database
    '''

    if isinstance(player, pplayer.Player):
        previouse_move = '...'
        if previouse_move in ['fold', 'call', 'bet', 'raise', 'allin']:
            move_flag = 1
        else:
            move_flag = 0
    else:
        raise TypeError('Wrong type')

    return move_flag

def check_allin_move(player):
    '''check allin move possibility
    
    - Extend with game_id for game history

    Select the previouse move from database
    '''

    if isinstance(player, pplayer.Player):
        previouse_move = '...'
        if previouse_move in ['', 'fold', 'check', 'call', 'bet', 'raise', 'allin']:
            move_flag = 1
        else:
            move_flag = 0
    else:
        raise TypeError('Wrong type')

    return move_flag

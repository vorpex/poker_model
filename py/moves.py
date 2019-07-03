'''poker moves'''

# pylint: disable=E1101, E1601, W0612

import sys
sys.path.append('c:\\ProgramData\\Anaconda3\\Lib\\site-packages\\deuces\\')

import pcard
import pboard
import pdeck
import phand
import pplayer
import ppot

def small_blind_move(player, small_blind, pot):
    '''small blind move'''
    
    if isinstance(player, pplayer.Player) and isinstance(pot, ppot.Pot):
        player.decrease_chips(small_blind)
        pot.increase_pot(small_blind)
    else:
        raise TypeError('Wrong type(s)')
    
    return 'small_blind_move', player.position_nr(), small_blind

def big_blind_move(player, big_blind, pot):
    '''big blind move'''
    
    if isinstance(player, pplayer.Player) and isinstance(pot, ppot.Pot):
        player.decrease_chips(big_blind)
        pot.increase_pot(big_blind)
    else:
        raise TypeError('Wrong type(s)')

    return 'big_blind_move', player.position_nr(), big_blind

def fold_move(player, player_move_flags):
    '''fold move'''

    if isinstance(player, pplayer.Player):
        player_move_flags[player.position_nr()] = 0
    else:
        raise TypeError('Wrong type')

    return 'fold_move', player.position_nr()

def check_move(player):
    '''check move'''

    if isinstance(player, pplayer.Player):
        pass
    else:
        raise TypeError('Wrong type')

    return 'check_move', player.position_nr()

def call_move(player, call_amount, pot):
    '''call move'''

    if isinstance(player, pplayer.Player) and isinstance(pot, ppot.Pot):
        player.decrease_chips(call_amount)
        pot.increase_pot(call_amount)
    else:
        raise TypeError('Wrong type(s)')

    return 'call_move', player.position_nr(), call_amount

def bet_move(player, bet_amount, pot):
    '''bet move'''

    if isinstance(player, pplayer.Player) and isinstance(pot, ppot.Pot):
        player.decrease_chips(bet_amount)
        pot.increase_pot(bet_amount)
    else:
        raise TypeError('Wrong type(s)')

    return 'bet_move', player.position_nr(), bet_amount

def raise_move(player, raise_amount, pot):
    '''raise move'''

    if isinstance(player, pplayer.Player) and isinstance(pot, ppot.Pot):
        player.decrease_chips(raise_amount)
        pot.increase_pot(raise_amount)
    else:
        raise TypeError('Wrong type(s)')

    return 'raise_move', player.position_nr(), raise_amount

def allin_move(player, pot):
    '''allin move'''

    if isinstance(player, pplayer.Player) and isinstance(pot, ppot.Pot):
        pot.increase_pot(player.chips())
        player.decrease_chips(player.chips())
    else:
        raise TypeError('Wrong type(s)')

    return 'allin_move', player.position_nr(), player.chips()

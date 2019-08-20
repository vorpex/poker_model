'''poker moves'''

# pylint: disable=E1101, E1601, W0612

import numpy as np

import funcs_db

import pplayer
import ppot

def table_init(number_of_players, player0_stack, player1_stack, player2_stack, player3_stack, \
    player4_stack, player5_stack):
    '''players initialization'''

    pot = ppot.Pot()

    players = []
    for i in range(number_of_players):

        if i == 0:
            stack = player0_stack
        elif i == 1:
            stack = player1_stack
        elif i == 2:
            stack = player2_stack
        elif i == 3:
            stack = player3_stack
        elif i == 4:
            stack = player4_stack
        else:
            stack = player5_stack

        players.append(pplayer.Player(i, stack))
        players[i].add_position(i)

    return pot, players

def move(poker_db, player, pot, move, phase=0, nr=0, flop1='none', flop2='none', flop3='none', turn='none', \
    river='none', amount=0):
    '''move'''

    if isinstance(player, pplayer.Player) and isinstance(pot, ppot.Pot):
        funcs_db.sql_insert_history(poker_db=poker_db, phase=phase, nr=nr, player_name=player.general_name(), \
            position=player.position_nr(), stack=player.stack(), pot=pot.show_pot(), \
            flop1=flop1, flop2=flop2, flop3=flop3, turn=turn, river=river, move=move, \
            amount=amount, new_stack=player.stack() - amount, new_pot=pot.show_pot() + amount)
        player.decrease_stack(amount)
        pot.increase_pot(amount)
    else:
        raise TypeError('Wrong type(s)')
    
    return None

def check_moves(last_move, sum_amount, stack, position):
    '''check possibile moves'''

    if sum_amount >= stack:
        call_amount = int(stack)
    else:
        call_amount = int(sum_amount)
        new_stack = stack - call_amount
        raise_amount = int(call_amount + np.random.random_integers(1, new_stack))

    if last_move is None or last_move == 'check':
        moves = {'check': 0, 'raise': raise_amount}
    elif position == 1 and sum_amount == 0 and last_move in ['fold', 'call']:
        moves = {'check': 0, 'raise': raise_amount}
    elif last_move in ['small_blind', 'big_blind', 'fold', 'call', 'raise']:
        moves = {'fold': 0, 'call': call_amount, 'raise': raise_amount}
    else:
        pass

    return moves

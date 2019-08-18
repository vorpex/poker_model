'''poker moves'''

# pylint: disable=E1101, E1601, W0612

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

def move(poker_db, player, move, pot, phase=0, nr=0, flop1='none', flop2='none', flop3='none', turn='none', river='none', \
        amount=0):
    '''move'''

    if isinstance(player, pplayer.Player) and isinstance(pot, ppot.Pot):
        funcs_db.sql_insert_history(poker_db=poker_db, values_list=[phase, nr, player.general_name(), player.position_nr(), player.stack(), \
            pot.show_pot(), flop1, flop2, flop3, turn, river, move, amount, player.stack() - amount, \
            pot.show_pot() + amount])
        player.decrease_stack(amount)
        pot.increase_pot(amount)
    else:
        raise TypeError('Wrong type(s)')
    
    return None

def check_moves(last_move):
    '''check possibile moves'''

    if last_move is None:
        moves = ['check', 'raise']
    elif last_move == 'small_blind':
        moves = ['fold', 'call', 'raise']
    elif last_move == 'big_blind':
        moves = ['fold', 'call', 'raise']
    elif last_move == 'fold':
        moves = ['call', 'raise']
    elif last_move == 'check':
        moves = ['check', 'raise']
    elif last_move == 'call':
        moves = ['fold', 'call', 'raise']
    elif last_move == 'raise':
        moves = ['fold', 'call', 'raise']
    else:
        pass

    return moves

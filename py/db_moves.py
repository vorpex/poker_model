'''poker moves'''

# pylint: disable=E1101, E1601, W0612

import db_funcs

import pplayer
import ppot

def small_blind_move(player, pot, phase=0, nr=0, flop1='none', flop2='none', flop3='none', turn='none', river='none', \
        amount=0, move='small_blind'):
    '''small blind move'''

    if isinstance(player, pplayer.Player) and isinstance(pot, ppot.Pot):
        db_funcs.sql_insert_history(values_list=[phase, nr, player.general_name(), player.position_nr(), player.stack(), \
            pot.show_pot(), flop1, flop2, flop3, turn, river, move, amount, player.stack() - amount, \
            pot.show_pot() + amount])
        player.decrease_stack(amount)
        pot.increase_pot(amount)
    else:
        raise TypeError('Wrong type(s)')
    
    return None

def big_blind_move(player, pot, phase=0, nr=1, flop1='none', flop2='none', flop3='none', turn='none', river='none', \
        amount=0, move='big_blind'):
    '''big blind move'''

    if isinstance(player, pplayer.Player) and isinstance(pot, ppot.Pot):
        db_funcs.sql_insert_history(values_list=[phase, nr, player.general_name(), player.position_nr(), player.stack(), \
            pot.show_pot(), flop1, flop2, flop3, turn, river, move, amount, player.stack() - amount, \
            pot.show_pot() + amount])
        player.decrease_stack(amount)
        pot.increase_pot(amount)
    else:
        raise TypeError('Wrong type(s)')
    
    return None

def fold_move(player, pot, phase=0, nr=2, flop1='none', flop2='none', flop3='none', turn='none', river='none', \
        amount=0, move='fold'):
    '''fold move'''

    if isinstance(player, pplayer.Player) and isinstance(pot, ppot.Pot):
        db_funcs.sql_insert_history(values_list=[phase, nr, player.general_name(), player.position_nr(), player.stack(), \
            pot.show_pot(), flop1, flop2, flop3, turn, river, move, amount, player.stack() - amount, \
            pot.show_pot() + amount])
        player.decrease_stack(amount)
        pot.increase_pot(amount)
    else:
        raise TypeError('Wrong type(s)')
    
    return None

def check_move(player, pot, phase=0, nr=2, flop1='none', flop2='none', flop3='none', turn='none', river='none', \
        amount=0, move='check'):
    '''check move'''

    if isinstance(player, pplayer.Player) and isinstance(pot, ppot.Pot):
        db_funcs.sql_insert_history(values_list=[phase, nr, player.general_name(), player.position_nr(), player.stack(), \
            pot.show_pot(), flop1, flop2, flop3, turn, river, move, amount, player.stack() - amount, \
            pot.show_pot() + amount])
        player.decrease_stack(amount)
        pot.increase_pot(amount)
    else:
        raise TypeError('Wrong type(s)')
    
    return None

def call_move(player, pot, phase=0, nr=2, flop1='none', flop2='none', flop3='none', turn='none', river='none', \
        amount=0, move='call'):
    '''call move'''

    if isinstance(player, pplayer.Player) and isinstance(pot, ppot.Pot):
        db_funcs.sql_insert_history(values_list=[phase, nr, player.general_name(), player.position_nr(), player.stack(), \
            pot.show_pot(), flop1, flop2, flop3, turn, river, move, amount, player.stack() - amount, \
            pot.show_pot() + amount])
        player.decrease_stack(amount)
        pot.increase_pot(amount)
    else:
        raise TypeError('Wrong type(s)')
    
    return None

def bet_move(player, pot, phase=0, nr=2, flop1='none', flop2='none', flop3='none', turn='none', river='none', \
        amount=0, move='bet'):
    '''bet move'''

    if isinstance(player, pplayer.Player) and isinstance(pot, ppot.Pot):
        db_funcs.sql_insert_history(values_list=[phase, nr, player.general_name(), player.position_nr(), player.stack(), \
            pot.show_pot(), flop1, flop2, flop3, turn, river, move, amount, player.stack() - amount, \
            pot.show_pot() + amount])
        player.decrease_stack(amount)
        pot.increase_pot(amount)
    else:
        raise TypeError('Wrong type(s)')
    
    return None

def raise_move(player, pot, phase=0, nr=2, flop1='none', flop2='none', flop3='none', turn='none', river='none', \
        amount=0, move='raise'):
    '''raise move'''

    if isinstance(player, pplayer.Player) and isinstance(pot, ppot.Pot):
        db_funcs.sql_insert_history(values_list=[phase, nr, player.general_name(), player.position_nr(), player.stack(), \
            pot.show_pot(), flop1, flop2, flop3, turn, river, move, amount, player.stack() - amount, \
            pot.show_pot() + amount])
        player.decrease_stack(amount)
        pot.increase_pot(amount)
    else:
        raise TypeError('Wrong type(s)')
    
    return None

def allin_move(player, pot, phase=0, nr=2, flop1='none', flop2='none', flop3='none', turn='none', river='none', \
        amount=0, move='allin'):
    '''allin move'''

    if isinstance(player, pplayer.Player) and isinstance(pot, ppot.Pot):
        db_funcs.sql_insert_history(values_list=[phase, nr, player.general_name(), player.position_nr(), player.stack(), \
            pot.show_pot(), flop1, flop2, flop3, turn, river, move, amount, player.stack() - amount, \
            pot.show_pot() + amount])
        player.decrease_stack(amount)
        pot.increase_pot(amount)
    else:
        raise TypeError('Wrong type(s)')
    
    return None

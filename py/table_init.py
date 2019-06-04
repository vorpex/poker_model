'''table initialization'''

# pylint: disable=E1601, W0612

import card as c
import deck as d
import board as b
import hand as h
import player as pl
import pot as p

def table_init(nr_of_players, starting_chips):
    '''players initialization'''

    POT = p.Pot()

    PLAYERS = []
    for i in range(nr_of_players):

        PLAYERS.append(pl.Player(i, starting_chips))
        PLAYERS[i].add_position(i)

    return POT, PLAYERS

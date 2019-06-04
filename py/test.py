'''poker test'''

# pylint: disable=E1101, E1601

import card as c
import board as b
import deck as d
import hand as h
import player as pl
import pot as p
import table_init as t

table_init = t.table_init(6, 1000)
POT = table_init[0]
PLAYERS = table_init[1]

# game initialization

for i in range(len(PLAYERS)):

    PLAYERS[i].add_position((PLAYERS[i].position_nr + 1) % len(PLAYERS))

deck = d.Deck()

brd = deck.make_board()
BOARD = b.Board(brd[0], brd[1], brd[2], brd[3], brd[4])

hnd = [deck.make_hand() for i in range(len(PLAYERS))]
HAND = [h.Hand(hnd[i][0], hnd[i][1]) for i in range(len(PLAYERS))]
for i in range(len(PLAYERS)):

    PLAYERS[i].add_hand(HAND[i])

player_order = []
for i in range(len(PLAYERS)):

    player_order[PLAYERS[i].position_nr()] = PLAYERS[i]

player_move = [1 for i in range(len(PLAYERS))]

# preflop phase

# player_order[0] action: bet small blind
# player_order[1] action: bet big blind

while sum(player_move) != 0:

    # for i in range(len(player_move)):
    #
    #     if player_move[i] == 1:
    #         check_valid_move_from_db(parameters)
    #         choose_valid_move_from_db(parameters)
    #         do valid move
    #         player_move[i] = 0

    pass

# flop phase

# turn phase

# river phase

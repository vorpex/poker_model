'''poker test'''

# pylint: disable=E1101, E1601, W0612

import sys
sys.path.append('c:\\ProgramData\\Anaconda3\\Lib\\site-packages\\deuces\\')

import pcard
import pboard
import pdeck
import phand
import pplayer
import ppot

import check_moves
import db_funcs
import moves

# parameters

game_id = 1
number_of_players = 6
starting_chips_amount = 1000
small_blind = 10
big_blind = 2 * small_blind

# table initialization

TABLE = db_funcs.table_init(number_of_players, starting_chips_amount)
POT = TABLE[0]
PLAYERS = TABLE[1]

# game initialization

for i in range(len(PLAYERS)):

    PLAYERS[i].add_position((PLAYERS[i].position_nr() + 1) % len(PLAYERS))

DECK = pdeck.Deck()
BOARD = DECK.make_board()

HANDS = [DECK.make_hand() for i in range(len(PLAYERS))]
for i in range(len(PLAYERS)):

    PLAYERS[i].add_hand(HANDS[i])

PLAYER_ORDER = [0 for i in range(len(PLAYERS))]
for i in range(len(PLAYERS)):

    PLAYER_ORDER[PLAYERS[i].position_nr()] = PLAYERS[i]

PLAYER_MOVE_FLAGS = [1 for i in range(len(PLAYERS))]

# preflop phase

db_funcs.create_decision_point(
    PLAYER_ORDER[i], \
    PLAYER_ORDER[i].show_player_hand().show_hand()[0].show_card(), \
    PLAYER_ORDER[i].show_player_hand().show_hand()[1].show_card(), \
    PLAYER_ORDER[i].chips(), \
    PLAYER_ORDER[i].position_nr(), \
    POT.show_pot()
)
moves.small_blind_move(PLAYER_ORDER[0], small_blind, POT)

db_funcs.create_decision_point(
    PLAYER_ORDER[i], \
    PLAYER_ORDER[i].show_player_hand().show_hand()[0].show_card(), \
    PLAYER_ORDER[i].show_player_hand().show_hand()[1].show_card(), \
    PLAYER_ORDER[i].chips(), \
    PLAYER_ORDER[i].position_nr(), \
    POT.show_pot()
)
moves.big_blind_move(PLAYER_ORDER[1], big_blind, POT)

for i in range(2, 6):

    db_funcs.create_decision_point(
    PLAYER_ORDER[i], \
    PLAYER_ORDER[i].show_player_hand().show_hand()[0].show_card(), \
    PLAYER_ORDER[i].show_player_hand().show_hand()[1].show_card(), \
    PLAYER_ORDER[i].chips(), \
    PLAYER_ORDER[i].position_nr(), \
    POT.show_pot()
    )

    if PLAYER_MOVE_FLAGS[i] == 1:
        pmf = db_funcs.check_possible_moves(
                PLAYER_ORDER[i], \
                PLAYER_ORDER[i].show_player_hand().show_hand()[0].show_card(), \
                PLAYER_ORDER[i].show_player_hand().show_hand()[1].show_card(), \
                PLAYER_ORDER[i].chips(), \
                PLAYER_ORDER[i].position_nr(), \
                POT.show_pot()
            )

        if pmf == 0:
            db_funcs.create_possible_moves(
                PLAYER_ORDER[i], \
                PLAYER_ORDER[i].show_player_hand().show_hand()[0].show_card(), \
                PLAYER_ORDER[i].show_player_hand().show_hand()[1].show_card(), \
                PLAYER_ORDER[i].chips(), \
                PLAYER_ORDER[i].position_nr(), \
                POT.show_pot()
            )
        else:
            db_funcs.call_possible_move(
                PLAYER_ORDER[i], \
                PLAYER_MOVE_FLAGS, \
                PLAYER_ORDER[i].chips(), \
                POT.show_pot()
            )
    else:
        pass

while sum(PLAYER_MOVE_FLAGS) != 0: # extend with other conditions

    for i in range(6):

        db_funcs.create_decision_point(
            PLAYER_ORDER[i], \
            PLAYER_ORDER[i].show_player_hand().show_hand()[0].show_card(), \
            PLAYER_ORDER[i].show_player_hand().show_hand()[1].show_card(), \
            PLAYER_ORDER[i].chips(), \
            PLAYER_ORDER[i].position_nr(), \
            POT.show_pot()
        )

        if PLAYER_MOVE_FLAGS[i] == 1:
            pmf = db_funcs.check_possible_moves(
                    PLAYER_ORDER[i], \
                    PLAYER_ORDER[i].show_player_hand().show_hand()[0].show_card(), \
                    PLAYER_ORDER[i].show_player_hand().show_hand()[1].show_card(), \
                    PLAYER_ORDER[i].chips(), \
                    PLAYER_ORDER[i].position_nr(), \
                    POT.show_pot()
                )

            if pmf == 0:
                db_funcs.create_possible_moves(
                    PLAYER_ORDER[i], \
                    PLAYER_ORDER[i].show_player_hand().show_hand()[0].show_card(), \
                    PLAYER_ORDER[i].show_player_hand().show_hand()[1].show_card(), \
                    PLAYER_ORDER[i].chips(), \
                    PLAYER_ORDER[i].position_nr(), \
                    POT.show_pot()
                )
            else:
                db_funcs.call_possible_move(
                    PLAYER_ORDER[i], \
                    PLAYER_MOVE_FLAGS, \
                    PLAYER_ORDER[i].chips(), \
                    POT.show_pot()
                )
        else:
            pass

# flop phase

# turn phase

# river phase

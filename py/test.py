'''poker test'''

# pylint: disable=E1101, E1601, W0612

import db_funcs
import db_moves

import pdeck

# GAME PARAMETERS

number_of_players = 6
starting_stack = 1000
small_blind = 10
big_blind = 2 * small_blind

db_funcs.sql_delete_all(table='games')
db_funcs.sql_delete_all(table='history')
db_funcs.sql_insert_games(values_list=[number_of_players, starting_stack, small_blind, big_blind])

# TABLE INITIALIZATION

TABLE = db_funcs.table_init(nr_of_players=number_of_players, starting_stack=starting_stack)
POT = TABLE[0]
PLAYERS = TABLE[1]

# GAME INITIALIZATION

# # shift the players position by 1
for player in PLAYERS:

    player.add_position((player.position_nr() + 1) % len(PLAYERS))

# # create deck and board
DECK = pdeck.Deck()
BOARD = DECK.make_board()

# # create hands and add them to players
HANDS = [DECK.make_hand() for player in PLAYERS]
for i in range(len(PLAYERS)):

    PLAYERS[i].add_hand(HANDS[i])

# # define players order
PLAYER_ORDER = [0 for player in PLAYERS]
for player in PLAYERS:

    PLAYER_ORDER[player.position_nr()] = player

# # define players move flags
PLAYER_MOVE_FLAGS = [1 for player in PLAYERS]

# PREFLOP PHASE

# # small blind and big blind moves
db_moves.small_blind_move(player=PLAYER_ORDER[0], pot=POT, amount=small_blind)
db_moves.big_blind_move(player=PLAYER_ORDER[1], pot=POT, amount=big_blind)

# # further moves
phase = 0
nr = 2
for i in range(2, 6):

    db_funcs.decision_point(hand=PLAYER_ORDER[i].show_player_hand_db(), stack=PLAYER_ORDER[i].stack(), \
        pot=POT.show_pot(), position=PLAYER_ORDER[i].position_nr(), phase=phase, nr=nr)

# while sum(PLAYER_MOVE_FLAGS) != 0: # extend with other conditions

#     for i in range(6):

#         db_funcs.create_decision_point(
#             PLAYER_ORDER[i], \
#             PLAYER_ORDER[i].show_player_hand().show_hand()[0].show_card(), \
#             PLAYER_ORDER[i].show_player_hand().show_hand()[1].show_card(), \
#             PLAYER_ORDER[i].chips(), \
#             PLAYER_ORDER[i].position_nr(), \
#             POT.show_pot()
#         )

#         if PLAYER_MOVE_FLAGS[i] == 1:
#             pmf = db_funcs.check_possible_moves(
#                     PLAYER_ORDER[i], \
#                     PLAYER_ORDER[i].show_player_hand().show_hand()[0].show_card(), \
#                     PLAYER_ORDER[i].show_player_hand().show_hand()[1].show_card(), \
#                     PLAYER_ORDER[i].chips(), \
#                     PLAYER_ORDER[i].position_nr(), \
#                     POT.show_pot()
#                 )

#             if pmf == 0:
#                 db_funcs.create_possible_moves(
#                     PLAYER_ORDER[i], \
#                     PLAYER_ORDER[i].show_player_hand().show_hand()[0].show_card(), \
#                     PLAYER_ORDER[i].show_player_hand().show_hand()[1].show_card(), \
#                     PLAYER_ORDER[i].chips(), \
#                     PLAYER_ORDER[i].position_nr(), \
#                     POT.show_pot()
#                 )
#             else:
#                 db_funcs.call_possible_move(
#                     PLAYER_ORDER[i], \
#                     PLAYER_MOVE_FLAGS, \
#                     PLAYER_ORDER[i].chips(), \
#                     POT.show_pot()
#                 )
#         else:
#             pass

# # FLOP PHASE

# # TURN PHASE

# # RIVER PHASE

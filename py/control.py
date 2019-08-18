'''poker model control script'''

# pylint: disable=E1101, E1601, W0612

import gc
import mysql.connector

import funcs_db
import funcs_poker

import pdeck

gc.collect()

# OPEN CONNECTION TO POKER DB

poker_db = mysql.connector.connect(user='root', host='127.0.0.1', database='poker')

# GAME PARAMETERS

number_of_players = 6
player0_stack = 1000
player1_stack = 1000
player2_stack = 1000
player3_stack = 1000
player4_stack = 1000
player5_stack = 1000
small_blind = 10
big_blind = 2 * small_blind

funcs_db.sql_delete_all(table='games', poker_db=poker_db)
funcs_db.sql_delete_all(table='history', poker_db=poker_db)
funcs_db.sql_delete_all(table='decision_points', poker_db=poker_db)
funcs_db.sql_delete_all(table='possible_moves', poker_db=poker_db)
funcs_db.sql_insert_games(number_of_players=number_of_players, player0_stack=player0_stack, \
    player1_stack=player1_stack, player2_stack=player2_stack, player3_stack=player3_stack, \
    player4_stack=player4_stack, player5_stack=player5_stack, small_blind=small_blind, big_blind=big_blind, \
    poker_db=poker_db)

# TABLE INITIALIZATION

TABLE = funcs_poker.table_init(nr_of_players=number_of_players, player0_stack=player0_stack, \
    player1_stack=player1_stack, player2_stack=player2_stack, player3_stack=player3_stack, \
    player4_stack=player4_stack, player5_stack=player5_stack)
POT = TABLE[0]
PLAYERS = TABLE[1]

# GAME INITIALIZATION

## shift the players position by 1
for player in PLAYERS:

    player.add_position((player.position_nr() + 1) % len(PLAYERS))

## create deck and board
DECK = pdeck.Deck()
BOARD = DECK.make_board()

## create hands and add them to players
HANDS = [DECK.make_hand() for player in PLAYERS]
for i in range(len(PLAYERS)):

    PLAYERS[i].add_hand(HANDS[i])

## define players order
PLAYER_ORDER = [0 for player in PLAYERS]
for player in PLAYERS:

    PLAYER_ORDER[player.position_nr()] = player

## define players move flags
PLAYER_MOVE_FLAGS = [1 for player in PLAYERS]

# PREFLOP PHASE

## small blind and big blind moves
funcs_poker.move(player=PLAYER_ORDER[0], move='small_blind', pot=POT, amount=small_blind, poker_db=poker_db)
funcs_poker.move(player=PLAYER_ORDER[1], move='big_blind', pot=POT, amount=big_blind, nr=1, poker_db=poker_db)

## further moves
phase = 0
nr = 2
for i in range(2, 6):
    
    move = funcs_db.decision_point(hand=PLAYER_ORDER[i].player_hand_simple(), stack=PLAYER_ORDER[i].stack(), \
        pot=POT.show_pot(), position=PLAYER_ORDER[i].position_nr(), phase=phase, nr=nr, poker_db=poker_db)
    if move in ['fold', 'check']:
        funcs_poker.move(player=PLAYER_ORDER[i], move=move, pot=POT, phase=phase, nr=nr, poker_db=poker_db)
    elif move in ['call', 'raise']:
        amount = 60 # calculation for call_amount
        funcs_poker.move(player=PLAYER_ORDER[i], move='call', pot=POT, phase=phase, nr=nr, amount=amount, poker_db=poker_db)
    else:
        pass
    
    # save move information for every players

    nr = nr + 1

## while sum(PLAYER_MOVE_FLAGS) != 0: # extend with other conditions

# FLOP PHASE

# TURN PHASE

# RIVER PHASE

poker_db.close()

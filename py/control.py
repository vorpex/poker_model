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

funcs_db.sql_delete_all(poker_db=poker_db, table='games')
funcs_db.sql_delete_all(poker_db=poker_db, table='history')
funcs_db.sql_delete_all(poker_db=poker_db, table='decision_points')
funcs_db.sql_delete_all(poker_db=poker_db, table='possible_moves')
funcs_db.sql_insert_games(poker_db=poker_db, number_of_players=number_of_players, player0_stack=player0_stack, \
    player1_stack=player1_stack, player2_stack=player2_stack, player3_stack=player3_stack, \
    player4_stack=player4_stack, player5_stack=player5_stack, small_blind=small_blind, big_blind=big_blind)

# TABLE INITIALIZATION

TABLE = funcs_poker.table_init(number_of_players=number_of_players, player0_stack=player0_stack, \
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
PLAYERS_ORDERED = {player.position_nr(): player for player in PLAYERS}
PLAYERS_ORDERED = dict(sorted(PLAYERS_ORDERED.items()))

## define players move flags
PLAYERS_MOVE_ORDERED = {player.position_nr(): 1 for player in PLAYERS}
PLAYERS_MOVE_ORDERED = dict(sorted(PLAYERS_MOVE_ORDERED.items()))

# PREFLOP PHASE

## small blind and big blind moves
funcs_poker.move(poker_db=poker_db, player=PLAYERS_ORDERED[0], pot=POT, move='small_blind', amount=small_blind)
funcs_poker.move(poker_db=poker_db, player=PLAYERS_ORDERED[1], pot=POT, move='big_blind', nr=1, amount=big_blind)

## further moves
phase = 0
nr = 2
for i in range(2, 6):
    
    move, amount = funcs_db.decision_point(poker_db=poker_db, player_name=PLAYERS_ORDERED[i].general_name(), \
        hand=PLAYERS_ORDERED[i].player_hand_simple(), stack=PLAYERS_ORDERED[i].stack(), pot=POT.show_pot(), \
        position=PLAYERS_ORDERED[i].position_nr(), phase=phase, nr=nr)
    funcs_poker.move(poker_db=poker_db, player=PLAYERS_ORDERED[i], pot=POT, move=move, phase=phase, nr=nr, \
        amount=amount)
    if move == 'fold':
        PLAYERS_MOVE_ORDERED[PLAYERS_ORDERED[i].position_nr()] = 0
    else:
        pass
    
    # save move information for every players

    nr = nr + 1

while sum(PLAYERS_MOVE_ORDERED.values()) > 0:
    
    for i in range(0, 6):

        last_move, action_flag = funcs_db.details_to_move(poker_db=poker_db, phase=phase, position=i)
        if last_move != 'fold' and action_flag > 0:
            move, amount = funcs_db.decision_point(poker_db=poker_db, player_name=PLAYERS_ORDERED[i].general_name(), \
                hand=PLAYERS_ORDERED[i].player_hand_simple(), stack=PLAYERS_ORDERED[i].stack(), pot=POT.show_pot(), \
                position=PLAYERS_ORDERED[i].position_nr(), phase=phase, nr=nr)
            funcs_poker.move(poker_db=poker_db, player=PLAYERS_ORDERED[i], pot=POT, move=move, phase=phase, nr=nr, \
                amount=amount)
            if move == 'fold':
                PLAYERS_MOVE_ORDERED[PLAYERS_ORDERED[i].position_nr()] = 0
            else:
                pass

# FLOP PHASE

# TURN PHASE

# RIVER PHASE

poker_db.close()

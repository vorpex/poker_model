'''poker test'''

# pylint: disable=E1101, E1601

import pcard
import pboard
import pdeck
import phand
import pplayer
import ppot

# parameters

number_of_players = 6
starting_chips_amount = 1000
small_blind_amount = 10
big_blind_amount = 2 * small_blind_amount

# table initialization

def table_init(nr_of_players, starting_chips):
    '''players initialization'''

    pot = ppot.Pot()

    players = []
    for i in range(nr_of_players):

        players.append(pplayer.Player(i, starting_chips))
        players[i].add_position(i)

    return pot, players

TABLE = table_init(number_of_players, starting_chips_amount)
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

PLAYER_MOVE = [1 for i in range(len(PLAYERS))]

# preflop phase

def small_blind(player, small_blind_amount, pot):
    '''small blind move'''
    
    if isinstance(player, pplayer.Player) and isinstance(pot, ppot.Pot):
        player.decrease_chips(small_blind_amount)
        pot.increase_pot(small_blind_amount)
        PLAYER_MOVE[0] = 0
    else:
        raise TypeError('Wrong type(s)')
    
    return None

def big_blind(player, big_blind_amount, pot):
    '''big blind move'''
    
    if isinstance(player, pplayer.Player) and isinstance(pot, ppot.Pot):
        player.decrease_chips(big_blind_amount)
        pot.increase_pot(big_blind_amount)
        PLAYER_MOVE[1] = 0
    else:
        raise TypeError('Wrong type(s)')

    return None

small_blind(PLAYER_ORDER[0], small_blind_amount, POT)
big_blind(PLAYER_ORDER[1], big_blind_amount, POT)

while sum(PLAYER_MOVE) != 0:

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

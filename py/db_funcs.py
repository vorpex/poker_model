'''database functions'''

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
import moves

def table_init(nr_of_players, starting_chips):
    '''players initialization'''

    pot = ppot.Pot()

    players = []
    for i in range(nr_of_players):

        players.append(pplayer.Player(i, starting_chips))
        players[i].add_position(i)

    return pot, players

def create_decision_point(player, card1, card2, chips, pot, position):
    '''create decision point
    
    - Extend with game_id for game history
    - Extend with other players' amount of chips information
    
    Insert descision point into database
    '''

    return None

def check_possible_moves(player, card1, card2, chips, pot, position):
    '''check possible moves
    
    - Extend with game_id for game history
    - Extend with other players' amount of chips information
    
    Select to query data from database. Return 1 if the current decision point is in the database otherwise return 0
    '''
       
    return 1 # or 0

def create_possible_moves(player, card1, card2, chips, pot, position):
    '''create possible moves
    
    - Extend with game_id for game history
    - Extend with other players' amount of chips information
    
    Insert possible moves into database associated with the current decisionpoint
    '''
    
    if check_moves.check_fold_move(player) == 1:
        '''Insert possible move into database associated with the current decisionpoint'''
        pass
    if check_moves.check_check_move(player) == 1:
        '''Insert possible move into database associated with the current decisionpoint'''
        pass
    if check_moves.check_call_move(player) == 1:
        '''Insert possible move into database associated with the current decisionpoint'''
        pass
    if check_moves.check_bet_move(player) == 1:
        '''Insert possible move into database associated with the current decisionpoint'''
        pass
    if check_moves.check_raise_move(player) == 1:
        '''Insert possible move into database associated with the current decisionpoint'''
        pass
    if check_moves.check_allin_move(player) == 1:
        '''Insert possible move into database associated with the current decisionpoint'''
        pass

    return None

def call_possible_move(player, player_move_flags, amount, pot):
    '''call possible move
    
    - Extend with game_id for game history
    - Extend with other players' amount of chips information
    
    Select a possible move from the database associated with the current decision point using the corresponding distribution 
    of all the moves remaining after filtering for the best ones using their expected value
    '''
    
    # define choosen move from database
    choosen_move = '...'

    if choosen_move == 'fold':
        moves.fold_move(player, player_move_flags)
    if choosen_move == 'check':
        moves.check_move(player)
    if choosen_move == 'call':
        moves.call_move(player, amount, pot)
    if choosen_move == 'bet':
        moves.bet_move(player, amount, pot)
    if choosen_move == 'raise':
        moves.raise_move(player, amount, pot)
    if choosen_move == 'allin':
        moves.allin_move(player, pot)
    
    return None

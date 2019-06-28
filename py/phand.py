'''hand class'''

# pylint: disable=E1601

import deuces
import bestfive

class Hand(object):
    '''hand class'''
    
    def __init__(self, card0, card1):
        '''hand initialization
        
        >>> import pcard
        >>> import pdeck
        >>> import phand
        >>>
        >>> card0 = pcard.Card('TS')
        >>> card1 = pcard.Card('8D')
        >>> HAND = phand.Hand(card0, card1)
        >>> 
        >>> DECK = pdeck.Deck()
        >>> HAND = DECK.make_hand()
        '''
        
        self.__card0 = card0
        self.__card1 = card1

    def show_hand(self):
        '''show hand
        
        >>> import pdeck
        >>>
        >>> DECK = pdeck.Deck()
        >>> HAND = DECK.make_hand()
        >>> HAND.show_hand()
        '''

        return self.__card0, self.__card1

    def best_five(self, board):
        '''best 5 out of 7

        >>> import pdeck
        >>>
        >>> DECK = pdeck.Deck()
        >>> BOARD = DECK.make_board()
        >>> HAND = DECK.make_hand()
        >>> HAND.best_five(BOARD)
        '''

        hand_and_board = self.__card0.show_card() + ' ' + self.__card1.show_card() + ' ' + \
        board.flop0().show_card() + ' ' + board.flop1().show_card() + ' ' + board.flop2().show_card() + ' ' + \
        board.turn().show_card() + ' ' + board.river().show_card()

        return bestfive.test_best_hand(hand_and_board)

    def hand_strength(self, board):
        '''hand strength

        >>> import deck
        >>>
        >>> DECK = deck.Deck()
        >>> BOARD = DECK.make_board()
        >>> HAND = DECK.make_hand()
        >>> HAND.hand_strength(BOARD)
        '''

        evaluator = deuces.Evaluator()
        b5 = self.best_five(board)

        h1 = b5[0].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c')
        h2 = b5[1].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c')
        b1 = b5[2].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c')
        b2 = b5[3].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c')
        b3 = b5[4].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c')
        hl = [deuces.Card.new(h1), deuces.Card.new(h2)]
        bl = [deuces.Card.new(b1), deuces.Card.new(b2), deuces.Card.new(b3)]
        strength = evaluator.evaluate(bl, hl)
        
        return strength

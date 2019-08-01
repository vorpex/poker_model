'''board class'''

# pylint: disable=E1101, E1601, W0612

import pcard

class Board(object):
    '''board class'''

    def __init__(self, card0, card1, card2, card3, card4):
        '''board initialization
        
        >>> import pboard
        >>> import pcard
        >>> import pdeck
        >>>
        >>> card0 = pcard.Card('TS')
        >>> card1 = pcard.Card('KS')
        >>> card2 = pcard.Card('8D')
        >>> card3 = pcard.Card('8C')
        >>> card4 = pcard.Card('2H')
        >>> BOARD = pboard.Board(card0, card1, card2, card3, card4)
        >>>
        >>> DECK = pdeck.Deck()
        >>> BOARD = DECK.make_board()
        '''

        if isinstance(card0, pcard.Card) and isinstance(card1, pcard.Card) and isinstance(card2, pcard.Card) and \
        isinstance(card3, pcard.Card) and isinstance(card4, pcard.Card):
            self.__flop0 = card0
            self.__flop1 = card1
            self.__flop2 = card2
            self.__turn = card3
            self.__river = card4
        else:
            raise TypeError('Wrong type')

    def show_board(self):
        '''show board
        
        >>> import pdeck
        >>>
        >>> DECK = pdeck.Deck()
        >>> BOARD = DECK.make_hand()
        >>> BOARD.show()
        '''

        return self.__flop0, self.__flop1, self.__flop2, self.__turn, self.__river

    def flop(self):
        '''show flop
        
        >>> import pdeck
        >>>
        >>> DECK = pdeck.Deck()
        >>> BOARD = DECK.make_hand()
        >>> BOARD.flop()
        '''

        return self.__flop0, self.__flop1, self.__flop2

    def flop0(self):
        '''show flop0
        
        >>> import pdeck
        >>>
        >>> DECK = pdeck.Deck()
        >>> BOARD = DECK.make_hand()
        >>> BOARD.flop0()
        '''

        return self.__flop0

    def flop1(self):
        '''show flop1
        
        >>> import pdeck
        >>>
        >>> DECK = pdeck.Deck()
        >>> BOARD = DECK.make_hand()
        >>> BOARD.flop1()
        '''

        return self.__flop1

    def flop2(self):
        '''show flop2
        
        >>> import pdeck
        >>>
        >>> DECK = pdeck.Deck()
        >>> BOARD = DECK.make_hand()
        >>> BOARD.flop2()
        '''

        return self.__flop2

    def turn(self):
        '''show turn
        
        >>> import pdeck
        >>>
        >>> DECK = pdeck.Deck()
        >>> BOARD = DECK.make_hand()
        >>> BOARD.turn()
        '''

        return self.__turn
    
    def river(self):
        '''show river
        
        >>> import pdeck
        >>>
        >>> DECK = pdeck.Deck()
        >>> BOARD = DECK.make_hand()
        >>> BOARD.river()
        '''

        return self.__river

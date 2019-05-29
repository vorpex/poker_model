'''board class'''

# pylint: disable=E1601

class Board(object):
    '''board class'''

    def __init__(self, card0, card1, card2, card3, card4):
        '''board initialization
        
        >>> card0 = Card('TS')
        >>> card1 = Card('KS')
        >>> card2 = Card('8D')
        >>> card3 = Card('8C')
        >>> card4 = Card('2H')
        >>> board = Board(card0, card1, card2, card3, card4)
        >>>
        >>> deck = Deck()
        >>> b = deck.make_board()
        >>> board = Board(b[0], b[1], b[2], b[3], b[4])        
        '''

        self.__flop0 = card0
        self.__flop1 = card1
        self.__flop2 = card2
        self.__turn = card3
        self.__river = card4

    def show_board(self):
        '''show board
        
        >>> board.show()
        '''

        return self.__flop0, self.__flop1, self.__flop2, self.__turn, self.__river

    def flop(self):
        '''show flop
        
        >>> board.flop()
        '''

        return self.__flop0, self.__flop1, self.__flop2

    def flop0(self):
        '''show flop0
        
        >>> board.flop0()
        '''

        return self.__flop0

    def flop1(self):
        '''show flop1
        
        >>> board.flop1()
        '''

        return self.__flop1

    def flop2(self):
        '''show flop2
        
        >>> board.flop2()
        '''

        return self.__flop2

    def turn(self):
        '''show turn
        
        >>> board.turn()
        '''

        return self.__turn
    
    def river(self):
        '''show river
        
        >>> board.river()
        '''

        return self.__river

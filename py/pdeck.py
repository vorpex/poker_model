'''deck class'''

# pylint: disable=E1101, E1601, W0612

import sys
sys.path.append('c:\\ProgramData\\Anaconda3\\Lib\\site-packages\\deuces\\')

import pboard
import pcard
import phand
import random

class Deck(object):
    '''deck class'''

    colors = ['C', 'D', 'H', 'S']
    figures = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    i = 0
    for color in colors:

        for figure in figures:

            locals()['card%s' % i] = pcard.Card(figure + color)
            i += 1

    def __init__(self):
        '''deck initialization
        
        >>> import pdeck
        >>>
        >>> DECK = pdeck.Deck()
        '''

        self.__deck = []
        for color in self.colors:

            for figure in self.figures:

                self.__deck.append(pcard.Card(figure + color))

    def show_deck(self):
        '''show deck
        
        >>> import pdeck
        >>>
        >>> DECK = pdeck.Deck()
        >>> DECK.show_deck()
        '''
        
        return self.__deck

    def nth_card(self, nth):
        '''show the n-th card from deck
        
        >>> import pdeck
        >>>
        >>> DECK = pdeck.Deck()
        >>> DECK.nth_card(13)
        '''
        
        try:
            return self.__deck[nth]
        except:
            raise AttributeError('Wrong index')
    
    def draw_by_number(self, nr):
        '''pick card from deck by nr
        
        >>> import pdeck
        >>>
        >>> DECK = pdeck.Deck()
        >>> DECK.draw_by_number(13)
        '''
        
        try:
            pick = self.__deck[nr]
            self.__deck.remove(pick)
            return pick
        except:
            raise AttributeError('Wrong index')

    def draw_by_name(self, name):
        '''pick card from deck by name
        
        >>> import pdeck
        >>>
        >>> DECK = pdeck.Deck()
        >>> DECK.draw_by_name('AS')
        '''

        flag = 0
        for crd in self.__deck:
        
            if crd.show_card() == name:
                self.__deck.remove(crd)
                flag = 1
                pick = crd
                break

        if flag == 0:
            raise TypeError('Wrong name')
        else:
            return pick

    def make_board(self):
        '''make a random board
        
        >>> import pdeck
        >>>
        >>> DECK = pdeck.Deck()
        >>> BOARD = DECK.make_board()
        '''
        
        board_cards = []
        for i in range(5):
        
            random_number = random.randint(0, len(self.__deck) - 1)
            board_cards.append(self.draw_by_number(random_number))
        
        brd = pboard.Board(board_cards[0], board_cards[1], board_cards[2], board_cards[3], board_cards[4])

        return brd

    def make_hand(self):
        '''make a random hand
        
        >>> import pdeck
        >>>
        >>> DECK = pdeck.Deck()
        >>> HAND = DECK.make_hand()
        '''
        
        hand_cards = []
        for i in range(2):
        
            random_number = random.randint(0, len(self.__deck) - 1)
            hand_cards.append(self.draw_by_number(random_number))
        
        hnd = phand.Hand(hand_cards[0], hand_cards[1])

        return hnd

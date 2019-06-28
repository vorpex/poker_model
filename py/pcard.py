'''card class'''

# pylint: disable=E1601

class Card(object):
    '''card class'''
    
    def __init__(self, card):
        '''card initialization
        
        >>> import pcard
        >>>
        >>> CARD = pcard.Card('Ts')
        '''

        if card[0].upper() in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'] \
        and card[1].upper() in ['C', 'D', 'H', 'S']:
            self.__figure = card[0].upper()
            self.__color = card[1].upper()
            self.__card = self.__figure + self.__color

            if self.__figure == 'A':
                self.__value = 14
            elif self.__figure == 'K':
                self.__value = 13
            elif self.__figure == 'Q':
                self.__value = 12
            elif self.__figure == 'J':
                self.__value = 11
            elif self.__figure == 'T':
                self.__value = 10
            else:
                self.__value = int(self.__figure)
        else:
            raise TypeError('')

    def show_card(self):
        '''show card
        
        >>> import pcard
        >>>
        >>> CARD = pcard.Card('Ts')
        >>> CARD.show_card()
        '''

        return self.__card

    def figure(self):
        '''show figure
        
        >>> import pcard
        >>>
        >>> CARD = pcard.Card('Ts')
        >>> CARD.figure()
        '''

        return self.__figure

    def color(self):
        '''show color
        
        >>> import pcard
        >>>
        >>> CARD = pcard.Card('Ts')
        >>> CARD.color()
        '''

        return self.__color

    def value(self):
        '''show value
        
        >>> import pcard
        >>>
        >>> CARD = pcard.Card('Ts')
        >>> CARD.value()
        '''

        return self.__value

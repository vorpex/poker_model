'''card class'''

# pylint: disable=E1601

class Card(object):
    '''card class'''
    
    def __init__(self, card):
        '''card initialization
        
        >>> card = Card('Ts')
        '''
       
        self.__figure = card[0]
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

    def show_card(self):
        '''show card
        
        >>> card.show_card()
        '''

        return self.__card

    def figure(self):
        '''show figure
        
        >>> card.figure()
        '''

        return self.__figure

    def color(self):
        '''show color
        
        >>> card.color()
        '''

        return self.__color

    def value(self):
        '''show value
        
        >>> card.value()
        '''

        return self.__value

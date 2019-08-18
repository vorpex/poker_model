'''player class'''

# pylint: disable=E1101, E1601, W0612

import phand

class Player(object):
    '''player class'''

    def __init__(self, nr, stack):
        '''player initialization
        
        >>> import pplayer
        >>>
        >>> PLAYER = pplayer.Player(2, 100)
        '''
        
        self.__number = nr
        self.__general_name = 'player' + str(nr)
        self.__stack = stack
        self.__hand = None
        self.__position_nr = 0
        self.__position_name = 'None'
    
    def number(self):
        '''show player number
        
        >>> import pplayer
        >>>
        >>> PLAYER = pplayer.Player(2, 100)
        >>> PLAYER.number()
        '''

        return self.__number

    def general_name(self):
        '''general name
        
        >>> import pplayer
        >>>
        >>> PLAYER = pplayer.Player(2, 100)
        >>> PLAYER.general_name()
        '''

        return self.__general_name

    def show_player_hand(self):
        '''show hand
        
        >>> import pplayer
        >>>
        >>> PLAYER = pplayer.Player(2, 100)
        >>> PLAYER.show_player_hand()
        '''

        return self.__hand
    
    def player_hand_simple(self):
        '''show hand in db format
        
        >>> import pplayer
        >>>
        >>> PLAYER = pplayer.Player(2, 100)
        >>> PLAYER.show_player_hand_db()
        '''

        try:
            hand = str(self.__hand.show_hand()[0].figure()) + '-' + str(self.__hand.show_hand()[1].figure())
            if self.__hand.show_hand()[0].color() == self.__hand.show_hand()[1].color():
                hand = hand + '-s'
            else:
                hand = hand + '-o'

            return hand
        except:
            return self.__hand

    def add_hand(self, hand):
        '''adding hand to player:
        
        >>> import pdeck
        >>> import pplayer
        >>>
        >>> DECK = pdeck.Deck()
        >>> BOARD = DECK.make_board()
        >>> HAND = DECK.make_hand()
        >>> PLAYER = pplayer.Player(2, 100)
        >>> player.add_hand(HAND)
        '''
        
        if isinstance(hand, phand.Hand):
            self.__hand = hand
        else:
            raise TypeError('Wrong type')

    def stack(self):
        '''show stack
        
        >>> import pplayer
        >>>
        >>> PLAYER = pplayer.Player(2, 100)
        >>> PLAYER.stack()
        '''

        return self.__stack

    def increase_stack(self, won_chips):
        '''winning money
        
        >>> import pplayer
        >>>
        >>> PLAYER = pplayer.Player(2, 100)
        >>> PLAYER.increase_stack(50)
        '''
        
        self.__stack = self.__stack + won_chips

    def decrease_stack(self, lost_chips):
        '''losing money
        
        >>> import pplayer
        >>>
        >>> PLAYER = pplayer.Player(2, 100)
        >>> PLAYER.decrease_stack(50)
        '''

        self.__stack = self.__stack - lost_chips

    def position_nr(self):
        '''show position number
        
        >>> import pplayer
        >>>
        >>> PLAYER = pplayer.Player(2, 100)
        >>> PLAYER.position_nr()
        '''

        return self.__position_nr

    def position_name(self):
        '''show position name
        
        >>> import pplayer
        >>>
        >>> PLAYER = pplayer.Player(2, 100)
        >>> PLAYER.position_name()
        '''

        return self.__position_name

    def add_position(self, position_nr):
        '''adding position
        
        >>> import pplayer
        >>>
        >>> PLAYER = pplayer.Player(2, 100)
        >>> PLAYER.add_position(5)
        '''

        if position_nr >= 0 and position_nr <= 5:
            self.__position_nr = position_nr
            
            if self.__position_nr == 0:
                self.__position_name = 'Small Blind'
            elif self.__position_nr == 1:
                self.__position_name = 'Big Blind'
            elif self.__position_nr == 2:
                self.__position_name = 'Under the Gun'
            elif self.__position_nr == 3:
                self.__position_name = 'Middle'
            elif self.__position_nr == 4:
                self.__position_name = 'Tail'
            else:
                self.__position_name = 'Dealer'
        else:
            raise AttributeError('Position nr is too big or too little')

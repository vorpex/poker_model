'''player class'''

# pylint: disable=E1601

class Player(object):
    '''player class'''

    def __init__(self, nr, chips):
        '''player initialization
        
        >>> player = Player(2, 100)
        '''
        
        self.__number = nr
        self.__general_name = 'player' + str(nr)
        self.__chips = chips
        self.__hand = []
        self.__position_nr = 0
        self.__position_name = 'None'
    
    def number(self):
        '''show player number
        
        >>> player.number()
        '''

        return self.__number

    def general_name(self):
        '''general name
        
        >>> player.general_name()
        '''

        return self.__general_name

    def show_player_hand(self):
        '''show hand
        
        >>> player.show_player_hand()
        '''

        return self.__hand

    def add_hand(self, hand):
        '''adding hand to player:
        
        >>> card0 = Card('TS')
        >>> card1 = Card('8D')
        >>> player.add_hand(Hand(card0, card1))
        '''
        
        self.__hand = hand

    def chips(self):
        '''show chips
        
        >>> player.chips()
        '''

        return self.__chips

    def increase_chips(self, won_chips):
        '''winning money
        
        >>> player.increase_chips(50)
        '''
        
        self.__chips = self.__chips + won_chips

    def decrease_chips(self, lost_chips):
        '''losing money
        
        >>> player.decrease_chips(50)
        '''

        self.__chips = self.__chips - lost_chips

    def position_nr(self):
        '''show position number
        
        >>> player.position_nr()
        '''

        return self.__position_nr

    def position_name(self):
        '''show position name
        
        >>> player.position_name()
        '''

        return self.__position_name

    def add_position(self, position_nr):
        '''adding position
        
        >>> player.add_position(5)
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
            print('Position nr is too big or too little')
            pass

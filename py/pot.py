'''pot class'''

# pylint: disable=E1601

class Pot(object):
    '''pot class'''

    def __init__(self):
        '''pot initialization
        
        >>> pot = Pot()
        '''
        
        self.__pot = 0
    
    def show_pot(self):
        '''show pot
        
        >>> pot.show()
        '''

        return self.__pot

    def increase_pot(self, chips):
        '''increase pot
        
        >>> pot.increase_pot(50)
        '''

        self.__pot = self.__pot + chips
        return self.__pot

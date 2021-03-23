from Pieces import *

class Pawn( Piece ):

    def __init__(self, x : int, y : int, color : str ):
        super().__init__(x, y, color)
        self.ascii_symbol = pieces_dict[self.color]['pawn'] 
        self.name = 'Pawn'
        
    def move(self, x_goal, y_goal, board ):
        print('Olá que tal ') 



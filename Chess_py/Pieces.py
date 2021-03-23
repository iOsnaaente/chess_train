# Pieces in ASCII formact 
pieces_dict = {
            'WHITE' : { 'pawn' : "♙", 'rook' : "♖", 'knight' : "♘", 'bishop' : "♗", 'king' : "♔", 'queen' : "♕" },
            'BLACK' : { 'pawn' : "♟", 'rook' : "♜", 'knight' : "♞", 'bishop' : "♝", 'king' : "♚", 'queen' : "♛" },
            'EMPTY' : { 'empty': " " }
            }

# Class default to create the especifics pieces like pawns and rocks 
class Piece: 

    ascii_symbol = ' '
    color = ''
    value = 0 
    name = ''

    pos = [-1, -1]
    
    def __init__(self, r : int, c : int, color : str ):

        self.pos = [ r, c ]

        self.color = color.upper()
        self.set_value( 0 ) 
        

    # Method to overwrite
    def move(self) -> bool: 
        print('No piece available on here to move...')
    
    # befero to move, verify if the pos_goal is available 
    def pos_available(self, x_goal : int, y_goal : int, board : list):
        print('No piece available on hero to check the available moves...') 

    # return a list with all moviments available to move the piece 
    def moves_available(self, board) -> list :  
        pass 
    

    # After the init_especific_piece was called, set the value 
    def set_value(self, value : int ):
        if self.color == 'WHITE':
            self.value = value *  1

        elif self.color == 'BLACK':
            self.value = value * -1
        
        else:
            self.ascii_symbol = pieces_dict['EMPTY']['empty']
            self.value = 0 




# ♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟ #
# ♙♟                                                       ♙♟ #
# ♙♟                       PAWN                            ♙♟ #
# ♙♟                                                       ♙♟ #
# ♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟ #



class Pawn( Piece ):

    def __init__(self, x : int, y : int, color : str ):
        super().__init__(x, y, color)
        self.ascii_symbol = pieces_dict[self.color]['pawn'] 
        self.name = 'Pawn'
        self.set_value( 1 )
        self.first_move = True 
        
    def move(self, row_goal, collum_goal, board):
        row    = self.pos[0]
        collum = self.pos[1]

        if collum == collum_goal:
            # Mesma coluna OK
            if collum_goal - collum > 1 and not self.first_move:
                # Mesma coluna porem salto muito grande
                return False

        elif collum + 1 == collum_goal and collum + 1 < 8:
            # Esta comendo uma peça na direita
            # Precisa ter uma peça de outra cor na posição  
            pass 

        elif collum - 1 == collum_goal and collum - 1 >= 0:
            # Esta comendo uma peça na esquerda 
            # Precisa ter uma peça de outra cor na posição 
            pass 

        else: 
            # Movimento inválido 
            return False  

        # If the goal position is available, move the pawn to the board goal position 
        board[row_goal][collum_goal], board[self.pos[0]][self.pos[1]] = board[self.pos[0]][self.pos[1]], board[row_goal][collum_goal]
        if self.first_move:
            self.first_move = False 
        return True 



    def pos_available(self, x_goal, y_goal, board):
        return board[x_goal][y_goal] if x_goal >= 0 and x_goal < 8 and y_goal >= 0 and y_goal < 8 else "Posição inválida" 



    def moves_available(self, board):
        r = self.pos[0]
        c = self.pos[1]


       
        



# ♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜ #
# ♖♜                                                       ♖♜ #
# ♖♜                        ROOK                           ♖♜ #
# ♖♜                                                       ♖♜ #
# ♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜ # 

class Rook( Piece ):

    def __init__(self, x : int, y : int, color : str ):
        super().__init__(x, y, color)
        self.ascii_symbol = pieces_dict[self.color]['rook'] 
        self.name = 'Rook'
        
    def move(self, x_goal, y_goal):
        pass 




# ♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞ # 
# ♘♞                                                       ♘♞ #
# ♘♞                      KNIGHT                           ♘♞ #
# ♘♞                                                       ♘♞ #
# ♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞ #

class Knight( Piece ):

    def __init__(self, x : int, y : int, color : str ):
        super().__init__(x, y, color)
        self.ascii_symbol = pieces_dict[self.color]['knight'] 
        self.name = 'Knight'
        
    def move(self, x_goal, y_goal):
        pass 





# ♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝ # 
# ♗♝                                                       ♗♝ #
# ♗♝                      BISHOP                           ♗♝ #
# ♗♝                                                       ♗♝ #
# ♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝ #

class Bishop( Piece ):

    def __init__(self, x : int, y : int, color : str ):
        super().__init__(x, y, color)
        self.ascii_symbol = pieces_dict[self.color]['bishop'] 
        self.name = 'Bishop'
        
    def move(self, x_goal, y_goal):
        pass 







# ♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛ #
# ♕♛                                                   ♕♛ #
# ♕♛                        QUEEN                      ♕♛ #
# ♕♛                                                   ♕♛ #
# ♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛ #
  
class Queen( Piece ):

    def __init__(self, x : int, y : int, color : str ):
        super().__init__(x, y, color)
        self.ascii_symbol = pieces_dict[self.color]['queen'] 
        self.name = 'queen'
        
    def move(self, x_goal, y_goal):
        pass 




# ♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚ #
# ♔♚                                                       ♔♚ #
# ♔♚                      KING                             ♔♚ #
# ♔♚                                                       ♔♚ #
# ♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚ #

class King( Piece ):

    def __init__(self, x : int, y : int, color : str ):
        super().__init__(x, y, color)
        self.ascii_symbol = pieces_dict[self.color]['king'] 
        self.name = 'King'
        
    def move(self, x_goal, y_goal):
        pass 
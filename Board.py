from Spot import Spot
from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from Queen import Queen
from King import King
from Pawn import Pawn
from Piece import Piece


'''
|
|
|
|
 
'''
class Board:
    def __init__(self):
        self.board = []

    def getSpot (self, x, y):
        return self.board[x][y]

    def setBoard (self):
        for row  in range (8):
                self.board.append ([])
                self.board[row] = [None]*8
        # element 0, 0 of the board is A1 on the chess board and
        # element 8,8 of the board is H8 on the chess board
        self.board[0][0] = Spot(Rook("Rook", True), 0, 0)
        self.board[0][1] = Spot(Knight("Knight", True), 0,1)
        self.board[0][2] = Spot(Bishop("Bishop",True),0,2)
        self.board[0][3] = Spot(Queen("Queen", True), 0, 3)
        self.board[0][4] = Spot(King("King", True), 0, 4)
        self.board[0][5] = Spot(Bishop("Bishop", True),0,5)
        self.board[0][6] = Spot(Knight("Knight",True),0,6)
        self.board[0][7] = Spot(Rook("Rook", True),0,7)

        for i in range(8):
            self.board[1][i] = Spot(Pawn("Pawn", True),1,i)
            self.board[6][i] = Spot(Pawn("Pawn", False),6,i)


        for emptyI in range (2,6):
            for j in range (8):
                self.board[emptyI][j] = 0


        self.board[7][0] = Spot(Rook("Rook", False), 7, 0)
        self.board[7][1] = Spot(Knight("Knight", False), 7, 1)
        self.board[7][2] = Spot(Bishop("Bishop", False), 7, 2)
        self.board[7][3] = Spot(Queen("Queen", False), 7, 3)
        self.board[7][4] = Spot(King("King", False), 7, 4)
        self.board[7][5] = Spot(Bishop("Bishop", False), 7, 5)
        self.board[7][6] = Spot(Knight("Knight", False), 7, 6)
        self.board[7][7] = Spot(Rook("Rook", False), 7, 7)




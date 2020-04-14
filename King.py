from Piece import Piece

class King (Piece):

    castled = False
    def canMove(self, board, spot1, spot2):
        xmovement = abs(spot2.x - spot1.x)
        ymovement = abs(spot2.y - spot1.y)
        if xmovement + ymovement == 1:
            return True

        if self.validCastle(board,spot1, spot2, King.isWhite()):
            return True
        return False

    def validCastle (self,board, x1, x2, white):
        if white:
            if spot1.x == 0 and spot1.y == 0:

        else:


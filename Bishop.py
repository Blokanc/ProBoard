from Piece import Piece


class Bishop(Piece):
    def canMove(self, board, spot1, spot2):
        # Checking to see if bishop moved diagonally
        if abs(spot2.x - spot1.x) != abs(spot2.y - spot1.y):
            return False

        if not(spot2.onBoard()):
            return False

        # if the spot is occupied, and if the spot is occupied by a different coloured piece
        if spot2.piece != 0:
            # if non-matchingColours = 1 then the pieces on both spots are not matching
            nonMatchingColours = (not (spot2.getPeice().isWhite()) and spot1.getPeice().isWhite()) or (
                        spot2.getPeice().isWhite() and not (spot1.getPiece().isWhite()))
            if not (nonMatchingColours):
                return False

        # checking to see if bishop has jumped over a piece
        pc1 = spot1.x
        pc2 = spot1.y
        for pc1 in range(abs(spot2.x - spot1.x) + 1):
            if board[pc1][pc2].spot.getPeice() != 0:
                return False
        return True

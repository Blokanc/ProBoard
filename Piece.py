from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, pieceName, isWhite):
        self.pieceName = pieceName
        self.white = isWhite
        self.isKilled = False

    def isWhite(self):
        return self.white

    def isKilled(self):
        return self.isKilled

    def setKiled(self):
        self.isKilled = True

    def onBoard (self, spot):
        if spot.x > 7 or spot.x < 0:
            return False
        if spot.y >7 or spot.y < 0:
            return False
        return True

    # Requires: Non-empty Board and spot objects
    # Promises: Return True if a piece can move from spot1 to spot2 on board, otherwise returns false
    def canMove(self, board, spot1, spot2):
        pass

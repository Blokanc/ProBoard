class Spot:
    def __init__ (self, piece, x, y):
        self.piece = piece
        self.x = x
        self.y = y


    def getPeice (self):
        return self.piece

    def setPeice (self, piece):
        self.piece = piece


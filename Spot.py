class Spot:
    def __init__ (self, piece, row, column):
        self.piece = piece
        self.row = row
        self.column = column


    def getPeice (self):
        return self.piece

    def setPeice (self, piece):
        self.piece = piece


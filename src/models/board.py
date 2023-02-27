from enum import Enum, auto


class Piece(Enum):
    # Represents the value of each chess piece
    pawn = 1
    knight = 3
    bishop = 3
    rook = 5
    queen = 9
    king = 10000


class Colour(Enum):
    white = auto()
    black = auto()

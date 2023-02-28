from enum import Enum, auto


class PieceType(Enum):
    # Represents the value of each chess piece
    pawn = 100
    knight = 320
    bishop = 330
    rook = 500
    queen = 900
    king = 10000


class ColourType(Enum):
    # Represents either white or black
    white = auto()
    black = auto()

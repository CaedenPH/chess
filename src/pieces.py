from enum import Enum


class ColourType(Enum):
    WHITE = 1
    BLACK = 2


class Piece:
    def __init__(self) -> None:
        self.has_moved = False

    def available_moves(self) -> list[tuple[int, int]]:
        return [(4, 4), (5, 4)]  # TODO: Fix


class Pawn(Piece):
    VALUE = 100

    def __init__(self) -> None:
        super().__init__()


class Knight(Piece):
    VALUE = 320

    def __init__(self) -> None:
        super().__init__()


class Bishop(Piece):
    VALUE = 330

    def __init__(self) -> None:
        super().__init__()


class Rook(Piece):
    VALUE = 500

    def __init__(self) -> None:
        super().__init__()


class Queen(Piece):
    VALUE = 900

    def __init__(self) -> None:
        super().__init__()


class King(Piece):
    VALUE = 20000

    def __init__(self) -> None:
        super().__init__()

from enum import Enum


class ColourType(Enum):
    WHITE = 1
    BLACK = 2


class Piece:
    def __init__(self, colour: ColourType, row: int, column: int) -> None:
        self.has_moved = False
        self.row = row
        self.column = column
        self.colour = colour

    def moves(self) -> list[tuple[int, int]]:
        """Return a list of all possible moves for the piece."""
        raise NotImplementedError

    def horizontal_and_verticle_moves(self) -> list[tuple[int, int]]:
        """Return a list of all possible horizontal and vertical moves for the piece."""
        moves = []
        for column in range(8):
            moves.append((self.row, column))

        for row in range(8):
            moves.append((row, self.column))
        return moves

    def diagonal_moves(self) -> list[tuple[int, int]]:
        """Return a list of all possible diagonal moves for the piece."""
        return []

    def available_moves(self) -> list[tuple[int, int]]:
        """
        Return a list of available moves for the piece.

        Filters
        -------
        1) Moves which are outside the board.
        2) Moves which would put the king in check.
        3) Moves that are blocked by other pieces.
        """
        moves = self.moves()
        for move in moves.copy():
            if not (0 <= move[0] <= 7 and 0 <= move[1] <= 7):
                moves.remove(move)
        return moves


class Pawn(Piece):
    VALUE = 100

    def __init__(self, colour: ColourType, row: int, column: int) -> None:
        super().__init__(colour, row, column)

    def moves(self) -> list[tuple[int, int]]:
        one_row_increase = self.row - 1 if self.colour == ColourType.WHITE else self.row + 1
        moves = [(one_row_increase, self.column)]
        if not self.has_moved:
            two_row_increase = self.row - 2 if self.colour == ColourType.WHITE else self.row + 2
            moves.append((two_row_increase, self.column))
        return moves


class Knight(Piece):
    VALUE = 320

    def __init__(self, colour: ColourType, row: int, column: int) -> None:
        super().__init__(colour, row, column)

    def moves(self) -> list[tuple[int, int]]:
        return [
            (self.row + 2, self.column + 1),
            (self.row + 2, self.column - 1),
            (self.row - 2, self.column + 1),
            (self.row - 2, self.column - 1),
            (self.row + 1, self.column + 2),
            (self.row + 1, self.column - 2),
            (self.row - 1, self.column + 2),
            (self.row - 1, self.column - 2),
        ]


class Bishop(Piece):
    VALUE = 330

    def __init__(self, colour: ColourType, row: int, column: int) -> None:
        super().__init__(colour, row, column)

    def moves(self) -> list[tuple[int, int]]:
        return self.diagonal_moves()


class Rook(Piece):
    VALUE = 500

    def __init__(self, colour: ColourType, row: int, column: int) -> None:
        super().__init__(colour, row, column)

    def moves(self) -> list[tuple[int, int]]:
        return self.horizontal_and_verticle_moves()


class Queen(Piece):
    VALUE = 900

    def __init__(self, colour: ColourType, row: int, column: int) -> None:
        super().__init__(colour, row, column)

    def moves(self) -> list[tuple[int, int]]:
        return self.horizontal_and_verticle_moves() + self.diagonal_moves()


class King(Piece):
    VALUE = 20000

    def __init__(self, colour: ColourType, row: int, column: int) -> None:
        super().__init__(colour, row, column)

    def moves(self) -> list[tuple[int, int]]:
        return [
            (self.row + i, self.column + j)
            for i in (-1, 0, +1)
            for j in (-1, 0, +1)
            if (i, j) != (0, 0)
        ]

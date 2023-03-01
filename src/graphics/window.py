from tkinter import Canvas, Frame, PhotoImage, Tk
from typing import Any, TypedDict, Union

from pieces import Bishop, ColourType, King, Knight, Pawn, Queen, Rook

# fmt: off
__all__ = [
    'SquareData',
    'Square',
    'Window'
]
# fmt: on


class SquareData(TypedDict):
    colour: ColourType | None
    piece: Union[Rook, Knight, Bishop, Queen, King, Pawn] | None
    image: PhotoImage | None
    row: int
    column: int


class Square(Canvas):
    """
    Represents a canvas which can be used to display a piece on the board.
    """

    def __init__(self, *args, row: int, column: int, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid(row=row, column=column)
        self.data: SquareData = {
            "row": row,
            "column": column,
            "colour": None,
            "piece": None,
            "image": None,
        }

    def set_piece(
        self,
        colour: ColourType | None,
        piece: Union[Rook, Knight, Bishop, Queen, King, Pawn] | None,
    ) -> None:
        """
        Add a piece to the board at the given row and column.

        :param colour: The colour of the piece to add.
        :param piece: The type of piece to add.
        """
        self.delete("all")

        if colour is not None and piece is not None:
            image = PhotoImage(file=f"assets/{colour.name}_{piece.__class__.__name__}.png")
            self.create_image(40, 40, image=image)

            self.data["image"] = image  # Stop image being garbage collected
        self.data.update({"colour": colour, "piece": piece})


class Window(Tk):
    """
    Represents the window object which will be used to display the game
    board.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.title("Chess")
        self.geometry("663x648")

        self.squares: list[list[Square]] = [[] for _ in range(8)]

        self.setup_board()

    def setup_board(self) -> None:
        """
        Create alternating black and white squares for pieces to be placed on.
        Then place pieces according to the starting position.
        """
        for row in range(8):
            for column in range(8):
                colour = "white" if (row + column) % 2 == 0 else "grey"

                square = Square(self, row=row, column=column, width=77, height=77, bg=colour)  # type: ignore
                self.squares[row].append(square)

        for colour in ColourType:
            row = 7 if colour is ColourType.WHITE else 0

            for column, piece in enumerate(
                (Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)
            ):
                self.squares[row][column].set_piece(colour, piece())

            row = 6 if colour is ColourType.WHITE else 1
            for column in range(8):
                self.squares[row][column].set_piece(colour, Pawn())

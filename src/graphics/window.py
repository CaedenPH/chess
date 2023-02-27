from tkinter import Canvas, Event, Frame, PhotoImage, Tk

# fmt: off
__all__ = [
    'Window'
]
# fmt: on


class Window(Tk):
    """
    Represents the window object which will be used to display the game
    board.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Chess")
        self.geometry("663x648")

        self.frame = Frame(self)
        self.frame.pack()

        self.squares = [[] for _ in range(8)]

        self.bind("<ButtonPress-1>", self.on_click)

        self.setup_board()

    def add_piece(
        self,
        colour: str,
        piece: str,
        row: int,
        column: int,
    ) -> None:
        """
        Add a piece to the board at the given row and column.
        """
        image = PhotoImage(file=f"assets/{colour}_{piece}.png")
        self.squares[row][column].create_image(40, 40, image=image)

        # Prevent the image from being garbage collected
        self.squares[row][column].image = image  # type: ignore

    def setup_board(self) -> None:
        """
        Create alternating black and white squares for pieces to be placed on.
        Then place pieces according to the starting position.
        """
        for row in range(8):
            for column in range(8):
                colour = "white" if (row + column) % 2 == 0 else "blue"

                square = Canvas(self.frame, width=77, height=77, bg=colour)  # type: ignore
                square.grid(row=row, column=column)
                self.squares[row].append(square)

        for colour in ("white", "black"):
            row = 7 if colour == "white" else 0

            for column, piece in enumerate(("rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook")):
                self.add_piece(colour, piece, row, column)

            row = 6 if colour == "white" else 1
            for column in range(8):
                self.add_piece(colour, "pawn", row, column)

    def on_click(self, event: Event) -> None:
        # x, y = event.widget.winfo_pointerxy()
        # target = event.widget.winfo_containing(x, y)
        pass

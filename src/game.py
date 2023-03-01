from __future__ import annotations

from tkinter import Event
from typing import Literal

from requests import delete

from graphics import Square, Window

# fmt: off
__all__ = (
    'Game'
)
# fmt: on


class Game:
    """
    Represents the game object which will be used to hold information
    including the current game status, the current current board status
    and other useful information about the game.
    """

    def __init__(self) -> None:
        self.window = Window()
        self.window.bind("<ButtonPress-1>", self.on_click)

        self.clicked_square: Literal[False] | Square = False

    def play(self) -> None:
        self.window.mainloop()

    def move_piece(self, target: Square) -> None:
        """
        Move a piece from one square to another.
        """
        for row in self.window.squares:
            for square in row:
                square.delete("oval")

        if (square := self.clicked_square) is not False:
            data = square.data
            if (target.data["row"], target.data["column"]) in data["piece"].available_moves():
                target.set_piece(data["colour"], data["piece"])
                square.set_piece(None, None)

        self.clicked_square = False

    def on_click(self, event: Event) -> None:
        """
        Handle a click event on the board.

        :param event: The event object.
        """

        x, y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x, y)
        if not isinstance(target, Square):
            return

        if self.clicked_square is not False:
            self.move_piece(target)
        elif target.data["piece"] is not None:
            self.clicked_square = target

            for available_square in target.data["piece"].available_moves():
                square = self.window.squares[available_square[0]][available_square[1]]
                square.create_oval(25, 25, 55, 55, fill="grey", tags="oval")

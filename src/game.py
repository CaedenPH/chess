from __future__ import annotations

from graphics import Window

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

    def play(self) -> None:
        self.window.mainloop()

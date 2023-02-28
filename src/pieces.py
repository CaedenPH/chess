from models.board import PieceType


class Piece:
    def __init__(self, x: int, y: int, type: PieceType) -> None:
        self.x = x
        self.y = y
        self.type = type
    
        

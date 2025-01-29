from typing import List, Optional

class Game:
    def __init__(self, game_id: str):
        self.game_id = game_id
        self.players: List[str] = []
        self.board: List[Optional[str]] = [None] * 9
        self.turn: Optional[str] = None
        self.winner: Optional[str] = None

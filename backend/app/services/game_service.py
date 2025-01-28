import random
from app.models.game import Game

class GameService:
    def __init__(self):
        self.games = {}  # Almacén de partidas {game_id: Game}

    def create_game(self) -> str:
        game_id = self._generate_game_id()
        self.games[game_id] = Game(game_id)
        return game_id

    def join_game(self, game_id: str) -> str:
        if game_id not in self.games:
            raise ValueError("La partida no existe.")
        game = self.games[game_id]
        if len(game.players) >= 2:
            raise ValueError("La partida ya está completa.")
        player_symbol = "X" if len(game.players) == 0 else "O"
        game.players.append(player_symbol)
        return player_symbol

    def _generate_game_id(self) -> str:
        return random.choice("ABCDEFGH") + str(random.randint(1000, 9999))

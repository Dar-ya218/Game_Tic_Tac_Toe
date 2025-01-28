from fastapi import APIRouter, HTTPException
from app.services.game_service import GameService

router = APIRouter()

# Instancia del servicio de juego
game_service = GameService()

@router.post("/create-game")
async def create_game():
    game_id = game_service.create_game()
    return {"gameId": game_id}

@router.post("/join-game")
async def join_game(game_id: str):
    try:
        player_symbol = game_service.join_game(game_id)
        return {"playerSymbol": player_symbol}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

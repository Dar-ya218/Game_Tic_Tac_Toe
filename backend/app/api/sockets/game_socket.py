from fastapi.websockets import WebSocket, WebSocketDisconnect

class SocketManager:
    def __init__(self):
        self.active_connections = {}

    async def connect(self, websocket: WebSocket, game_id: str):
        await websocket.accept()
        if game_id not in self.active_connections:
            self.active_connections[game_id] = []
        self.active_connections[game_id].append(websocket)

    def disconnect(self, websocket: WebSocket, game_id: str):
        self.active_connections[game_id].remove(websocket)

    async def broadcast(self, game_id: str, message: dict):
        for websocket in self.active_connections.get(game_id, []):
            await websocket.send_json(message)

socket_manager = SocketManager()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.sockets.game_socket import socket_manager

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar a dominios específicos en producción
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas HTTP
app.include_router(api_router)

# WebSockets
@app.on_event("startup")
async def startup_event():
    socket_manager.initialize()

@app.on_event("shutdown")
async def shutdown_event():
    socket_manager.shutdown()

# Punto de entrada
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

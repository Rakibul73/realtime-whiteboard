from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from redis import Redis
from .redis_handler import RedisHandler
from .session_manager import SessionManager
import threading
import asyncio

app = FastAPI()

redis_handler = RedisHandler(Redis(host='localhost', port=6379, db=0))
session_manager = SessionManager()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Collaborative Whiteboard"}

async def handle_message(session_id: str, data: str):
    """Process the incoming message in a separate thread."""
    redis_handler.set(f"drawing_{session_id}", data)
    await session_manager.broadcast(session_id, data)

@app.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await websocket.accept()
    session_manager.add_user_to_session(session_id, websocket)

    # Send the current drawing state to the newly connected user
    current_state = redis_handler.get(f"drawing_{session_id}")
    if current_state:
        await websocket.send_text(current_state)

    try:
        while True:
            data = await websocket.receive_text()
            # Use asyncio to run the coroutine in the event loop
            asyncio.run_coroutine_threadsafe(handle_message(session_id, data), asyncio.get_event_loop())
    except WebSocketDisconnect:
        session_manager.remove_user_from_session(session_id, websocket)
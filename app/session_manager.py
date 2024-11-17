from typing import List
from fastapi import WebSocket
from .redis_handler import RedisHandler

class SessionManager:
    def __init__(self, redis_handler: RedisHandler):
        self.redis_handler = redis_handler
        self.sessions = {}

    def add_user_to_session(self, session_id: str, websocket: WebSocket):
        if session_id not in self.sessions:
            self.sessions[session_id] = []
        self.sessions[session_id].append(websocket)

    def remove_user_from_session(self, session_id: str, websocket: WebSocket):
        if session_id in self.sessions:
            self.sessions[session_id].remove(websocket)

    async def broadcast(self, session_id: str, data: str):
        if session_id in self.sessions:
            for user in self.sessions[session_id]:
                await user.send_text(data)
        # Publish to Redis for synchronization across servers
        self.redis_handler.publish(session_id, {"data": data})


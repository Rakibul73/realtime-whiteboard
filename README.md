# Collaborative Whiteboard Backend (FastAPI)

This is the **backend service** for the Collaborative Whiteboard Application, built using **FastAPI**, **Redis**, and **MongoDB**. It provides real-time WebSocket communication, session management, and data persistence for the collaborative drawing experience.

> **Frontend Repository**: [https://github.com/Rakibul73/whiteboard-app](https://github.com/Rakibul73/whiteboard-app) - Next.js/React whiteboard interface

## Current Features

### ✅ Implemented Features
- **Real-time WebSocket Communication**: WebSocket endpoint at `/ws/{session_id}` for live collaboration
- **Session Management**: Multiple users can join the same drawing session using unique session IDs
- **Redis Integration**: Fast temporary storage for session drawing data and real-time synchronization
- **MongoDB Integration**: Persistent storage setup for saving session data (basic implementation)
- **Broadcasting System**: Real-time message broadcasting to all users within a session
- **Session State Recovery**: New users automatically receive current drawing state when joining
- **CORS Support**: Configured for cross-origin requests from frontend

### 🔄 In Development
- Full MongoDB persistence implementation
- User authentication system
- Session history and replay features
- Drawing tools and styles support

## Architecture

### Tech Stack
- **FastAPI**: Modern Python web framework with automatic API documentation
- **WebSockets**: Real-time bidirectional communication
- **Redis**: In-memory data store for session management and message broadcasting
- **MongoDB**: NoSQL database for persistent data storage
- **Uvicorn**: ASGI server for running the FastAPI application

### API Endpoints
- `GET /`: Welcome message and health check
- `WebSocket /ws/{session_id}`: Real-time drawing collaboration endpoint

### File Structure
```
app/
├── main.py              # FastAPI application and WebSocket endpoints
├── redis_handler.py     # Redis operations and connection management
├── session_manager.py   # User session management and broadcasting
└── db.py               # MongoDB connection and data persistence
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- Redis server
- MongoDB server (optional, for persistence)

### Setup Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rakibul73/realtime-whiteboard.git
   cd realtime-whiteboard
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Redis server:**
   ```bash
   # On Windows with Redis installed
   redis-server
   
   # On Linux/Mac
   sudo systemctl start redis
   # or
   brew services start redis
   ```

5. **Configure MongoDB (Optional):**
   - Update the MongoDB connection string in `app/db.py`
   - Default uses MongoDB Atlas connection

6. **Start the FastAPI server:**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

## Usage

### With Frontend Application
1. Start this backend server (port 8000)
2. Clone and start the frontend application: [https://github.com/Rakibul73/whiteboard-app](https://github.com/Rakibul73/whiteboard-app) (port 3000)
3. Access the application at `http://localhost:3000`

### Direct WebSocket Connection
Connect to `ws://localhost:8000/ws/{session_id}` where `session_id` is any unique string.

### API Documentation
Visit `http://localhost:8000/docs` for interactive API documentation (Swagger UI).

## WebSocket Message Format

### Incoming Messages (from client):
```json
{
  "type": "draw",
  "path": [
    {"x": 100, "y": 150, "isDrawing": true},
    {"x": 101, "y": 151, "isDrawing": true}
  ]
}
```

### Outgoing Messages (to clients):
- Initial state: Current drawing data for new connections
- Real-time updates: Drawing events broadcast to all session participants

## Development

### Running Tests
```bash
# Add test commands here when tests are implemented
pytest
```

### Code Structure
- **main.py**: Application entry point, WebSocket handling
- **session_manager.py**: Manages user connections and message broadcasting
- **redis_handler.py**: Redis operations for temporary data storage
- **db.py**: MongoDB integration for persistent storage

## Related Projects

- **Frontend**: [whiteboard-app](https://github.com/Rakibul73/whiteboard-app) - Next.js/React whiteboard interface
- **Full Stack**: This backend + frontend creates a complete collaborative drawing platform

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
# Collaborative Whiteboard Application

The Collaborative Whiteboard Application is a real-time web application built using FastAPI, Redis, and MongoDB. It allows multiple users to connect to a shared whiteboard where they can draw and share their drawings in real-time. This application is designed to facilitate collaborative work and brainstorming sessions.


## Features

- **Real-time Collaboration**: Users can connect to a session and see updates from other users in real-time.

- **WebSocket Support**: Utilizes WebSocket for efficient two-way communication between the server and clients.

- **Persistent Session Management**: Session data is stored in MongoDB, ensuring that user drawings are saved and can be retrieved later.

- **Redis for Pub/Sub**: Redis is used for broadcasting messages across different instances of the application, ensuring synchronization in a distributed environment.


## Architecture

### Components

1. **FastAPI**: The web framework that serves the application and handles HTTP requests and WebSocket connections.


2. **Redis**: A key-value store used for message broadcasting and session management.

3. **MongoDB**: A NoSQL database used to persist session data.


### File Structure

- `app/main.py`: The main entry point of the application, defining the FastAPI app and WebSocket endpoints.

- `app/redis_handler.py`: Contains the `RedisHandler` class for managing Redis connections and operations.

- `app/session_manager.py`: Manages user sessions and broadcasting messages to connected clients.

- `app/db.py`: Handles interactions with MongoDB for saving session data.


- `requirements.txt`: Lists the dependencies required to run the application.


## Installation

To set up the application, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```


2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```


3. Ensure that Redis and MongoDB are running on your local machine or configure the connection settings accordingly.


4. Start the application:
   ```bash
      uvicorn app.main:app --reload
   ```



## Usage


- Open your web browser and navigate to `http://localhost:8000`.

- Connect to a session by using the WebSocket endpoint at `ws://localhost:8000/ws/{session_id}`.

- Start drawing and collaborate with other users in real-time.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.



## License

This project is licensed under the MIT License. See the LICENSE file for more details.
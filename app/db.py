from pymongo import MongoClient
import threading
import time

class MongoDBHandler:
    def __init__(self, uri: str):
        self.client = MongoClient(uri)
        self.db = self.client.whiteboard
        self.sessions = self.db.sessions

    def save_session_data(self, session_id: str, data: dict):
        """Save session data to MongoDB."""
        self.sessions.update_one(
            {"session_id": session_id},
            {"$push": {"data": data}},
            upsert=True
        )

    def periodic_save(self):
        """Save data periodically in the background."""
        while True:
            # This could be adjusted to save data at a certain interval
            # For example, saving every 10 seconds
            for session_id, data in self.sessions.items():
                self.save_session_data(session_id, data)
            time.sleep(10)  # Wait for 10 seconds before saving again

# Start the periodic save process in the background
db_handler = MongoDBHandler("mongodb+srv://rakib:rakib@rakib.7rgkzty.mongodb.net/new_project_3?retryWrites=true&w=majority")
threading.Thread(target=db_handler.periodic_save, daemon=True).start()

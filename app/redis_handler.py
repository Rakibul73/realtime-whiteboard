import redis
import json

class RedisHandler:
    def __init__(self, redis_client: redis.Redis):
        self.redis_client = redis_client

    def publish(self, channel: str, message: dict):
        """Publish a message to the Redis channel."""
        self.redis_client.publish(channel, json.dumps(message))

    def subscribe(self, channel: str):
        """Subscribe to a Redis channel."""
        pubsub = self.redis_client.pubsub()
        pubsub.subscribe(channel)
        return pubsub

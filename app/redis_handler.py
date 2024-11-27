import redis
import json

class RedisHandler:
    def __init__(self, redis_client: redis.Redis):
        self.redis_client = redis_client
    
    def get(self, key: str) -> str:
        value = self.redis_client.get(key)
        if value:
            return value.decode('utf-8')
        return None


    def set(self, key: str, value: str):
        self.redis_client.set(key, value)

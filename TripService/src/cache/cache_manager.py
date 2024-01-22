import redis

class CacheManager:
    def __init__(self):
        self.cache = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        return self.cache.set(key, value)

    def delete(self, key):
        return self.cache.delete(key)

    def flush(self):
        return self.cache.flushdb()

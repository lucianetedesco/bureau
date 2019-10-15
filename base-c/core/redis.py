import pickle

import singletons
from redis import Redis

from core import config


@singletons.GlobalFactory
class RedisClient:

    def __init__(self):
        self.redis = Redis(host=config.REDIS, port=config.REDIS_PORT, password=config.REDIS_PASS)

    def get(self, key):
        cache = self.redis.get(key)
        if cache:
            return pickle.loads(cache)

    def set(self, key, value):
        self.redis.set(key, pickle.dumps(value))

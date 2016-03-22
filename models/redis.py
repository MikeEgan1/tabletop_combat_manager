import redis
from tabletop_combat_manager.config import RedisConfig

class Service(object):
    def __init__(self, db):
        self.service = redis.Redis(host=RedisConfig.host, port=RedisConfig.port, db=db)

    def set(self, key, json):
        self.service.setex(key, json, RedisConfig.expire)

    def get(self, key):
        self.service.get(key)

from redis import Redis

class Service(object):
    def __init__(self, db):
        self.service = redis.Redis(host='localhost', port=6379, db=db)

    def set(self, key, json):
        self.service.setex(key, json, 86400)

    def get(self, key):
        self.service.get(key)

from tabletopmbat_manager.models.redis import Redis

class Model(object):
    def __init__(self):
        self.redis = Redis()

    def get(self, game_id):
        return self.redis.get(game_id)


from tabletop_combat_manager.models.redis import Service


class Model(object):
    def __init__(self):
        self.redis = Service()

    def get(self, game_id):
        return self.redis.get(game_id)


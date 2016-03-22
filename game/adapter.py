from tabletop_combat_manager.game.builder import Builder

class Adapter(object):
    def __init__(self):
        self.builder = Builder()

    def adapt(self, game_json):
        self.builder.setGameId(game_json['game_id'])
        return self.builder.build()




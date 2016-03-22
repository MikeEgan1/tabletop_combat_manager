from tabletop_combat_manager.models.game import Model
from tabletop_combat_manager.game.adapter import Adapter

class Creator(object):
    def __init__(self):
        self.game_model = Model()
        self.adapter = Adapter()

    def get(self, game_id):
        game_json_data = self.game_model.get()
        return self.adapter.adapt(game_json_data)

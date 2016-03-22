from tabletop_game_manager.models.game import Model

class Creator(object):
    def __init__(self):
        self.game_model = Model()

    def get(self, game_id):
        game_json_data = self.game_model.get()

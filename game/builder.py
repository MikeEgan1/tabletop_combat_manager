from tabletop_combat_manager.game.game import Game

class Builder(object):
    def __init__(self):
        pass

    def setGameId(self, game_id):
        self.game_id = game_id


    def build(self):
        return Game(game_id)
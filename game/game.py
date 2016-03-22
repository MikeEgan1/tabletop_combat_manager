from tabletop_combat_manager.utils import create_hash

class Game(object):
    def __init__(self, game_id=create_hash()):
        self.game_id = game_id
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def json(self):
        return self.__dict__
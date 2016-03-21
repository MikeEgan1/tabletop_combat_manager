import random
import json
from tabletop_combat_manager.utils import create_hash

class Game(object):
    def __init__(self, game_id=create_hash()):
        self.game_id = game_id

    def json(self):
        return self.__dict__
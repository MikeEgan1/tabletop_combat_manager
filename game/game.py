import random
import json
from tabletop_combat_manager.utils import create_hash

class Game(object):
    def __init__(self):
        self.game_id = create_hash()

    def json(self):
        return self.__dict__
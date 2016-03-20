import random
import json

class Game(object):
    def __init__(self):
        self.game_id = ''.join(random.choice('0123456789ABCDEF') for i in xrange(16))

    def json(self):
        return self.__dict__
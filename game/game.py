import random

class Game(object):
    def __init__(self):
        self.game_id = ''.join(random.choice('0123456789ABCDEF') for i in xrange(16))
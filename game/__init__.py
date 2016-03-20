import random

def create_new_game():
    game_id = create_game_id()

    return game_id


def create_game_id():
    return ''.join(random.choice('0123456789ABCDEF') for i in xrange(16))
import random

def create_hash():
    return ''.join(random.choice('0123456789ABCDEF') for i in xrange(16))
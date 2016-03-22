from tabletop_combat_manager.creature.creature import Creature

class Player(Creature):
    def __init__(self, name):
        super(Player, self).__init(*args, **kwargs)
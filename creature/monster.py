from tabletop_combat_manager.creature.creature import Creature

class Monster(Creature):
    def __init__(self, name, initiative):
        super(Monster, self).__init(*args, **kwargs)
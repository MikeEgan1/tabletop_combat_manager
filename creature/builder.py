from tabletop_combat_manager.monster.monster import Monster
from tabletop_combat_manager.player.player import Player
from tabletop_combat_manager.exceptions import TypeCreatureTypeNotSetException

class Builder(object):
    def __init__(self):
        self.type = None

    def setName(self, name):
        self.name = name
        return self

    def setInitiative(self, initiative):
        self.initiative = initiative

    def build(self):
        if self.type == "player":
            creature = Player(self.name, self.initiative)
        elif self.type == "monster":
            creature = Monster(self.name, self.initiative)
        else:
            raise TypeCreatureTypeNotSetException("Creature type not valid")




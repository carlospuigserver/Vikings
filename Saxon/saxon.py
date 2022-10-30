from Soldado import soldier
class Saxon(soldier):
    def __init__(self,health,strenght):
        self.health=health
        self.strenght=strenght

def attack(self):
    return self.strenght

def damage(self,damage):
    self.health=self.health-damage
    self.health=self.health-damage
    if(self.health>0):
            return f'A Saxon has received {damage} points of damage'
    else:
            return f'A Saxon has died in combat'

from random import choice

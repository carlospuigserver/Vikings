from Soldado import soldier
class Viking(soldier):
    def __init__(self,health,strenght,name):
        self.health=health
        self.strenght=strenght
        self.name=name

def attack(self):
    return self.strenght

def damage(self,damage):
    self.health=self.health-damage
    if(self.health>0):
            return f'{self.name} has received {damage} points of damage'
    else:
            return f'{self.name} has died in act of combat'

def battleCry(self):
        return 'Odin Owns You All!'


    
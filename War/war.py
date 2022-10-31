from random import choice
from Vikingo import vikingo
from Saxon import saxon
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, viking:vikingo):
        self.vikingArmy.append(viking)
        return None

    def addSaxon(self, saxon:saxon):
        self.saxonArmy.append(saxon)
        return None
    
    def vikingAttack(self):
        saxon = choice(self.saxonArmy)
        viking = choice(self.vikingArmy)
        ataque = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        else:
            pass
        return ataque

    def saxonAttack(self):
        viking = choice(self.vikingArmy)
        saxon = choice(self.saxonArmy)
        ataque = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        else:
            pass
        return ataque
    
    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"  
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."    
        else:
            return "Vikings and Saxons are still in the thick of battle."
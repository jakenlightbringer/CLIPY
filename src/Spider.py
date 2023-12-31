from Enemy import Enemy
from ability import Ability


class Spider(Enemy):
    DEFAULT_HEALTH = 70
    BASE_ATTACK = 12
    BASE_DEFENSE = 15
    BASE_SPELLPOINTS = 3
    BASE_MAX_DAMAGE = 18


    def __init__(self):
        super().__init__("Spider", self.DEFAULT_HEALTH, self.BASE_ATTACK, self.BASE_MAX_DAMAGE, self.BASE_DEFENSE, self.BASE_SPELLPOINTS)            

        self.venom = Ability("Venom", spCost=1, spellEffect=5)
        self.viperSting = Ability("Viper Sting", 2, spellEffect=8)
    
    # dump what's inside object called from Enemy.py
    def __str__(self) -> str:
        return super().__str__()






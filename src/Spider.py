from Enemy import Enemy
from ability import Ability


class Spider(Enemy):
    defaultHeath = 70
    BASE_DAMAGE = 12
    BASE_DEFENSE = 15
    BASE_SP = 3
    BASE_MAX_DAMAGE = 18

    def __init__(self):
        super().__init__("Spider", self.BASE_SP, self.BASE_DEFENSE, self.defaultHeath, self.BASE_DAMAGE, self.BASE_MAX_DAMAGE)

        self.venom = Ability("Venom", spCost=1, spellEffect=5)
        self.viperSting = Ability("Viper Sting", 2, spellEffect=8)
    
    # dump what's inside object called from Enemy.py
    def __str__(self) -> str:
        return super().__str__()


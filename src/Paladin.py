from player import Player
import random

class PaladinClass(Player):
    defaultHeath = 120
    BASE_ATTACK = 20
    BASE_DEFENSE = 25 #will be percent
    BASE_SP = 3
    BASE_MAX_DAMAGE = 28


    
    def __init__(self):
        super().__init__("Paladin", self.defaultHeath, self.BASE_ATTACK, self.BASE_MAX_DAMAGE, self.BASE_DEFENSE, self.BASE_SP)
    
    def playerAttack(self):
        playerAttackValue = random.randrange(self.BASE_ATTACK, self.BASE_MAX_DAMAGE)
        return playerAttackValue



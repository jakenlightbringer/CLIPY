from player import Player
import random

class PaladinClass(Player):
    DEFAULT_HEALTH = 120
    BASE_ATTACK = 20
    BASE_DEFENSE = 25 #will be percent
    BASE_SPELLPOINTS = 3
    BASE_MAX_DAMAGE = 28
    
    def __init__(self):
        super().__init__("Paladin", self.DEFAULT_HEALTH, self.BASE_ATTACK, self.BASE_MAX_DAMAGE, self.BASE_DEFENSE, self.BASE_SPELLPOINTS)
    
    def playerAttack(self):
        playerAttackValue = random.randrange(self.BASE_ATTACK, self.BASE_MAX_DAMAGE)
        return playerAttackValue
    
    '''
    def getPlayerAbilities(playerClass):
            divineJustice = Player.PlayerAbilities("Divine Justice", 2, 40)
            holySalvation = Player.PlayerAbilities("Holy Salvation", 1, 30)
            lightsArmor = Player.PlayerAbilities("Light's Armor", 1, 8)
            return divineJustice, holySalvation, lightsArmor
    '''



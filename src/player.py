import random
from basecharacter import BaseCharacter

class Player(BaseCharacter):
    currentHealth = 0
    
    def __init__(self, baseClass, BASE_HITPOINTS, BASE_ATTACK, BASE_MAX_DAMAGE, BASE_DEFENSE, BASE_SP):
        self.name = baseClass
        self.BASE_HITPOINTS = BASE_HITPOINTS
        self.currentHealth = BASE_HITPOINTS
        self.BASE_ATTACK = BASE_ATTACK
        self.BASE_DEFENSE = BASE_DEFENSE
        self.BASE_SP = BASE_SP
        self.BASE_MAX_DAMAGE = BASE_MAX_DAMAGE


    def playerAttack(self):
        playerAttackValue = random.randrange(self.BASE_ATTACK, self.BASE_MAX_DAMAGE)
        return playerAttackValue
    
    def playerDefend(self):
        damageReduction = self.BASE_DEFENSE / 100
        return damageReduction
        
    def getCurrentHealth(self):
        return self.currentHealth
    
    def takeDamage(self, damageValue):
        self.currentHealth = self.currentHealth - damageValue
        return self.getCurrentHealth()

import random
from ability import Ability
from basecharacter import BaseCharacter

class Enemy(BaseCharacter):
    currentHealth = 0

    def __init__(self, name, BASE_SP, BASE_DEFENSE, BASE_HITPOINTS, BASE_ATTACK, BASE_MAX_DAMAGE):
        self.name = name
        self.BASE_SP = BASE_SP
        self. BASE_DEFENSE = BASE_DEFENSE
        self.BASE_HITPOINTS = BASE_HITPOINTS
        self.BASE_ATTACK = BASE_ATTACK
        self.ability = None
        self.currentHealth = BASE_HITPOINTS
        self.BASE_MAX_DAMAGE = BASE_MAX_DAMAGE
    
    def enemyAttackValue(self):
        enemyAttack = random.randrange(self.BASE_ATTACK, self.BASE_MAX_DAMAGE)
        return enemyAttack

    def getCurrentHealth(self):
        return self.currentHealth
    
    def takeDamage(self, damageValue):
        self.currentHealth = self.currentHealth - damageValue
        return self.getCurrentHealth()

    def enemyLogic(self):
        pass
        #define enenmy attack logic to be passed to battlemanager
    def playerDefend(self):
        damageReduction = self.BASE_DEFENSE / 100
        return damageReduction

    

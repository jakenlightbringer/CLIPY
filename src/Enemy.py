import random
from ability import Ability
from basecharacter import BaseCharacter

class Enemy(BaseCharacter):
    currentHealth = 0

#    def __init__(self, name, spellPoints, defense, hitPoints, attack, maxDamage):
#        self.name = name
#        self.spellPoints = spellPoints
#        self.defense = defense
#        self.hitPoints = hitPoints
#        self.attack = attack
#        self.ability = None
#        self.currentHealth = hitPoints
#        self.maxDamage = maxDamage
    
    def enemyAttackValue(self):
        enemyAttack = random.randrange(self.attack, self.maxDamage)
        return enemyAttack

    def getCurrentHealth(self):
        return self.currentHealth
    
    def takeDamage(self, damageValue):
        self.currentHealth = self.currentHealth - damageValue
        return self.getCurrentHealth()

    def enemyLogic(self):
        pass
        #define enenmy attack logic to be passed to battlemanager
    def enemyDefend(self):
        damageReduction = self.defense / 100
        return damageReduction

    

import random
from ability import Ability
from basecharacter import BaseCharacter
from constants import ATTACK_LOW, ATTACK_HIGH, ATTACK_MID, DEFEND_LOW, DEFEND_HIGH, DEFEND_MID

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

    def takeDamage(self, damageValue):
        self.currentHealth = self.currentHealth - damageValue
        return self.getCurrentHealth()

    def enemyLogic(self):
        pass
        #define enenmy attack logic to be passed to battlemanager
    def enemyDefend(self):
        damageReduction = self.defense / 100
        return damageReduction
    
    def getEnemyAttackSwing(self):
        swingChoice = [ATTACK_HIGH, ATTACK_MID, ATTACK_LOW]
        enemySwing = random.choice(swingChoice)
        return enemySwing
    def getEnemyDefenseStance(self):
        defenseStanceChoice = [DEFEND_HIGH, DEFEND_MID, DEFEND_LOW]
        defenseStance = random.choice(defenseStanceChoice)
        return defenseStance
        

    

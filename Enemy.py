import random
from ability import Ability

class Enemy:
    def __init__(self, name, baseSP, baseDefense, baseHP, baseAttack, enemyType):
        self.name = name
        self.baseSP = baseSP
        self. baseDefense = baseDefense
        self.baseHP = baseHP
        self.enemyType = enemyType
        self.baseAttack = baseAttack
        self.ability = None
    
    def enemyAttackValue(self, attackValue):
        enemyAttack = random.randrange(attackValue, attackValue + 10)
        return enemyAttack

    def setAbility(self, ability):
        self.ability = ability
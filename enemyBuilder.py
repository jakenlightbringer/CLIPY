import random


class EnemyBuilder:
    def __init__(self, name, hitpoints, attackValue, blockValue, lootTable, enemySP):
        self.name = name
        self.hitpoints = hitpoints
        self.attackValue = attackValue
        self.blockValue = blockValue
        self.lootTable = lootTable
        self.enemySP = enemySP
    
    def enemyAttackValue(attackValue):
        enemyAttack = random.randrange(attackValue, attackValue + 10)
        return enemyAttack



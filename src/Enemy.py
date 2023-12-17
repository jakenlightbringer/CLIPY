import random
from ability import Ability

class Enemy:
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

    
    #can add any objects in the init to display all
    def __str__(self) -> str:
        return (
        f"{self.name} attributes:\n"
        f"Attack: {self.BASE_ATTACK}\n"
        f"Defense: {self.BASE_DEFENSE}\n"
        f"Hitpoints: {self.BASE_HITPOINTS}\n"
        #f"BASE_SP: {self.BASE_SP}\n"
        #f"ability: {self.ability}\n"
        #f"currentHealth: {self.currentHealth}\n"
    )

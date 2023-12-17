import random


class Player:
    currentHealth = 0
    
    def __init__(self, baseClass, BASE_HITPOINTS, BASE_ATTACK, BASE_MAX_DAMAGE, BASE_DEFENSE, BASE_SP):
        self.baseClass = baseClass
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

    
    
    def __str__(self) -> str:
        return (
        f"Player Attributes:\n"
        f"Attack: {self.BASE_ATTACK}\n"
        f"Defense: {self.BASE_DEFENSE}\n"
        f"Hitpoints: {self.BASE_HITPOINTS}\n"
        #f"BASE_SP: {self.BASE_SP}\n"
        #f"ability: {self.ability}\n"
        #f"currentHealth: {self.currentHealth}\n"
    )   
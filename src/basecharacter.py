

class BaseCharacter:
    def __init__(self, baseClass, hitPoints, attack, maxDamage, defense, spellPoints):
        self.currentHealth = hitPoints
        self.spellPoints = spellPoints        
        self.hitPoints = hitPoints        
        self.maxDamage = maxDamage
        self.defense = defense        
        self.characterClass = baseClass
        self.attack = attack

    def getCharacterClass(self):
        return self.characterClass

    def getCurrentHealth(self):
        return self.currentHealth    

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
    
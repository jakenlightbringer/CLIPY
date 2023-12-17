

class BaseCharacter:
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
    
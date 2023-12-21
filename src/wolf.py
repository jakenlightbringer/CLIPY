from Enemy import Enemy

class Wolf(Enemy):
    DEFAULT_HEALTH = 60
    BASE_ATTACK = 18
    BASE_DEFENSE = 5
    BASE_SPELLPOINTS = 2
    BASE_MAX_DAMAGE = 25
    
    def __init__(self):
        super().__init__("Wolf", self.DEFAULT_HEALTH, self.BASE_ATTACK, self.BASE_MAX_DAMAGE, self.BASE_DEFENSE, self.BASE_SPELLPOINTS) 
        
    def __str__(self) -> str:
        return super().__str__()
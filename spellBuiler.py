class Spells:
    def __init__(self, name, spCost, spellEffect):
        self.name = name
        self.spCost = spCost
        self.spellEffect = spellEffect

    
def setAracnidAbilities():
    venom = Spells("Venom", 1, 5)
    enweb = Spells("Enweb", 3, 0)
    return venom, enweb
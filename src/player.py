import random
from basecharacter import BaseCharacter

NameList = [
    'Eldrathor Shadowbane',
    'Lyra Moonfire',
    'Thalion Stormheart',
    'Seraphina Frostwind',
    'Draven Blackthorn',
    'Isolde Silverleaf',
    'Ragnar Ironclad',
    'Elowen Starwhisper',
    'Kael Bloodmoon',
    'Lirael Nightshade',
    'Galadriel Emberfore',
    'Fenrir Stormbreaker',
    'Selene Shadowflame',
    'Malachai Voidstrider',
    'Morwen Swiftsteel',
    'Elysia Dreamweaver',
    'Valen Blackstone',
    'Thora Grimshadow',
    'Eldritch Ravenshadow',
    'Seraphel Astralwind'
]

class Player(BaseCharacter):
    playerName = random.choice(NameList)
    currentHealth = 0
    
    def __init__(self, baseClass, hitpoints, attack, maxDamage, defense, spellPoints):
        self.currentHealth = hitPoints
        self.spellPoints = spellPoints        
        self.hitPoints = hitPoints        
        self.maxDamage = maxDamage
        self.defense = defense        
        self.name = baseClass
        self.attack = attack
        

    def setPlayerName(self, name):
        self.playerName = name

    def getPlayerName():
        return self.playerName

    def playerAttack(self):
        playerAttackValue = random.randrange(self.attack, self.maxDamage)
        return playerAttackValue
    
    def playerDefend(self):
        damageReduction = self.defense / 100
        return damageReduction
        
    def getCurrentHealth(self):
        return self.currentHealth
    
    def takeDamage(self, damageValue):
        self.currentHealth = self.currentHealth - damageValue
        return self.getCurrentHealth()

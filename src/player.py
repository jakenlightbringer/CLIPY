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
    
    def __init__(self, baseClass, BASE_HITPOINTS, BASE_ATTACK, BASE_MAX_DAMAGE, BASE_DEFENSE, BASE_SP):
        self.name = baseClass
        self.BASE_HITPOINTS = BASE_HITPOINTS
        self.currentHealth = BASE_HITPOINTS
        self.BASE_ATTACK = BASE_ATTACK
        self.BASE_DEFENSE = BASE_DEFENSE
        self.BASE_SP = BASE_SP
        self.BASE_MAX_DAMAGE = BASE_MAX_DAMAGE

    def setPlayerName(self, name):
        self.playerName = name
        
    def getPlayerName(self):
        return self.playerName

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

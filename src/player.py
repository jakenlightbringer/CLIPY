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

    def setPlayerName(self, name):
        self.playerName = name
        
    def getPlayerName(self):
        return self.playerName

    def playerAttack(self):
        playerAttackValue = random.randrange(self.attack, self.maxDamage)
        return playerAttackValue
    
    def playerDefend(self):
        damageReduction = self.defense / 100
        return damageReduction
        
    def takeDamage(self, damageValue):
        damageValue = int(damageValue)
        self.currentHealth = self.currentHealth - damageValue
        return self.getCurrentHealth()

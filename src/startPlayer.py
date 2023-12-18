#Start of player class to get the 
import random
import Paladin
from enum import Enum
from player import Player

class Player:
    def __init__(self, baseClass, baseHealth, baseDamage, baseDefense, baseCrit, baseSP):
        self.baseClass = baseClass
        self.baseHealth = baseHealth
        self.baseDamage = baseDamage
        self.baseDefense = baseDefense
        self.baseCrit = baseCrit
        self.baseSP = baseSP
    
    def playerAttack(self):
        playerAttackValue = random.randrange(self.baseDamage, self.baseDamage + 8)
        return playerAttackValue

        

    class PlayerAbilities:
        def __init__(self, name, spCost, spellEffect):
            self.name = name
            self.spCost = spCost
            self.spellEffect = spellEffect
        







#redefine health values far too low -> Maybe in hundreds range -> For displaying this we could display actual health value? 

def getClass():
    
    
    #TODO
    return Paladin.PaladinClass()
    
    while(True):
        playerClass = input("1. Paladin\n 2. Warrior \n 3. Mage\n")
        if (playerClass == "1"):
            return Paladin.PaladinClass()


def getPlayerAbilities(playerClass):
    if(playerClass == "Paladin"):
        divineJustice = Player.PlayerAbilities("Divine Justice", 2, 40)
        holySalvation = Player.PlayerAbilities("Holy Salvation", 1, 30)
        lightsArmor = Player.PlayerAbilities("Light's Armor", 1, 8)
        return divineJustice, holySalvation, lightsArmor
    





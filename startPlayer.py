#Start of player class to get the 
import random

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
        





def getName():
    print("Welcome Adventurer! Please enter your name to begin\n")
    name = input("")
    return name

#redefine health values far too low -> Maybe in hundreds range -> For displaying this we could display actual health value? 
def playerClassStats(playerClass):
    if(playerClass == "Paladin"):
        classStats = Player("Paladin", 120, 16, 7, .05, 3)
        divineJustice = Player.PlayerAbilities("Divine Justice", 2, 40)
        holySalvation = Player.PlayerAbilities("Holy Salvation", 1, 30)
        lightsArmor = Player.PlayerAbilities("Light's Armor", 1, 8)
        return classStats
    elif(playerClass == "Warrior"):
        classStats = Player("Warrior", 150, 18, 5, .1, 3)
        return classStats
    elif(playerClass == "Mage"):
        classStats = Player("Mage", 100, 10, 14, .03, 4)
        return classStats
            

def getClass(playerName):
    print("Hello " + playerName + " Please select your class!\n")
    
    correctClassSelection = False
    while(correctClassSelection == False):
        playerClass = input("1. Paladin\n 2. Warrior \n 3. Mage\n")
        if(playerClass == "1"):
            playerClassChoice = "Paladin"
            correctClassSelection = True
            return playerClassStats(playerClassChoice)
        elif(playerClass == '2'):
            playerClassChoice = "Warrior"
            correctClassSelection = True
            return playerClassStats(playerClassChoice)
        elif(playerClass == '3'):
            playerClassChoice = "Mage"
            correctClassSelection = True
            return playerClassStats(playerClassChoice)
        else:
            print("Please Enter a correct number choice")

def getPlayerAbilities(playerClass):
    if(playerClass == "Paladin"):
        divineJustice = Player.PlayerAbilities("Divine Justice", 2, 40)
        holySalvation = Player.PlayerAbilities("Holy Salvation", 1, 30)
        lightsArmor = Player.PlayerAbilities("Light's Armor", 1, 8)
        return divineJustice, holySalvation, lightsArmor
    
## EXAMPLE OF HOW TO GET SPECIFIC SPELL INFO ##

#divine = getPlayerAbilities("Paladin")

# Find the Divine Justice ability
#divine_justice_ability = None
#for ability in divine:
#    if ability.name == "Divine Justice":
#        divine_justice_ability = ability
#        break

# Print information for Divine Justice if found
#if divine_justice_ability:
 #
 # 
 #    print(f"Name: {divine_justice_ability.name}, SP Cost: {divine_justice_ability.spCost}, Spell Effect: {divine_justice_ability.spellEffect}")
#else:
#    print("Divine Justice not found for the Paladin class.")




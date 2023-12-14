import startPlayer
import random
from Spider import Spider
from player import Player




'''
player selects class
    Paladin
    Warrior
    Mage
player random name assigned
Tutorial battle
    setting building
    allow player to view personal stats
        attack  
        defend
            % based
        view stats
            display % health
        view enemy stats
    
'''

'''
def battleOne(player):
        #enemy loot table
        #aracnidLoot = ["Spider Cloth Cloak", "Venom Infused Ring"]
        #Enemy built
        aracnidEnemy = enemyBuilder.EnemyBuilder("Skalash", 60, 18, 5, random.choice(aracnidLoot), 3)
        print("\n Oh Paladin, so naive you think you can cleanse these land of our corruption.")
        print("I am Skalash, servant of Spider Lord Vandris. YOU WILL DIE")
        #battle loop
        while(player.baseHealth and aracnidEnemy.hitpoints > 0):
            playerAttackTurn = True
            if(playerAttackTurn == True):
                pAttackValue = player.playerAttack()
                enemyDefenseValue = aracnidEnemy.blockValue
                paladinAbilities = startPlayer.getPlayerAbilities(player.baseClass)
                #Defines player action (Chosing between abilities or basic attacks, can see enemy stats as well)
                playerActionTaken = False
                while(playerActionTaken == False):
                    print("\nEnter Your Action\n")
                    playerAction = input("\n1. Basic Attack\n2. See Abilities List \n3. See Enemy Stats\n")
                    if(playerAction == "1"):
                        aracnidEnemy.hitpoints -= pAttackValue 
                        aracnidEnemy.hitpoints += enemyDefenseValue
                        aracnidEnemy.hitpoints + enemyDefenseValue
                        print(f"You attacked {aracnidEnemy.name} for {pAttackValue}. {aracnidEnemy.name} blocked {enemyDefenseValue} damage.")
                        print(f"{aracnidEnemy.name} has {aracnidEnemy.hitpoints} hit points left.")
                        playerActionTaken = True
                        playerAttackTurn = False
                    elif(playerAction == "2"):
                        divineJustice = None
                        holySalvation = None
                        lightsArmor = None
                        #Paladin spell implementation/Assignment
                        for ability in paladinAbilities:
                            if(ability.name == "Divine Justice"):
                                divineJustice = ability
                            elif(ability.name == "Holy Salvation"):
                                holySalvation = ability
                            elif(ability.name == "Light's Armor"):
                                lightsArmor = ability
                            print(f"Name: {ability.name}, SP Cost: {ability.spCost}, Spell Effect: {ability.spellEffect}")
                        print('\nPlease select an Ability or Return\n')
                        
                        playerAbilitySelection = input("\n1. Divine Justice\n2. Holy Salvation\n3. Light's Armor\n")
                        #Divine Justice Spell implementation
                        if(playerAbilitySelection == "1"):
                            player.baseSP -= divineJustice.spCost
                            aracnidEnemy.hitpoints -= divineJustice.spellEffect
                            print(f'You cast {divineJustice.name} dealing {divineJustice.spellEffect} damage. {aracnidEnemy.name} has {aracnidEnemy.hitpoints} hitpoints left')
                            print(f"You have {player.baseSP} skillpoints left")
                            playerActionTaken = True
                            playerAttackTurn = False
                        if(playerAbilitySelection == "2"):
                            if player.baseHealth == 120:
                                print(f"It seems that the heat of the battle has caused you to waste your {holySalvation.name}. It has no effect as you do not have any wounds.")
                                player.baseSP -= holySalvation.spCost
                                playerActionTaken = True
                                playerAttackTurn = False
                            elif player.baseHealth < 120:
                                player.baseSP -= holySalvation.spCost
                                print(f"The light graces you and feel its warmth across your skin")
                                print(f"{holySalvation.name} heals you for {holySalvation.spellEffect}. Your have {player.baseHealth} health and {player.baseSP} skill points.")
                        if(playerAbilitySelection == "3"):
                            player.baseDefense += lightsArmor.spellEffect
                            player.baseSP -= lightsArmor.spCost
                            print(f'You Case {lightsArmor.name}, increasing your armor by {lightsArmor.spellEffect}.')
                            print(f"You now have {player.baseSP} skillpoints remaining")
                            playerActionTaken = True
                            playerAttackTurn = False
                    elif(playerAction == "3"):
                        print(f"Enemy Name: {aracnidEnemy.name}\nEnemy HP: {aracnidEnemy.hitpoints}\nEnemy Attack Value: {aracnidEnemy.attackValue}\nEnemy Defense Value{enemyDefenseValue}\n")
                        playerActionTaken = False
                    else:
                        print("Invalid selection. Please choose a valid action.")
                  
                

                
                
                playerAttackTurn = False
            
            #Defining and assigning Enemy Abilities
            enemyAbilities = spellBuiler.setAracnidAbilities()
            for eAbility in enemyAbilities:
                if(eAbility.name == "Venom"):
                    venom = eAbility
                elif(eAbility.name == "Enweb"):
                    enweb = eAbility
            #set if result = attackturn -> set playerattack turn
            if(playerAttackTurn == False):
                enemyAttackValue = aracnidEnemy.attackValue
                playerDefenseValue = player.baseDefense
                enemyAbilitySelection = enemyLogic(aracnidEnemy, venom, enweb, player, playerAttackTurn)
                if(enemyAbilitySelection == 1):
                    print(f"\n{aracnidEnemy.name} attacks you for {aracnidEnemy.attackValue}. You blocked {player.baseDefense}")
                    print(f"You have {player.baseHealth} Health remaining")
                playerAttackTurn = True
                if(enemyAbilitySelection == 2):
                    print(f"\n{aracnidEnemy.name} attacks you with {venom.name} for {venom.spellEffect}. You blocked {player.baseDefense}")
                    print(f"You have {player.baseHealth} Health remaining")
                playerAttackTurn = True
                if(enemyAbilitySelection == 3):
                    print(f"\n{aracnidEnemy.name} attacks you with {enweb.name}. Stunning you for one turn.")
                playerAttackTurn = False
        if(aracnidEnemy.hitpoints <= 0):
            print(f'You have defeated {aracnidEnemy.name}. You search the disgusting creatures corpse and find a {aracnidEnemy.lootTable}.')
            if(aracnidEnemy.lootTable == "Spider Cloth Cloak"):
                print("You equip the cloak and you increase your defense by 5")
                player.baseDefense += 5
            if(aracnidEnemy.lootTable == "Venom Infused Ring"):
                print("You equip the ring and increase your Damage by 5")
                player.baseDamage += 5
        if(player.baseHealth <= 0):
            print("You Lose!")
            return 0

'''







def getName():
        print("Welcome Adventurer! Please enter your name to begin\n")
        #name = input("")
        #return name
        return "jake"



playerName = getName()
playerInstance = startPlayer.getClass(playerName)

'''
def getNewEnemy()
  return spider()

game loop (while !dead) {
   enemy = getNewEnemy()
   battleLoop (while player || enemy !dead) {
    enemy vs player    
   }

   
}

'''
# Need figure out way to determine what enemy passed into the game loop
#options are hardcode which enemy is coming or randomize enemy


def getEnemy():
    return Spider()

def gameLoop():
    #determine battle count
    battleCount = 0
    while(True):
        
        newEnemy = getEnemy()
        
        while(playerInstance.currentHealth > 0 or newEnemy.getCurrentHealth() > 0):
            playerChoice = input("\n1. Attack, 2. Defend, 3. Your Stats, 4. Enemy Stats\n")
            if(playerChoice == '1'):
                print(f"{playerName} attacks dealing {playerInstance.playerAttack()} damage")
            if(playerChoice == '2'):
                playerAttack = playerInstance.playerAttack()
                newEnemy.takeDamage(playerAttack)
                print(f"{playerName} attacks for {playerAttack} damage. {newEnemy.name} has {newEnemy.getCurrentHealth()} HP")
            if(playerChoice == '3'):
                print(playerInstance)
            if(playerChoice == '4'):
                print(newEnemy)

            



        break
    







def main():
    
    
    
    
    print(playerInstance)


    if playerInstance.baseClass == "Paladin":
        print("\nYou survey the battlefield before you. The crescendo and clash of plate scream across the wartorn barrens.")
        print(f"Brother {playerName}, a voice calls out. Brother Eziekiel and Brother Addonis have been taken by the scorpids into the cave")
        print("You turn to see the aracnid creatures dragging away two of your fellow brethren into the dark lair")
        print("Just as you begin to walk towards the lair, an aracnid deformation leaps out towards you.")

        gameLoop()


    


if __name__ == "__main__":
    main()

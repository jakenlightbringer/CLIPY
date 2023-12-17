from battlemanager import BattleManager
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


def enemyActionSelection():
    attackSelection = random.randrange(1, 3)
    return attackSelection






def gameLoop():
    #determine battle count
    battleCount = 1

    battleMgr = BattleManager()
    while(True):
        
        newEnemy = battleMgr.getEnemyClassSelection(battleCount)
        ATTACK = '1'
        DEFEND = '2'
        PLAYER_STATS = '3'
        ENEMY_STATS = '4'

        '''
        
            Enemy & Player Type
        
        
            playerAction
            EnemyAction
            
            initiative = rand(player or enemy)
            
             getBattleResult(playeraction,  , initiative)
                {player_damage_taken, enemy_damage_taken}

            roundOutcome = {
                "player_damage" : 10
                "enemy_damage" : 5
            }
            
            print (roundOutcome['player_damage']) #10
            
            
            
            
            while (!done or dead)

                if (enemy or player status)
                    displayStats
                else                
                    if (player_initiative)
                        getPlayerAction()
                        TakePlayerAction()
                        if (TakePlayerAction() == PLAYER or ENEMY stats)
                            pass
                        if (EnemeyIsNotDead)
                            TakeEnemyAction()
                    else
                        TakeEnemyAction()
                        getPlayerAction()
                        if (PlayerIsNotDead)
                            TakePlayerAction()
                    
                    If EnemyIsDead
                        break;
                    if PlayerIsDead
                        return player_dead
                    
        def endGame()
            print end game stas
                Total enemies killed
                total damange taken
                total damage done
                total rounds
                new high in any stat 
        ''' 
        while(playerInstance.currentHealth >= 0 and newEnemy.getCurrentHealth() >= 0):
            playerChoice = input("\n1. Attack, 2. Defend, 3. Your Stats, 4. Enemy Stats\n")
            damage = battleMgr.getCombatantsDamageOuput(playerChoice, 0)
            newEnemy.takeDamage(damage['player_damage']) #playerAttack
            print(damage)
            print(newEnemy.getCurrentHealth())
            playerInstance.takeDamage(damage['enemy_damage']) #enemyAttack
        
        
        
        '''
        while(playerInstance.currentHealth >= 0 and newEnemy.getCurrentHealth() >= 0):
            playerChoice = input("\n1. Attack, 2. Defend, 3. Your Stats, 4. Enemy Stats\n")
            if(playerChoice == ATTACK):
                playerAttack = playerInstance.playerAttack()
                
                print(f"{playerName} attacks for {playerAttack} damage. {newEnemy.name} has {newEnemy.getCurrentHealth()} HP")
            elif(playerChoice == DEFEND ) :
                enemyDamge = newEnemy.enemyAttackValue()
                playerDamageReduction = enemyDamge * playerInstance.playerDefend()
                enemyDamge -= playerDamageReduction
                playerInstance.takeDamage(enemyDamge)
            elif(playerChoice == PLAYER_STATS):
                print(playerInstance) 
            elif(playerChoice == ENEMY_STATS):
                print(newEnemy)
            if(enemyActionSelection() == 1):
                print(enemyActionSelection())
                enemyAttack = newEnemy.enemyAttackValue()
                playerInstance.takeDamage(enemyAttack)
                print(f"{newEnemy.name} attacks for {enemyAttack} damage. {playerName} has {playerInstance.getCurrentHealth()} HP")
            elif(enemyActionSelection() == 2):
                print(enemyActionSelection())
                playerDamage = playerInstance.playerAttack()
                enemyDamageReduction = playerDamage * playerInstance.playerDefend()
                playerDamage -= enemyDamageReduction
                newEnemy.takeDamage(playerDamage)
                print('Defend')

        if(newEnemy.getCurrentHealth() <= 0):
            print("\nYou've Killed Your Enemy!")
            print(f"\n You have {playerInstance.getCurrentHealth()} health remaining.")
        if(playerInstance.getCurrentHealth() <= 0):
            print("Youve Lost!")

        break
        '''
        
        

def main():
    
    
    
    
    


    if playerInstance.name == "Paladin":
        print("\nYou survey the battlefield before you. The crescendo and clash of plate scream across the wartorn barrens.")
        print(f"Brother {playerName}, a voice calls out. Brother Eziekiel and Brother Addonis have been taken by the scorpids into the cave")
        print("You turn to see the aracnid creatures dragging away two of your fellow brethren into the dark lair")
        print("Just as you begin to walk towards the lair, an aracnid deformation leaps out towards you.")

        gameLoop()


    


if __name__ == "__main__":
    main()

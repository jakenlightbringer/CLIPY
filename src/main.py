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

playerInstance = startPlayer.getClass()
playerName = playerInstance.getPlayerName()

def gameLoop():
    #determine battle count
    battleCount = 1

    battleMgr = BattleManager()
    while(True):
        
        newEnemy = battleMgr.getEnemyClassSelection(battleCount)

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
            playerChoice = int(input("\n1. Attack, 2. Defend, 3. Your Stats, 4. Enemy Stats\n"))
            damage = battleMgr.getCombatantsDamageOuput(playerChoice, 0)
            print(damage)
            #print(newEnemy.getCurrentHealth())
        
        

def main():
    
    
    
    
    


    if playerInstance.name == "Paladin":
        print("\nYou survey the battlefield before you. The crescendo and clash of plate scream across the wartorn barrens.")
        print(f"Brother {playerName}, a voice calls out. Brother Eziekiel and Brother Addonis have been taken by the scorpids into the cave")
        print("You turn to see the aracnid creatures dragging away two of your fellow brethren into the dark lair")
        print("Just as you begin to walk towards the lair, an aracnid deformation leaps out towards you.")

        gameLoop()


    


if __name__ == "__main__":
    main()

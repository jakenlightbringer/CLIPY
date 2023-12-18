from battlemanager import BattleManager
from gamestats import GameStats
import startPlayer
import random
from player import Player


def gameLoop(playerInstance):
    #determine battle count
    battleCount = 0

    battleMgr = BattleManager()
    gameStats = GameStats()

    #todo handle player death and/or game exit
    while(battleCount < 1):
        gameStats.incrementRound()
        battleCount += 1     
        newEnemy = battleMgr.getEnemyClassSelection(battleCount)

        '''

            Enemy & Player Type
        
        
            playerAction
            EnemyAction
            
            initiative = rand(player or enemy)
            
             getBattleResult(playeraction,  , initiative)
                {player_damage_taken, enemy_damage_taken}
            
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
        ''' 
        while(playerInstance.currentHealth >= 0 and newEnemy.getCurrentHealth() >= 0):
            playerChoice = int(input("\n1. Attack, 2. Defend, 3. Your Stats, 4. Enemy Stats\n"))
            damage = battleMgr.getCombatantsDamageOuput(playerChoice, 0)
            gameStats.addDamageTaken(damage['player_damage_taken'])
            gameStats.addDamageDealt(damage['player_damage_given'])
            print(damage)
            #print(newEnemy.getCurrentHealth())
           
    print(gameStats)
        
        
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
    playerInstance = startPlayer.getClass()
    playerName = playerInstance.getPlayerName()
    
    if playerInstance.name == "Paladin":
        print("\nYou survey the battlefield before you. The crescendo and clash of plate scream across the wartorn barrens.")
        print(f"Brother {playerName}, a voice calls out. Brother Eziekiel and Brother Addonis have been taken by the scorpids into the cave")
        print("You turn to see the aracnid creatures dragging away two of your fellow brethren into the dark lair")
        print("Just as you begin to walk towards the lair, an aracnid deformation leaps out towards you.")

        gameLoop(playerInstance)

if __name__ == "__main__":
    main()

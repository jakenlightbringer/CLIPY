from Spider import Spider
from Paladin import PaladinClass
import random

# Need figure out way to determine what enemy passed into the game loop
#options are hardcode which enemy is coming or randomize enemy

class BattleManager:
    currentEnemy = Spider()
    
    
    def getEnemyClassSelection(self, battleCount):
        return self.currentEnemy
    def takePlayerAction(self, playerAction):
        result = None
        P_ATTACK = '1'
        P_DEFEND = '2'
        PLAYER_STATS = '3'
        ENEMY_STATS = '4'
        playerInstance = PaladinClass()
        
        if (playerAction == P_ATTACK):
            result = playerInstance.playerAttack()
        if (playerAction == P_DEFEND):
            result = playerInstance.playerDefend()
        
        return result
    
    def getEnemyAction(self):
        #TEMP
        return 1
        enemyActionSelection = random.randint(1, 2)
        return enemyActionSelection
    
    def takeEnemyAction(self, enemyActionSelection):
        E_ATTACK = 1
        E_DEFEND = 2
        if(enemyActionSelection == E_ATTACK):
            enemy = self.getEnemyClassSelection(1)
            enemyAttackValue = enemy.enemyAttackValue()
            return enemyAttackValue
        
    
    #returns damage given    
    def getCombatantsDamageOuput(self, playerAction, initiative):
        battleCount = 1
        
        enemy = self.getEnemyClassSelection(battleCount)
        playerInstance = PaladinClass()
        
        enemySelection = self.getEnemyAction()
        
        
        
        if(playerAction == "1" and enemySelection == 1):
            playerAttack = self.takePlayerAction(playerAction)
            enemyResult = self.takeEnemyAction(enemySelection)
            roundResult = {
                'player_damage_given' : playerInstance.playerAttack(),
                'player_damage_taken' : playerInstance.takeDamage(enemyResult),
                'player_current_health': playerInstance.getCurrentHealth(),
                
                'enemy_damage_given' : enemy.enemyAttackValue(),
                'enemy_damage_taken' : enemy.takeDamage(playerAttack),
                'enemy_current_health' : enemy.getCurrentHealth()
            }
            return (roundResult)
            
            
        
        
        
        
        
        
        
       
        

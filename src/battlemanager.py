from Spider import Spider
from Paladin import PaladinClass
import random

# Need figure out way to determine what enemy passed into the game loop
#options are hardcode which enemy is coming or randomize enemy

class BattleManager:
    ATTACK = 1
    DEFEND = 2
    PLAYER_STATS = 3
    ENEMY_STATS = 4
    playerInstance = PaladinClass()
    currentEnemy = Spider()    
    
    def getEnemyClassSelection(self, battleCount):
        return self.currentEnemy        
    def takePlayerAction(self, playerAction):        
        result = None
        
        
        if (playerAction == self.ATTACK):
            result = self.playerInstance.playerAttack()
        if (playerAction == self.DEFEND):
            result = self.playerInstance.playerDefend()
        
        return result
    
    def getEnemyAction(self):
        #TEMP
        return 1
        enemyActionSelection = random.randint(1, 2)
        return enemyActionSelection
    
    def takeEnemyAction(self, enemyActionSelection):
        if(enemyActionSelection == self.ATTACK):
            enemy = self.getEnemyClassSelection(1)
            enemyAttackValue = enemy.enemyAttackValue()
            return enemyAttackValue
        
    
    #returns damage given    
    def getCombatantsDamageOuput(self, playerAction, initiative):
        battleCount = 1
        
        enemy = self.getEnemyClassSelection(battleCount)

            
        enemyAction = self.getEnemyAction()
                
        
        if(playerAction == self.ATTACK and enemyAction == self.ATTACK):
            playerAttack = self.takePlayerAction(playerAction)            
            enemyAttack = self.takeEnemyAction(enemyAction)
            self.playerInstance.takeDamage(enemyAttack)
            enemy.takeDamage(playerAttack)
            

            roundResult = {
                'player_damage_given' : playerAttack,
                'player_damage_taken' : enemyAttack,
                'player_current_health': self.playerInstance.getCurrentHealth(),
                
                'enemy_damage_given' : enemyAttack,
                'enemy_damage_taken' : playerAttack,
                'enemy_current_health' : enemy.getCurrentHealth()
            }
            #return (roundResult)
        elif(playerAction == self.ATTACK and enemyAction == self.DEFEND):
            pass
            
            
            
        return (roundResult)
            
            
        
        
        
        
        
        
        
       
        

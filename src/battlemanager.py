from Spider import Spider
from Paladin import PaladinClass
from wolf import Wolf
import random

# Need figure out way to determine what enemy passed into the game loop
#options are hardcode which enemy is coming or randomize enemy

class BattleManager:
    ATTACK = 1
    DEFEND = 2
    PLAYER_STATS = 3
    ENEMY_STATS = 4
    
    currentEnemy = Spider() 
    enemyList = [Spider(), Wolf()]
    
    #need a get playerClass function to initilize the player
    def setPlayer(self, player):
        self.playerInstance = player
        
    #TODO Add player input to select class return class wanted
    def getStartingClass():
        return PaladinClass()
    
    def getCurrentEnemy(self):
        return self.currentEnemy        
    
    #can be changes to get new enemy -> randomized enemy next
    def getNewEnemy(self, battleCount):
        if (battleCount == 1):
            self.currentEnemy = Spider() 
        else:
            self.currentEnemy = random.choice(self.enemyList)

        return self.currentEnemy
        
    def takePlayerAction(self, playerAction):        
        result = None
        if (playerAction == self.ATTACK):
            result = self.playerInstance.playerAttack()

        if (playerAction == self.DEFEND):
            result = self.playerInstance.playerDefend()
        
        return result

    def getEnemyAction(self):
        enemyActionSelection = random.randint(1, 2)
        return enemyActionSelection
    
    def takeEnemyAction(self, enemyActionSelection):
        if(enemyActionSelection == self.ATTACK):
            enemy = self.currentEnemy
            enemyAttackValue = self.currentEnemy.enemyAttackValue()
            return enemyAttackValue
        elif(enemyActionSelection == self.DEFEND):
            enemyDefenseValue = self.currentEnemy.enemyDefend()
            return enemyDefenseValue
    
    #returns damage given    
    def getCombatantsDamageOuput(self, playerAction, initiative):
        battleCount = 1
        enemy = self.getCurrentEnemy()
        enemyAction = self.getEnemyAction()                
        
        if(playerAction == self.ATTACK and enemyAction == self.ATTACK):
            playerAttack = self.takePlayerAction(playerAction)            
            enemyAttack = self.takeEnemyAction(enemyAction)
            #Attack swing logic
            playerAttackSwing = self.playerInstance.getPlayerAttackSwing()
            enemyAttackSwing = self.currentEnemy.getEnemyAttackSwing()
            
            if(playerAttackSwing == enemyAttackSwing):
                playerAttack = 0
                enemyAttack = 0
                print("Your blades clash blocking each other")
            else:
                self.playerInstance.takeDamage(enemyAttack)
                enemy.takeDamage(playerAttack)
            
            roundResult = {
                'player_damage_given' : playerAttack,
                'player_damage_taken' : enemyAttack,
                'player_current_health': self.playerInstance.getCurrentHealth(),
                'player_action': 'Attacks',
                
                'enemy_damage_given' : enemyAttack,
                'enemy_damage_taken' : playerAttack,
                'enemy_current_health' : enemy.getCurrentHealth(),
                'enemy_action' : 'Attacks'
            }
            
            return (roundResult)
        
        elif(playerAction == self.ATTACK and enemyAction == self.DEFEND):
            playerAttack = self.takePlayerAction(playerAction)
            enemyDefend = self.takeEnemyAction(enemyAction)
            enemyAttack = 0
            
            playerAttackSwing = self.playerInstance.getPlayerAttackSwing()
            enemyDefenceStance = self.currentEnemy.getEnemyDefenseStance()
            
            if(playerAttackSwing == enemyDefenceStance):
                playerAttack = 0
                print(f"{self.currentEnemy.getCharacterClass()} blocks your swing perfectly!")
                actualDamageAmount = 0
                damageAmountReduced = 0
            else:
                #Defense Calculation -> Gets the decimal multiplies by player attack to get damage reduction number -> Subtracts from the attack
                damageAmountReduced = int(enemyDefend * playerAttack)
                actualDamageAmount = playerAttack - damageAmountReduced
                enemy.takeDamage(actualDamageAmount)
            
            roundResult = {
                'player_damage_given' : playerAttack,
                'player_damage_taken' : enemyAttack,
                'player_current_health': self.playerInstance.getCurrentHealth(),
                'player_action': 'Attacks',
                
                'enemy_damage_given' : enemyAttack,
                'enemy_damage_taken' : actualDamageAmount,
                'enemy_damage_blocked': damageAmountReduced,
                'enemy_current_health' : enemy.getCurrentHealth(),
                'enemy_action' : 'Defends'
            }
            
            return (roundResult)
        
        elif(playerAction == self.DEFEND and enemyAction == self.ATTACK):
            playerDefend = self.takePlayerAction(playerAction)
            enemyAttack = self.takeEnemyAction(enemyAction)
            playerAttack = 0
            
            playerDefenseStance = self.playerInstance.getPlayerDefenseStance()
            enemyAttackSwing = self.currentEnemy.getEnemyAttackSwing()
            
            if(playerDefenseStance == enemyAttackSwing):
                print(f'{self.playerInstance.name} perfectly blocks {self.currentEnemy.getCharacterClass()} swing')
                enemyAttack = 0
                actualDamageAmount = 0
                damageAmountReduced = 0
            else:
                damageAmountReduced = int(playerDefend * enemyAttack)
                actualDamageAmount = enemyAttack - damageAmountReduced
                self.playerInstance.takeDamage(actualDamageAmount)
        
            roundResult = {
                'player_damage_given' : playerAttack,
                'player_damage_taken' : actualDamageAmount,
                'enemy_damage_blocked': damageAmountReduced,
                'player_current_health': self.playerInstance.getCurrentHealth(),
                'player_action' : 'Defends',
                
                'enemy_damage_given' : actualDamageAmount,
                'enemy_damage_taken' : playerAttack,
                'enemy_current_health' : enemy.getCurrentHealth(),
                'enemy_action' : 'Attacks'
            }
        
            return (roundResult)
        
        elif(playerAction == self.DEFEND and enemyAction == self.DEFEND):
            playerAttack = 0
            enemyAttack = 0
            roundResult = {
                'player_damage_given' : playerAttack,
                'player_damage_taken' : enemyAttack,
                'player_current_health': self.playerInstance.getCurrentHealth(),
                'player_action' : 'Defends',
                
                'enemy_damage_given' : enemyAttack,
                'enemy_damage_taken' : playerAttack,
                'enemy_current_health' : enemy.getCurrentHealth(),
                'enemy_action' : 'Defends'
            }
            return (roundResult)
        else:
            print("enter correct input")
            
            
        
            
            
        
        
        
        
        
        
        
       
        

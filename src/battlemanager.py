from Spider import Spider

# Need figure out way to determine what enemy passed into the game loop
#options are hardcode which enemy is coming or randomize enemy

class BattleManager:
    currentEnemy = Spider()
    
    def getEnemyClassSelection(self, battleCount):
        return self.currentEnemy
    
    #returns damage given    
    def getCombatantsDamageOuput(self, playerAction, initiative):
        roundResult = {
            'player_damage' : 10,
            'enemy_damage' : 5,
            #'player_health' : playerInstance.getCurrentHealth(),

        }
        return (roundResult)

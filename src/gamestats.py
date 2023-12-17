
class GameStats:
    totalEnemiesDefeated = 0
    totalDamageTaken = 0
    totalDamageDone = 0
    totalRoundsPlayed = 1

    def incrementRound(self):
        self.totalRoundsPlayed += 1
    
    def incrementEnemeiesDefeated(self):
        self.totalEnemiesDefeated += 1
    
    def addDamageTaken(self, damage):
        self.totalDamageTaken += damage
    
    def addDamageDone(self, damage):
        self.totalDamageDone += damage


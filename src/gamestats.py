
class GameStats:
    totalEnemiesDefeated = 0
    totalDamageTaken = 0
    totalDamageDealt = 0
    totalRoundsPlayed = 0

    def incrementRound(self):
        self.totalRoundsPlayed += 1
    
    def incrementEnemeiesDefeated(self):
        self.totalEnemiesDefeated += 1
    
    def addDamageTaken(self, damage):
        self.totalDamageTaken += damage
    
    def addDamageDealt(self, damage):
        self.totalDamageDealt += damage

    def __str__(self):
        return (f"Total Rounds: {self.totalRoundsPlayed} \
            Enemies Defeated: {self.totalEnemiesDefeated} \
            Damage Dealt: {self.totalDamageDealt} \
            Damage Taken: {self.totalDamageTaken}"
        )

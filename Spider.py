from Enemy import Enemy
from ability import Ability

class Spider(Enemy):
    def __init__(self, name, baseSP, baseDefense, baseHP, baseAttack, enemyType):
        super().__init__(name, baseSP, baseDefense, baseHP, baseAttack, enemyType)
        
        spiderSP = 3
        spiderDefense = 6
        spiderHP = 80
        spiderAttack = 16

        #spider enemy health values

        

        self.venom = Ability("Venom", spCost=1, spellEffect=5)

spider_test = Spider("Spider", 3, 6, 80, 16, "spider")

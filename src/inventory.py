from items import Item

class Inventory:
    def __init__(self):
        self.head = None
        self.shoulders = None
        self.chest = None
        self.gloves = None
        self.pants = None
        self.boots = None      

    
    def getItem(self, item):
        #TODO call items.py to get an Item
        pass      
    def equipItem(self, gearSlot, item):
        #TODO EQUIP ITEM TO A SPECIFIED SLOT 
        pass
    def unequipItem(self, gearSlot):
        #TODO UNEQUIP ITEM FROM SPECIFIED SLOT
        pass
    def compareItem(self, equippedItem, newItem):
        #TODO COMPARE ATTRIBUTES FROM ONE ITEM TO ANOTHER AND ALLOW OPTION TO REPLACE ITEM
        pass
    def displayGear(self):
        #TODO Display equipped gear
        pass
    
    

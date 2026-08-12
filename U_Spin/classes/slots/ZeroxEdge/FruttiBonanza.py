from classes.nesting.ZeroxEdge import ZeroxEdge
from utilityFunctions import Sleep

slotCode = '0xedgefrutti-bonanza'

class FruttiBonanza(ZeroxEdge):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 300
        self.estimatedWaitTime = 50
        self.bonusOption = 7
        
        self.run()
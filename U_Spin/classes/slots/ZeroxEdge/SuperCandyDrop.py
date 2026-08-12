from classes.nesting.ZeroxEdge import ZeroxEdge
from utilityFunctions import Sleep

slotCode = '0xedge-super-candy-drop'

class SuperCandyDrop(ZeroxEdge):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 213
        self.estimatedWaitTime = 35
        self.bonusOption = 5

        self.run()
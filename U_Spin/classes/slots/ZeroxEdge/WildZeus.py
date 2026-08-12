from classes.nesting.ZeroxEdge import ZeroxEdge
from classes.classUtilityFunctions import takePicture, cleanNumber
from utilityFunctions import Sleep

slotCode = '0xedge-wild-zeus'

class WildZeus(ZeroxEdge):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 500
        self.estimatedWaitTime = 80
        self.bonusOption = 6
        
        self.run()
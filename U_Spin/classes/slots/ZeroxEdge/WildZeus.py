from classes.nesting.ZeroxEdge import ZeroxEdge
from classes.classUtilityFunctions import takePicture, cleanNumber
from classes.Capture import Capture
from utilityFunctions import Sleep

slotCode = '0xedge-wild-zeus'

class WildZeus(ZeroxEdge):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 500
        self.estimatedWaitTime = 80
        self.bonusOption = 6
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,3) # loading time
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        self.checkStart()
        self.checkFin()
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()
from classes.nesting.EighteenGaming import EighteenGaming
from utilityFunctions import Sleep

slotCode = '18gaming-zombie-harvest'

class ZombieHarvest(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 30
        
        self.changeScene() # take the screen blocks off
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        self.checkFinEle()
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()
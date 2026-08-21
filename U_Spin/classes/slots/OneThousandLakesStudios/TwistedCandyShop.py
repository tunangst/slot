from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios
from utilityFunctions import Sleep

slotCode = '1000lakesstudios-twisted-candy-shop'

class TwistedCandyShop(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 500
        self.estimatedWaitTime = 180
        
        self.changeScene() # take the screen blocks off
        self.findSplashLoaded()
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        self.checkFin(crop=slotCode)
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()
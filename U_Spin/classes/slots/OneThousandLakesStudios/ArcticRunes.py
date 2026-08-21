from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios
from utilityFunctions import Sleep

slotCode = '1000lakesstudios-arctic-runes'

class ArcticRunes(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 400
        self.estimatedWaitTime = 40

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
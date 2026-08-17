from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios
from utilityFunctions import Sleep

slotCode = '1000lakesstudios-yakuza-v-i-p'

class YakuzaVIP(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 300
        self.estimatedWaitTime = 30
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,17)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb,3)
        self.checkFin(crop=slotCode)
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()
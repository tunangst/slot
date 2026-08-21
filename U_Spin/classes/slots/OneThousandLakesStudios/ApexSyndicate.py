from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios
from utilityFunctions import Sleep

slotCode = '1000lakesstudios-apex-syndicate'

class ApexSyndicate(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 777
        self.estimatedWaitTime = 120

        self.changeScene()
        self.findSplashLoaded()
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        self.checkFin(crop=slotCode)
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()
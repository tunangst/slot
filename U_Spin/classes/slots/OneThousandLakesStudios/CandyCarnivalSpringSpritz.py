from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios
from classes.classUtilityFunctions import cleanNumber
from utilityFunctions import Sleep

slotCode = '1000lakesstudios-candy-carnival-spring-spritz'
# winningScreenshot = 'fin'
# closingWords = ['total win', 'totalwin']

class CandyCarnivalSpringSpritz(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        Sleep(sb,3)
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 500
        self.estimatedWaitTime = 30

        self.changeScene() # take the screen blocks off
        self.findSplashLoaded()
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        self.checkFin(slotCode)
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()
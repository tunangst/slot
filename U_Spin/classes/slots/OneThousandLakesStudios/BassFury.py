from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios
from utilityFunctions import Sleep

slotCode = '1000lakesstudios-bass-fury'
closingWords = ['the big catch over'] # 'totalwin'

class BassFury(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 250
        self.estimatedWaitTime = 50
        self.splashCheckStr = '//div[@aria-label="Press anywhere to start"]'

        self.changeScene() # take the screen blocks off
        self.findSplashLoaded()
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb,15)
        self.run()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin(action='check end words',targetWordList=closingWords)
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()
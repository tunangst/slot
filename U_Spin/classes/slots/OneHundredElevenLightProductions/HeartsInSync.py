from classes.nesting.OneHundredElevenLightProductions import OneHundredElevenLightProductions
from utilityFunctions import Sleep

slotCode = '111lightproductions-hearts-in-sync'

class HeartsInSync(OneHundredElevenLightProductions):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 90
        self.bonusOption = 3
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,13)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        self.checkFin(crop=slotCode)
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()
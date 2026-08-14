from classes.nesting.OneHundredElevenLightProductions import OneHundredElevenLightProductions
from classes.classUtilityFunctions import cleanNumber
from utilityFunctions import Sleep

slotCode = '111lightproductions-nfl-touchdown'
spinWords = ['free','spins','free spins']

class NFLTouchdown(OneHundredElevenLightProductions):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 30
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,10) # takes too long to load main screen
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb,3)
        # self.run()
        # Sleep(sb,10)
        self.checkFin(crop=slotCode,action='check end words',targetWordList=spinWords)
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()

    # def findFinBal(self):
    #     self.defaultClick()
    #     Sleep(self.sb,3)
    #     balanceStr = 'span.mg-balance-value'
    #     self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
from classes.nesting.OneHundredElevenLightProductions import OneHundredElevenLightProductions
from classes.classUtilityFunctions import cleanNumber
from utilityFunctions import Sleep

slotCode = '111lightproductions-gemburst-rush'
spinWords = ['free','spins','free spins']

class GemburstRush(OneHundredElevenLightProductions):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 30
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,13)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        self.checkFin(crop=slotCode,action='check end words',targetWordList=spinWords)
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()
        
    def setup(self):
        self.clickBuyout()
        Sleep(self.sb,3)
        self.clickBonusCard()
        Sleep(self.sb,3)
        self.clickConfirm()

    # def run(self):
    #     self.sb.find_element(self.canvasStr).click()

    # def findFinBal(self):
    #     self.defaultClick()
    #     Sleep(self.sb,3)
    #     balanceStr = '//span[contains(@class,"mg-balance-value")]'
    #     self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
from classes.nesting.OneHundredElevenLightProductions import OneHundredElevenLightProductions
from classes.classUtilityFunctions import cleanNumber
from utilityFunctions import Sleep

slotCode = '111lightproductions-the-syndicate'
spinWords = ['free spins','free','spins']

class TheSyndicate(OneHundredElevenLightProductions):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.estimatedWaitTime = 30
        self.buyoutBalance = 200
        self.bonusOption = 3
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb,15)
        self.checkFin(crop=slotCode,action='check end words',targetWordList=spinWords)
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()

    # def setup(self):
    #     self.clickBuyout()
    #     Sleep(self.sb)
    #     scatterStr = f'//div[contains(@class,"cards")]/div[{self.bonusOption}]/div[contains(@class,"card-body")]/button'
    #     self.sb.find_element(scatterStr).click()
    #     Sleep(self.sb)
    #     self.clickConfirm()

    # def findFinBal(self):
    #     self.defaultClick()
    #     Sleep(self.sb,3)
    #     balanceStr = 'span.mg-balance-value'
    #     self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
from classes.nesting.OneHundredElevenLightProductions import OneHundredElevenLightProductions
from classes.classUtilityFunctions import cleanNumber
from utilityFunctions import Sleep

slotCode = '111lightproductions-hearts-in-sync'
checkWordsList = ['free','spins','free spins','freespins']

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


    # def setup(self):
    #     self.clickBuyout()
    #     Sleep(self.sb)
    #     scatterStr = f'//div[contains(@class,"cards")]/div[{self.bonusOption}]/div[contains(@class,"card-body")]/button'
    #     self.sb.find_element(scatterStr).click()
    #     Sleep(self.sb)
    #     self.clickConfirm()

    # def run(self):
    #     self.timedScreenCheck(timeout=self.estimatedWaitTime,checkWordsList=checkWordsList,eleStr=self.canvasStr)

    # def findFinBal(self):
    #     self.defaultClick()
    #     Sleep(self.sb,3)
    #     balanceStr = 'span.mg-balance-value'
    #     self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
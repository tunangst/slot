from classes.nesting.OneHundredElevenLightProductions import OneHundredElevenLightProductions
from utilityFunctions import Sleep

slotCode = '111lightproductions-dragon-fortunes'
spinWords = ['free','spins','free spins']

class DragonFortunes(OneHundredElevenLightProductions):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 30
        self.bonusOption = 4
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,13)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        # Sleep(sb,15)
        # self.run()
        # Sleep(sb, self.estimatedWaitTime)
        self.checkFin(crop=slotCode,action='check end words',targetWordList=spinWords)
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()

    # def setup(self):
    #     self.clickBuyout()
    #     Sleep(self.sb)
    #     bonusCardStr = f'(//div[contains(@class,"cards")]/div[{self.bonusOption}]//button)'
    #     self.sb.find_element(bonusCardStr).click()
    #     Sleep(self.sb)
    #     self.clickConfirmBtn()

    # def run(self):
    #     self.sb.find_element(self.canvasStr).click()

    # def checkFin(self):
    #     ssNum = 1
    #     while True:
    #         # take screenshot 1
    #         picLocation1 = takePicture(sb=self.sb,action='increment', increment=ssNum)
    #         # change increment
    #         ssNum = (ssNum % 2) + 1
    #         Sleep(self.sb,10)
    #         # take screenshot 2
    #         picLocation2 = takePicture(sb=self.sb,action='increment',increment=ssNum)
    #         # change increment
    #         ssNum = (ssNum % 2) + 1
    #         # compare
    #         sameImg = compareImages(picLocation1,picLocation2,similarity=.95)
    #         # exit if they are the same
    #         if sameImg:
    #             return

    # def findFinBal(self):
    #     self.sb.find_element(self.canvasStr).click()
    #     Sleep(self.sb,3)
    #     balanceStr = 'span.mg-balance-value'
    #     self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
    #     self.finalBalance = self.endingBalance - self.startingBalance

    
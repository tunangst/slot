from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios
from utilityFunctions import Sleep

slotCode = '1000lakesstudios-bloom-em'
closingWords = ['total win']

class BloomEm(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 250
        self.estimatedWaitTime = 30
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

    # def setup(self):
    #     self.clickBuyout()
    #     self.runSleepOne()
    #     scatterStr = '//article[@data-offer-id="bonus3"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
    #     self.sb.find_element(scatterStr).click()
    #     self.runSleepOne()
    #     self.clickConfirmBtn()

    # def run(self):
    #     self.sb.find_element(self.canvasStr).click()

    # def findFinBal(self):
    #     self.sb.find_element(self.canvasStr).click()
    #     Sleep(self.sb,3)
    #     balanceStr = 'span.frame-hud__display-value'
    #     self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
    #     self.finalBalance = self.endingBalance - self.startingBalance
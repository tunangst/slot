from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios
from classes.classUtilityFunctions import cleanNumber
from utilityFunctions import Sleep

slotCode = '1000lakesstudios-flying-finns-1000'
# winningScreenshot = 'fin'
# closingWords = ['freespinsover']

class FlyingFinsOneThousand(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 500
        self.estimatedWaitTime = 30
        # self.canvasStr = 'canvas#game'
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,15)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        # Sleep(sb,3)
        # self.run()
        # Sleep(sb, self.estimatedWaitTime)
        self.checkFin(slotCode)
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()

    # def setup(self):
    #     self.clickBuyout()
    #     self.runSleepOne()
    #     scatterStr = '//article[@data-offer-id="super_buy"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
    #     self.sb.find_element(scatterStr).click()
    #     self.runSleepOne()
    #     self.clickConfirmBtn()

    # def run(self):
    #     self.sb.find_element(self.canvasStr).click()

    # def findFinBal(self):
    #     self.sb.find_element(self.canvasStr).click()
    #     Sleep(self.sb,5)
    #     balanceStr = 'span.frame-hud__display-value'
    #     self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
    #     self.finalBalance = self.endingBalance - self.startingBalance
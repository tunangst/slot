from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios
from classes.classUtilityFunctions import takePicture, cleanNumber
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '1000lakesstudios-twisted-candy-shop'
winningScreenshot = 'fin'
closingWords = ['total win', 'totalwin']

class TwistedCandyShop(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 500
        self.estimatedWaitTime = 180
        self.canvasStr = 'canvas#game'
        
        self.changeScene() # take the screen blocks off
        self.runSleepMain()
        self.passSplashScreen()
        self.runSleepThree()
        self.setup()
        self.runSleepFive()
        self.run()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin(closingWords)
        self.runSleepThree()
        self.findFinBal()

    def setup(self):
        self.clickBuyout()
        self.runSleepOne()
        scatterStr = '//article[@data-offer-id="buy_12fs"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        self.sb.find_element(scatterStr).click()
        self.runSleepOne()
        self.clickConfirmBtn()

    def run(self):
        self.sb.find_element(self.canvasStr).click()

    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,20)
        balanceStr = 'span.frame-hud__display-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios
from classes.classUtilityFunctions import cleanNumber
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '1000lakesstudios-bloom-em'
winningScreenshot = 'fin'
closingWords = ['total win']

class BloomEm(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 250
        self.estimatedWaitTime = 30
        self.canvasStr = 'canvas#game'
        
        self.changeScene() # take the screen blocks off
        self.runSleepThree()
        self.passSplashScreen()
        self.runSleepThree()
        self.setup()
        self.runSleepMain()
        self.run()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin(closingWords)
        self.runSleepFive()
        self.findFinBal()

    def setup(self):
        self.clickBuyout()
        self.runSleepOne()
        scatterStr = '//article[@data-offer-id="bonus3"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        self.sb.find_element(scatterStr).click()
        self.runSleepOne()
        self.clickConfirmBtn()

    def run(self):
        self.sb.find_element(self.canvasStr).click()

    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,3)
        balanceStr = 'span.frame-hud__display-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
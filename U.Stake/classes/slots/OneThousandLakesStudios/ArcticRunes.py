from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios
from classes.classUtilityFunctions import cleanNumber, takePicture
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '1000lakesstudios-arctic-runes'
winningScreenshot = 'fin'
closingWordsList = ['total win', 'totalwin']

class ArcticRunes(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 400
        self.estimatedWaitTime = 40
        self.canvasStr = 'canvas#game'
        # need to pass two splash screens
        self.changeScene() # take the screen blocks off
        self.runSleepFive()
        self.passSplashScreen()
        self.runSleepThree()
        self.setup()
        self.runSleepMain()
        self.run()
        Sleep(sb,self.estimatedWaitTime)
        self.checkFin(closingWordsList)
        self.runSleepThree()
        self.findFinBal()

    def setup(self):
        self.clickBuyout()
        self.runSleepOne()
        bonusCardStr = '//article[@data-offer-id="super_buy"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        self.sb.find_element(bonusCardStr).click()
        self.runSleepOne()
        self.clickConfirmBtn()

    def run(self):
        self.sb.find_element(self.canvasStr).click()        

    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,5)
        balanceStr = 'span.frame-hud__display-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
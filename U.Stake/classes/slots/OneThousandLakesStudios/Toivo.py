from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios
from classes.classUtilityFunctions import takePicture, clickDomElement, cleanNumber
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '1000lakesstudios-toivo'
winningScreenshot = 'fin'
closingWords = ['total win']

class Toivo(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 300
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
        self.runSleepThree()
        self.findFinBal()

    def passSplashScreen(self):
        bodyStr = 'body'
        self.sb.switch_to_frame('iframe')
        self.sb.find_element(bodyStr).click()
        Sleep(self.sb)
        skipStr = 'button.finnisher-intro__skip'
        self.sb.find_element(skipStr).click()

    def setup(self):
        self.clickBuyout()
        Sleep(self.sb)
        scatterStr = '//article[@data-offer-id="buy_super"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb)
        self.clickConfirmBtn()

    def run(self):
        clickDomElement(sb=self.sb,selector=self.canvasStr)

    def findFinBal(self):
        clickDomElement(sb=self.sb,selector=self.canvasStr)
        Sleep(self.sb,5)
        balanceStr = 'span.frame-hud__display-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
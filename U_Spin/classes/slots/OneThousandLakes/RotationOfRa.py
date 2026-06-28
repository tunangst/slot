from classes.nesting.OneThousandLakes import OneThousandLakes
from classes.classUtilityFunctions import cleanNumber
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '1000lakes-rotation-of-ra'
winningScreenshot = 'fin'
closingWordsList = ['totalwin','total win']

class RotationOfRa(OneThousandLakes):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 500
        self.estimatedWaitTime = 240
        self.canvasStr = 'canvas#game'
        # need to pass two splash screens
        self.changeScene() # take the screen blocks off
        self.runSleepThree()
        self.passSplashScreen()
        self.runSleepThree()
        self.setup()
        Sleep(sb,15)
        self.run()
        Sleep(sb,self.estimatedWaitTime)
        self.checkFin(closingWordsList)
        self.runSleepThree()
        self.findFinBal()
        
    def setup(self):
        self.setTurbo()
        self.runSleepOne()
        self.clickBuyout()
        self.runSleepOne()
        self.clickBonusCard()
        self.runSleepOne()
        self.clickConfirm()

    def run(self):
        self.sb.find_element(self.canvasStr).click()

    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()

        Sleep(self.sb,5)
        balanceStr = 'span.frame-hud__display-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
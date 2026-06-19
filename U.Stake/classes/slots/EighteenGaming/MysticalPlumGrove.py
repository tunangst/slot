from classes.nesting.EighteenGaming import EighteenGaming
from classes.classUtilityFunctions import cleanNumber, takePicture, findEmbeddedCoords, findCircles
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom, ClickTheDom
from selenium.webdriver.common.action_chains import ActionChains
import time

slotCode = '18gaming-mystical-plum-grove'
closingWordsList = ['conratulations','congratulations', 'cong', 'tions','ratulations']

class MysticalPlumGrove(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 60
        self.bonusOption = 4
        
        self.changeScene() # take the screen blocks off
        self.runSleepThree()
        self.passSplashScreen()
        self.runSleepThree()
        self.setup()
        self.runSleepMain()
        self.run()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin(closingWordsList)
        self.runSleepThree()
        self.findFinBal()

    def setup(self):
        self.clickBuyout()
        self.runSleepOne()
        self.clickBonusCard()
        self.runSleepOne()
        self.clickConfirmBtn()

    def run(self):
        canvas = self.sb.find_element(self.canvasStr)
        x = canvas.size['width'] * .60 # 60%
        y = canvas.size['height'] * .5 # 50%
        ClickTheDom(sb=self.sb,xVal=x,yVal=y)
        Sleep(self.sb,10)
        ClickTheDom(sb=self.sb,xVal=x,yVal=y)
         
    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,3)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
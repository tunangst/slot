from classes.nesting.EighteenGaming import EighteenGaming
from classes.classUtilityFunctions import cleanNumber, takePicture, findEmbeddedCoords, findCircles
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom, ClickTheDom
from selenium.webdriver.common.action_chains import ActionChains
import time

slotCode = '18gaming-santas-christmas-magic'
closingWordsList = ['conratulations','congratulations', 'cong', 'tions','ratulations']

class SantasChristmasMagic(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.estimatedWaitTime = 60
        
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
        self.setupAutoSpin()

    def run(self):
        self.sb.find_element(self.canvasStr).click()
         
    def checkFin(self):
        countStr = '//div[contains(@class,"icon-spin")]/div[contains(@class,"mg-stop-icon")]/span'
        stuck = False
        while True:
            try:
                checkCount = self.sb.find_element(countStr).text
                if checkCount == stuck:
                    canvas = self.sb.find_element(self.canvasStr)
                    x = canvas.size['width'] * .7 # 70%
                    y = canvas.size['height'] * .50 # 50%
                    # MarkTheDom(sb=self.sb,xVal=x,yVal=y)
                    ClickTheDom(sb=self.sb,xVal=x,yVal=y)
                    Sleep(self.sb,3)
                    ClickTheDom(sb=self.sb,xVal=x,yVal=y)
                stuck = checkCount
                print(checkCount)
                Sleep(self.sb,5)
            except:
                # after a free spins, there is a congratulations screen that blocks the spin count and will fall into this spot
                break

    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,3)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
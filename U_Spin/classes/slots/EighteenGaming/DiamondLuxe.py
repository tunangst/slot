from classes.nesting.EighteenGaming import EighteenGaming
from classes.classUtilityFunctions import cleanNumber, takePicture, findEmbeddedCoords, findCircles
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom, ClickTheDom
from selenium.webdriver.common.action_chains import ActionChains
import time

slotCode = '18gaming-diamond-luxe'
closingWordsList = ['conratulations','congratulations', 'cong', 'tions','ratulations']
scatterWordList = ['200.00']

class DiamondLuxe(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 30
        
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
        xScatter,yScatter = findEmbeddedCoords(sb=self.sb,checkWordList=scatterWordList)
        yScatter += 50 # add 50 px down for the btn
        ClickTheDom(sb=self.sb,xVal=xScatter,yVal=yScatter)
        self.runSleepOne()
        xAccept,yAccept = findEmbeddedCoords(sb=self.sb,checkWordList=scatterWordList)
        yAccept += 50 # add 50 px down for the btn
        ClickTheDom(sb=self.sb,xVal=xAccept,yVal=yAccept)

    def run(self):
        canvas = self.sb.find_element(self.canvasStr)
        x = canvas.size['width'] * .7 # 70%
        y = canvas.size['height'] * .50 # 50%
        ClickTheDom(sb=self.sb,xVal=x,yVal=y)
        Sleep(self.sb,10)
        ClickTheDom(sb=self.sb,xVal=x,yVal=y)
         
    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,3)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
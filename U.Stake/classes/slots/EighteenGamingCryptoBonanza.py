from classes.Slot import Slot
from classes.classUtilityFunctions import cleanNumber, takePicture, findEmbeddedCoords, findCircles
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom, ClickTheDom
from selenium.webdriver.common.action_chains import ActionChains
import time

slotCode = '18gaming-crypto-bonanza'
closingWordsList = ['conratulations','congratulations', 'cong', 'tions','ratulations']
checkWordsList = ['choose a coin']

class EighteenGamingCryptoBonanza(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 60
        self.canvasStr = 'canvas'
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb,15)
        self.run()
        # Sleep(sb, self.estimatedWaitTime)
        self.checkFin()
        Sleep(sb,3)
        self.findFinBal()

    def setup(self):
        countStr = '//div[contains(@class,"mg-right-container")]/div[contains(@class,"mg-action-autoplay")]/div[contains(@class,"mg-autoplay-icon")]'
        self.sb.find_element(countStr).click()
        Sleep(self.sb)
        numStr = '//li[contains(., "50")]'
        self.sb.find_element(numStr).click()
        Sleep(self.sb)
        autoStr = '//div[contains(@class,"mg-action-panel-container")]/div[contains(@class,"mg-action-play")]/div[contains(@class,"icon-spin")]/div[contains(@class,"mg-spin-autoplay-icon")]'
        self.sb.find_element(autoStr).click()

    def run(self):
        # self.sb.find_element(self.canvasStr).click()
        pass

    def checkFin(self):
        countStr = '//div[contains(@class,"icon-spin")]/div[contains(@class,"mg-stop-icon")]/span'
        stuck = False
        while True:
            try:
                checkCount = self.sb.find_element(countStr).text
                print(checkCount)
                Sleep(self.sb,5)
                if checkCount == stuck:
                    self.sb.find_element(self.canvasStr).click()
                stuck = checkCount
            except:
                # take pic,
                temp = takePicture(sb=self.sb,action='tmp')
                # check for free spins
                freeSpins = Capture(imageLocation=temp,action='check end words',targetWordList=checkWordsList)
                if freeSpins.fin:
                    canvas = self.sb.find_element(self.canvasStr)
                    x = canvas.size['width'] * .7 # 70%
                    y = canvas.size['height'] * .50 # 50%
                    ClickTheDom(sb=self.sb,xVal=x,yVal=y)
                    Sleep(self.sb,5)
                    ClickTheDom(sb=self.sb,xVal=x,yVal=y)
                # check for ends
                else:
                    endCheck = Capture(imageLocation=temp,action='check end words',targetWordList=closingWordsList)
                    if endCheck.fin:
                        self.sb.find_element(self.canvasStr).click()
                    else:
                        break
                # look for 
         
    def findFinBal(self):
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
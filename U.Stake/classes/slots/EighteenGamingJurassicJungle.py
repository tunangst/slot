from classes.Slot import Slot
from classes.classUtilityFunctions import cleanNumber, takePicture, findEmbeddedCoords, findCircles
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom, ClickTheDom
from selenium.webdriver.common.action_chains import ActionChains
import time

slotCode = '18gaming-jurassic-jungle'
closingWordsList = ['conratulations','congratulations', 'cong', 'tions','ratulations']

class EighteenGamingJurassicJungle(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.betValue = 1
        self.spinCount = 50
        self.estimatedWaitTime = 120
        self.canvasStr = 'canvas'
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb,15)
        self.run()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin()
        Sleep(sb,3)
        self.findFinBal()

    def setup(self):
        self.passTriangleScreen()
        Sleep(self.sb)
        autoStr = '//div[contains(@class,"mg-right-container")]/div[contains(@class,"mg-action-autoplay")]/div[contains(@class,"mg-autoplay-icon")]'
        self.sb.find_element(autoStr).click()
        Sleep(self.sb)
        countStr = f'//li[contains(., "{self.spinCount}")]'
        self.sb.find_element(countStr).click()
        Sleep(self.sb)
        btnStr = 'div.mg-action-play'
        self.sb.find_element(btnStr).click()

    def run(self):
        self.sb.find_element(self.canvasStr).click()

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
                break
         
    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,3)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
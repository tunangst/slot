from classes.Slot import Slot
from classes.classUtilityFunctions import cleanNumber, takePicture, findEmbeddedCoords, findCircles
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom, ClickTheDom
from selenium.webdriver.common.action_chains import ActionChains
import time

slotCode = '18gaming-legends-of-olympus'
closingWordsList = ['conratulations','congratulations', 'cong', 'tions','ratulations']

class EighteenGamingLegendsOfOlympus(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 30
        self.canvasStr = 'canvas'
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb,15)
        self.run()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin(closingWordsList)
        Sleep(sb,3)
        self.findFinBal()

    def setup(self):
        indexAdjustment = 1
        bonusStr = '//div[contains(@class,"mg-buy-circle")]'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        scatterStr = '//div[contains(@class,"bonus-cards")]/div[1]/div[contains(@class,"bonus-footer")]'
        self.sb.find_elements(scatterStr)[indexAdjustment].click()
        Sleep(self.sb)
        confirmStr = '//div[contains(@class,"confirm-btn")]'
        self.sb.find_elements(confirmStr)[indexAdjustment].click()

    def run(self):
        self.sb.find_element(self.canvasStr).click()
         
    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,3)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
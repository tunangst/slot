from classes.Slot import Slot
from classes.classUtilityFunctions import cleanNumber, takePicture, findEmbeddedCoords, findCircles
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom, ClickTheDom
from selenium.webdriver.common.action_chains import ActionChains
import time

slotCode = '18gaming-beachside-betties'
closingWordsList = ['conratulations','congratulations', 'cong', 'tions','ratulations']

class EighteenGamingBeachsideBetties(Slot):
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
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin(closingWordsList)
        Sleep(sb,3)
        self.findFinBal()

    def setup(self):
        multIndex = 1
        canvas = self.sb.find_element(self.canvasStr)
        x = canvas.size['width'] * .5 # 50%
        y = canvas.size['height'] * .80 # 80%
        ClickTheDom(sb=self.sb,xVal=x,yVal=y)
        Sleep(self.sb)
        bonusStr = '//div[contains(@class,"mg-buy-wrapper")]/div[contains(@class,"mg-buy")]/div[contains(@class,"mg-buy-circle")]'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        scatterStr = '//div[contains(@class,"bonus-cards")]/div[contains(@class,"bonus-card")]/div[contains(@class,"bonus-footer")]'
        self.sb.find_elements(scatterStr)[multIndex].click()
        Sleep(self.sb)
        confirmStr = '//div[contains(@class,"confirm-btn")]'
        self.sb.find_elements(confirmStr)[multIndex].click()

    def run(self):
        self.sb.find_element(self.canvasStr).click()
         
    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,3)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
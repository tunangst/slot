from classes.Slot import Slot
from classes.classUtilityFunctions import cleanNumber, takePicture, findEmbeddedCoords, findCircles
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom, ClickTheDom
from selenium.webdriver.common.action_chains import ActionChains
import time

slotCode = '18gaming-mystical-plum-grove'
closingWordsList = ['conratulations','congratulations', 'cong', 'tions','ratulations']

class EighteenGamingMysticalPlumGrove(Slot):
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
        cardIndex = 4
        bonusStr = '//div[contains(@class,"mg-buy-circle")]'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        scatterStr = f'//div[contains(@class,"cards")]/div[{cardIndex}]/div[contains(@class,"card-body")]/button'
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb)
        confirmStr = 'button.confirm-btn'
        self.sb.find_element(confirmStr).click()

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
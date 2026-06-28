from classes.nesting.EighteenGaming import EighteenGaming
from classes.classUtilityFunctions import cleanNumber, takePicture, findEmbeddedCoords, findCircles
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom, ClickTheDom
from selenium.webdriver.common.action_chains import ActionChains
import time

slotCode = '18gaming-toppings-tantalizer'
closingWordsList = ['conratulations','congratulations', 'cong', 'tions','ratulations']
spinWordsList = ['free spins']

class ToppingsTantalizer(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.estimatedWaitTime = 120
        
        self.changeScene() # take the screen blocks off
        self.runSleepThree()
        self.passSplashScreen()
        self.passTriangleScreen()
        self.runSleepThree()
        self.setup()
        self.runSleepMain()
        self.run()
        # Sleep(sb, self.estimatedWaitTime)
        self.checkAutoFin()
        self.runSleepThree()
        self.findFinBal()

    def setup(self):
        self.setupAutoSpin()

    def run(self):
        self.sb.find_element(self.canvasStr).click()
         
    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,3)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
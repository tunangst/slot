from classes.nesting.EighteenGaming import EighteenGaming
from classes.classUtilityFunctions import cleanNumber, takePicture, findEmbeddedCoords, findCircles
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom, ClickTheDom
from selenium.webdriver.common.action_chains import ActionChains
import time

slotCode = '18gaming-the-great-potato-war'
closingWordsList = ['conratulations','congratulations', 'cong', 'tions','ratulations']
checkWordsList = ['you won','free spins'] # congratulations
checkClosingWordsList = ['you won','total win']

# check for all words checkWordsList
# keep looping
# find a way to check free spins
# free spins and total win are on the canvas naturally
# take a pic and crop 50% to center?

class TheGreatPotatoWar(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 30
        
        self.changeScene() # take the screen blocks off
        self.runSleepThree()
        self.passSplashScreen()
        self.passTriangleScreen()
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
        self.clickBonusCardIncrement()
        self.runSleepOne()
        self.clickConfirmDivIncrement()

    def run(self):
        location = takePicture(sb=self.sb,action='tmp',eleStr=self.canvasStr,crop='mid-fifty')
        # Capture(imageLocation=location,action=)
        self.sb.find_element(self.canvasStr).click()
         
    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,3)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
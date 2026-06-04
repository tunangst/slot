from classes.Slot import Slot
from classes.classUtilityFunctions import takePicture, cleanNumber
from classes.Capture import Capture
from utilityFunctions import Sleep

slotCode = '0xedge-wild-zeus'
winningScreenshot = 'fin'
closingWords = ['gongratulations','congratulations']

class ZeroxEdgeWildZeus(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.startingBalance = 1000.00
        self.buyoutBalance = 500
        self.estimatedWaitTime = 80
        self.canvasStr = 'div.fs-content'
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,10)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb,3)
        self.run()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin(closingWords)
        Sleep(sb,3)
        self.findFinBal()

    def setup(self):
        bonusOption = 6
        bonusStr = '.bonus-outline-btn'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        scatterStr = f'(//div[contains(@class, "tiles-grid")]/div[{bonusOption}]//div[contains(@class, "tile-footer")]//button)[1]'
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb)
        yesStr = '.confirm-yes'
        self.sb.find_element(yesStr).click()

    def run(self):
        continueStr = '.fsi-tap'
        self.sb.find_element(continueStr).click()

    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb)
        balanceStr = '//div[contains(@class,"bar-left")]/div[contains(@class,"info-stack")]/div[contains(@class,"info-row")]/span[contains(@class,"info-value")]'
        balance = self.sb.find_element(balanceStr).text
        self.endingBalance = cleanNumber(balance)
        self.finalBalance = self.endingBalance - self.startingBalance
from classes.nesting.ZeroxEdge import ZeroxEdge
from classes.classUtilityFunctions import takePicture, cleanNumber
from classes.Capture import Capture
from utilityFunctions import Sleep

slotCode = '0xedge-wild-zeus'
winningScreenshot = 'fin'
closingWords = ['gongratulations','congratulations']

class WildZeus(ZeroxEdge):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 500
        self.estimatedWaitTime = 80
        self.bonusOption = 6
        self.canvasStr = 'div.fs-content'
        
        self.changeScene() # take the screen blocks off
        self.runSleepMain()
        self.passSplashScreen()
        self.runSleepThree()
        self.setup()
        self.runSleepThree()
        self.run()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin(closingWords)
        self.runSleepThree()
        self.findFinBal()

    def setup(self):
        self.clickBonus()
        self.runSleepOne()
        self.clickBonusCard()
        self.runSleepOne()
        self.clickConfirm()

    def run(self):
        continueStr = '.fsi-tap'
        self.sb.find_element(continueStr).click()

    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()
        self.runSleepOne()
        balanceStr = '//div[contains(@class,"bar-left")]/div[contains(@class,"info-stack")]/div[contains(@class,"info-row")]/span[contains(@class,"info-value")]'
        balance = self.sb.find_element(balanceStr).text
        self.endingBalance = cleanNumber(balance)
        self.finalBalance = self.endingBalance - self.startingBalance
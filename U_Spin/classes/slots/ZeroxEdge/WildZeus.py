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
        self.canvasStr = '//div[contains(@class,"game-container")]'
        self.canvasStr2 = '//div[contains(@class,"fs-content")]'
        self.counterStr = '//button[contains(@class,"play-btn-circle")]/span[contains(@class,"fs-btn-counter")]/span[contains(@class,"fs-btn-num") and not(contains(@class,"fs-btn-total"))]'
        self.checkEndFlag = False
        
        self.changeScene() # take the screen blocks off
        self.runSleepMain()
        self.passSplashScreen()
        self.runSleepThree()
        self.setup()
        self.runSleepThree()
        # self.run()
        # Sleep(sb, self.estimatedWaitTime)
        self.checkStart()
        self.checkFin()
        # self.checkFin(closingWords)
        self.runSleepThree()
        self.findFinBal()

    def setup(self):
        self.clickBonus()
        self.runSleepOne()
        self.clickBonusCard()
        self.runSleepOne()
        self.clickConfirm()

    def checkStart(self):
        while True:
            Sleep(self.sb,2)
            counterStatus = self.sb.is_element_present(self.counterStr)
            if counterStatus:
                self.sb.find_element(self.counterStr)
                break

            try:
                self.sb.find_element(self.canvasStr).click()
            except:
                self.sb.find_element(self.canvasStr2).click()

    def checkFin(self):
        Sleep(self.sb,2)
        while True:
            try:
                self.sb.find_element(self.canvasStr).click()
                counterNum = self.sb.find_element(self.counterStr).text
                self.checkEndFlag = False
            except:
                try:
                    self.sb.find_element(self.canvasStr).click()
                except:
                    self.sb.find_element(self.canvasStr2).click()
                if not self.checkEndFlag:
                    self.checkEndFlag = True
                else:
                    break

    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()
        self.runSleepOne()
        balanceStr = '//div[contains(@class,"bar-left")]/div[contains(@class,"info-stack")]/div[contains(@class,"info-row")]/span[contains(@class,"info-value")]'
        balance = self.sb.find_element(balanceStr).text
        self.endingBalance = cleanNumber(balance)
        self.finalBalance = self.endingBalance - self.startingBalance

    # def run(self):
    #     continueStr = '.fsi-tap'
    #     self.sb.find_element(continueStr).click()
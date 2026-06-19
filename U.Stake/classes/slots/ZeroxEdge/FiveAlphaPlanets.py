from classes.nesting.ZeroxEdge import ZeroxEdge
from classes.classUtilityFunctions import takePicture, compareImages, cleanNumber
from utilityFunctions import Sleep

slotCode = '0xedge-5-alpha-planets'

class FiveAlphaPlanets(ZeroxEdge):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 250
        self.estimatedWaitTime = 60
        self.bonusOption = 4
        
        self.changeScene() # take the screen blocks off
        self.runSleepFive()
        self.passSplashScreen()
        self.runSleepThree()
        self.setup()
        self.runSleepMain()
        self.run()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin()
        self.runSleepThree()
        self.findFinBal()

    def setup(self):
        bonusStr = 'button.bonus-x-btn'
        self.sb.find_element(bonusStr).click()
        self.runSleepOne()
        self.clickBonusCard()
        self.runSleepOne()
        self.clickConfirm()

    def run(self):
        continueStr = '.fsi-tap'
        self.sb.find_element(continueStr).click()

    def checkFin(self):
        ssNum = 1
        while True:
            # take screenshot 1
            picLocation1 = takePicture(sb=self.sb,action='increment', increment=ssNum)
            # change increment
            ssNum = (ssNum % 2) + 1
            Sleep(self.sb,10)
            # take screenshot 2
            picLocation2 = takePicture(sb=self.sb,action='increment',increment=ssNum)
            # change increment
            ssNum = (ssNum % 2) + 1
            # compare
            sameImg = compareImages(picLocation1,picLocation2)
            # exit if they are the same
            if sameImg:
                return

    def findFinBal(self):
        balanceStr = '//div[contains(@class,"bar-left")]/div[contains(@class,"info-stack")]/div[contains(@class,"info-row")]/span[contains(@class,"info-value")]'
        balance = self.sb.find_element(balanceStr).text
        self.endingBalance = cleanNumber(balance)
        self.finalBalance = self.endingBalance - self.startingBalance
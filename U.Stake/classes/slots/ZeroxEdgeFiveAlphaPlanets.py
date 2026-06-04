from classes.Slot import Slot
from classes.classUtilityFunctions import takePicture, compareImages, cleanNumber
from utilityFunctions import Sleep

slotCode = '0xedge-5-alpha-planets'

class ZeroxEdgeFiveAlphaPlanets(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.startingBalance = 1000.00
        self.buyoutBalance = 250
        self.estimatedWaitTime = 60
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,5)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb,10)
        self.run()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin()
        Sleep(sb,3)
        self.findFinBal()

    def setup(self):
        bonusOption = 4
        bonusStr = 'button.bonus-x-btn'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        scatterStr = f'(//div[contains(@class, "tiles-row")]/div[{bonusOption}]//div[contains(@class, "tile-body")]//button)[1]'
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb)
        yesStr = '.confirm-yes'
        self.sb.find_element(yesStr).click()

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
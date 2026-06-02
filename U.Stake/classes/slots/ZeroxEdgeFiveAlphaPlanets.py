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
        # need to pass two splash screens
        self.changeScene() # take the screen blocks off
        Sleep(self.sb,5)
        self.passSplashScreen()
        self.setup()
        self.run()

    def setup(self):
        # click bonus
        bonusOption = 4
        bonusStr = 'button.bonus-x-btn'
        self.sb.find_element(bonusStr).click()
        # choose scatter
        scatterStr = f'(//div[contains(@class, "tiles-row")]/div[{bonusOption}]//div[contains(@class, "tile-body")]//button)[1]'
        self.sb.find_element(scatterStr).click()
        yesStr = '.confirm-yes'
        self.sb.find_element(yesStr).click()

    def run(self):
        Sleep(self.sb,10)
        # find play btn
        continueStr = '.fsi-tap'
        self.sb.find_element(continueStr).click()

        # find a way to trigger checkFin
        # read reoccur screenshots to look for " click to continue "
        Sleep(self.sb, self.estimatedWaitTime)
        self.checkFin()
        # find what was won
        self.findFinBal()

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
        # value = self.sb.get_text('span.info-value')
        # self.winnings = cleanNumber(value)
        balanceStr = '//div[contains(@class,"bar-left")]/div[contains(@class,"info-stack")]/div[contains(@class,"info-row")]/span[contains(@class,"info-value")]'
        balance = self.sb.find_element(balanceStr).text
        self.endingBalance = cleanNumber(balance)
        self.finalBalance = self.endingBalance - self.startingBalance
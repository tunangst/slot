from classes.Slot import Slot
from classes.classUtilityFunctions import takePicture, cleanNumber
from classes.Capture import Capture
from utilityFunctions import Sleep

slotCode = '0xedge-wild-zeus'
winningScreenshot = 'fin'

class ZeroxEdgeWildZeus(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.startingBalance = 1000.00
        self.buyoutBalance = 500
        self.estimatedWaitTime = 80
        self.closingWords = ['gongratulations','congratulations']
        # can find "congratulations" to end the searching
        self.changeScene() # take the screen blocks off
        Sleep(self.sb,10)
        self.passSplashScreen()
        Sleep(self.sb,3)
        self.setup()
        Sleep(self.sb,3)
        self.run()
        # while check for same screenshots to see if game ended
        # record ending balance

    def setup(self):
        # click bonus
        Sleep(self.sb)
        bonusOption = 6
        bonusStr = '.bonus-outline-btn'
        self.sb.find_element(bonusStr).click()
        # choose scatter
        scatterStr = f'(//div[contains(@class, "tiles-grid")]/div[{bonusOption}]//div[contains(@class, "tile-footer")]//button)[1]'
        self.sb.find_element(scatterStr).click()
        yesStr = '.confirm-yes'
        self.sb.find_element(yesStr).click()
        self.sb.sleep(10)

    def run(self):
        # find play btn
        continueStr = '.fsi-tap'
        self.sb.find_element(continueStr).click()

        # find a way to trigger checkFin
        # read reoccur screenshots to look for " click to continue "
        Sleep(self.sb, self.estimatedWaitTime)
        self.checkFin(self.closingWords)
        # get winning capture
        self.findFinBal()

    def findFinBal(self):
        # picLocation = takePicture(sb=self.sb,action='custom',fileName=winningScreenshot)
        # cap = Capture(imageLocation=picLocation,action='find number')
        # winStr = cap.status
        # self.winnings = cleanNumber(winStr)
        canvasStr = 'div.fs-content'
        self.sb.find_element(canvasStr).click()
        # div.bar-left > div.info-stack > div.info-row > span.info-value
        balanceStr = '//div[contains(@class,"bar-left")]/div[contains(@class,"info-stack")]/div[contains(@class,"info-row")]/span[contains(@class,"info-value")]'
        balance = self.sb.find_element(balanceStr).text
        self.endingBalance = cleanNumber(balance)
        self.finalBalance = self.endingBalance - self.startingBalance

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
        self.estimatedWaitTime = 80
        self.closingWords = ['gongratulations','congratulations']
        # can find "congratulations" to end the searching
        self.changeScene() # take the screen blocks off
        self.passSplashScreen()
        self.setup()
        # run
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
        self.findWinnings()

    def findWinnings(self):
        picLocation = takePicture(sb=self.sb,action='custom',fileName=winningScreenshot)
        cap = Capture(imageLocation=picLocation,action='find number')
        winStr = cap.status
        self.winnings = cleanNumber(winStr)
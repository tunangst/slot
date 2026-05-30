from classes.Slot import Slot
from classes.classUtilityFunctions import takePicture, compareImages, cleanNumber
from utilityFunctions import Sleep

slotCode = '0xedge-super-candy-drop'

class ZeroxEdgeSuperCandyDrop(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.startingBalance = 1000.00
        self.estimatedWaitTime = 35
        # need to pass two splash screens
        self.changeScene() # take the screen blocks off
        self.passSplashScreen()
        self.setup()
        self.run()
        # while check for same screenshots to see if game ended
        # record ending balance

    def passSplashScreen(self):
        Sleep(self.sb)
        str = 'body'
        self.sb.switch_to_frame('iframe')
        self.sb.find_element(str).click()
        Sleep(self.sb)
        self.sb.find_element(str).click()

    def setup(self):
        # click bonus
        bonusOption = 6
        bonusStr = '.bonus-outline-btn'
        self.sb.find_element(bonusStr).click()
        # choose scatter
        Sleep(self.sb)
        scatterStr = f'(//div[contains(@class, "tiles-grid")]/div[{bonusOption}]//div[contains(@class, "tile-body")]//button)[1]'
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb)
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
        self.findWinnings()

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

    def findWinnings(self):
        value = self.sb.get_text('span.info-value.win')
        filteredVal = cleanNumber(value)
        self.winnings = filteredVal

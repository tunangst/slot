from classes.Slot import Slot
from classes.classUtilityFunctions import cleanNumber
from utilityFunctions import Sleep

slotCode = '0xedge-do-not-redeem-it'

class ZeroxEdgeDoNotRedeemIt(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.startingBalance = 1000.00
        self.estimatedWaitTime = 60
        self.betValue = 1
        self.spinCount = 50
        # need to pass two splash screens
        self.changeScene() # take the screen blocks off
        self.passSplashScreen()
        self.setup()
        self.run()

    def setup(self):
        Sleep(self.sb)
        hasteStr = 'button[aria-label="Turbo mode"]'
        self.sb.find_element(hasteStr).click()

        autoPlayStr = 'button[aria-label="Autoplay"]'
        self.sb.find_element(autoPlayStr).click()
        # choose scatter
        startBtn = 'button.start-btn'
        self.sb.find_element(startBtn).click()
        yesStr = '.confirm-yes'
        self.sb.find_element(yesStr).click()

    def run(self):
        Sleep(self.sb, self.estimatedWaitTime)
        self.checkFin()
        # find what was won
        self.findWinnings()

    def checkFin(self):
        # find autoplay count and break when the element goes invisible
        autoPlayCountStr = 'span.autoplay-count'
        killSwitch = True
        ssNum = 1
        while killSwitch:
            Sleep(self.sb,10)
            # check if counts are present
            countIsPresent = self.sb.is_element_visible(autoPlayCountStr)
            if not countIsPresent:
                return

    def findWinnings(self):
        spanStr = 'span.info-value'
        txtNum = self.sb.get_text(spanStr)
        value = cleanNumber(txtNum)
        self.winnings = self.betValue * self.spinCount + value

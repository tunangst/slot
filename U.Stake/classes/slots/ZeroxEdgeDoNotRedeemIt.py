from classes.Slot import Slot
from classes.classUtilityFunctions import cleanNumber
from utilityFunctions import Sleep

slotCode = '0xedge-do-not-redeem-it'

class ZeroxEdgeDoNotRedeemIt(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.estimatedWaitTime = 60
        self.betValue = 1
        self.spinCount = 50
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        # Sleep(self.sb,3)
        # self.run()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin()
        Sleep(sb,3)
        self.findFinBal()

    def setup(self):
        hasteStr = 'button[aria-label="Turbo mode"]'
        self.sb.find_element(hasteStr).click()
        Sleep(self.sb)
        autoPlayStr = 'button[aria-label="Autoplay"]'
        self.sb.find_element(autoPlayStr).click()
        Sleep(self.sb)
        startBtn = 'button.start-btn'
        self.sb.find_element(startBtn).click()
        Sleep(self.sb)
        yesStr = '.confirm-yes'
        self.sb.find_element(yesStr).click()

    def run(self):
        pass

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

    def findFinBal(self):
        spanStr = 'span.info-value'
        txtNum = self.sb.get_text(spanStr)
        self.endingBalance = cleanNumber(txtNum)
        self.finalBalance = self.endingBalance - self.startingBalance
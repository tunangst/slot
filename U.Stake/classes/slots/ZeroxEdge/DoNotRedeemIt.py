from classes.nesting.ZeroxEdge import ZeroxEdge
from classes.classUtilityFunctions import cleanNumber
from utilityFunctions import Sleep

slotCode = '0xedge-do-not-redeem-it'

class DoNotRedeemIt(ZeroxEdge):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.estimatedWaitTime = 60
        
        self.changeScene() # take the screen blocks off
        self.runSleepThree()
        self.passSplashScreen()
        self.runSleepThree()
        self.setup()
        # Sleep(self.sb,3)
        # self.run()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin()
        self.runSleepThree()
        self.findFinBal()

    def setup(self):
        self.clickTurbo()
        self.runSleepOne()
        self.clickAuto()
        self.runSleepOne()
        self.clickStart()
        self.runSleepOne()
        self.clickConfirm()

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
from classes.nesting.ZeroxEdge import ZeroxEdge
from classes.classUtilityFunctions import cleanNumber
from utilityFunctions import Sleep

slotCode = '0xedge-do-not-redeem-it'

class DoNotRedeemIt(ZeroxEdge):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.estimatedWaitTime = 60
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin()
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()

    def setup(self):
        self.clickTurbo()
        Sleep(self.sb)
        self.clickAuto()
        Sleep(self.sb)
        self.clickStart()
        Sleep(self.sb)
        self.clickConfirm()

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
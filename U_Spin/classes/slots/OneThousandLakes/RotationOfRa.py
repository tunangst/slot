from classes.nesting.OneThousandLakes import OneThousandLakes
from classes.classUtilityFunctions import cleanNumber
from utilityFunctions import Sleep

slotCode = '1000lakes-rotation-of-ra'

class RotationOfRa(OneThousandLakes):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 500
        self.estimatedWaitTime = 240

        self.changeScene() # take the screen blocks off
        self.findSplashLoaded()
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        self.checkFin(crop=slotCode)
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()
        
    def setup(self):
        self.setTurbo()
        Sleep(self.sb)
        self.clickBuyout()
        Sleep(self.sb)
        self.clickBonusCard()
        Sleep(self.sb)
        self.clickConfirm()

    def findFinBal(self):
        self.defaultClick()
        Sleep(self.sb,5)
        balanceStr = 'span.frame-hud__display-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)

from classes.nesting.OneThousandLakes import OneThousandLakes
from classes.classUtilityFunctions import cleanNumber
from utilityFunctions import Sleep

slotCode = '1000lakes-rotation-of-ra'
winningScreenshot = 'fin'
closingWordsList = ['totalwin','total win']

class RotationOfRa(OneThousandLakes):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 500
        self.estimatedWaitTime = 240

        self.changeScene() # take the screen blocks off
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb,15)
        self.run()
        Sleep(sb,self.estimatedWaitTime)
        self.checkFin(closingWordsList)
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

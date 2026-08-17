from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios
from classes.classUtilityFunctions import cleanNumber, findEmbeddedCoords
from utilityFunctions import Sleep, ClickTheDom

slotCode = '1000lakesstudios-toivo'
continueStr = ['continue']

class Toivo(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 300
        self.estimatedWaitTime = 30
        self.introSkipStr = '//button[contains(@class,"finnisher-intro__skip")]'

        self.changeScene() # take the screen blocks off
        Sleep(sb,5)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb,15)
        self.run()
        self.checkFin(crop=slotCode)
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()

    def passSplashScreen(self):
        self.sb.switch_to_frame('iframe')
        Sleep(self.sb,3)
        self.defaultClick()
        Sleep(self.sb,3)
        self.sb.find_element(self.introSkipStr).click()

    def run(self):
        clickX,clickY = findEmbeddedCoords(sb=self.sb,checkWordList=continueStr)
        ClickTheDom(sb=self.sb,xVal=clickX,yVal=clickY)

    def findFinBal(self):
        self.run()
        Sleep(self.sb,3)   
        self.endingBalance = cleanNumber(self.sb.find_element(self.balanceStr).text)
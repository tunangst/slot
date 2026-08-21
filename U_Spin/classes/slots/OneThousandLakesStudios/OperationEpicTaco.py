from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios
from utilityFunctions import Sleep

slotCode = '1000lakesstudios-operation-epic-taco'

class OperationEpicTaco(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 500
        self.estimatedWaitTime = 60
        
        self.changeScene() # take the screen blocks off
        self.findSplashLoaded()
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        self.checkFin()
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()

    def checkFin(self):
        # make sure the spin starts
        while not self.sb.is_element_present(self.counterStr):
            Sleep(self.sb,2)
            self.defaultClick()
        # find when the spin finishes
        while not self.sb.is_element_present(self.spinStr):
            Sleep(self.sb,2)
            self.defaultClick()
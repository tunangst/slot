from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios
from utilityFunctions import Sleep

slotCode = '1000lakesstudios-disco-cubes'

class DiscoCubes(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 500
        self.estimatedWaitTime = 90
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,15)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        self.checkFin()
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()

    def checkFin(self):
            startSwitch = False
            endSwitch = 0 # 0-3
            endSwitchLimit = 1
            while True:
                self.defaultClick()
                Sleep(self.sb,3)
                if self.sb.is_element_present(self.counterStr):
                    startSwitch = True
                elif endSwitch >= endSwitchLimit:
                    break
                elif startSwitch:
                    endSwitch += 1
                else:
                    print('checkfin might not have started yet')
from classes.nesting.ZeroxEdge import ZeroxEdge
from utilityFunctions import Sleep

slotCode = '0xedge-5-alpha-planets'

class FiveAlphaPlanets(ZeroxEdge):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.bonusOption = 4
        self.run()

    def run(self):
        self.changeScene() # take the screen blocks off
        self.findSplashLoaded()
        Sleep(self.sb,3)
        self.passSplashScreen()
        Sleep(self.sb,3)
        self.setup()
        self.checkFin(crop=slotCode)
        Sleep(self.sb,3)
        self.findFinBal()
        self.calculateWinnings()
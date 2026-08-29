from classes.nesting.EighteenGaming import EighteenGaming
from classes.classUtilityFunctions import findEmbeddedCoords
from utilityFunctions import Sleep, ClickTheDom

slotCode = '18gaming-diamond-luxe'
scatterWordList = ['200.00']

class DiamondLuxe(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        # self.buyoutBalance = 200
        # self.estimatedWaitTime = 30
        self.run()

    def setup(self):
        self.clickBuyout()
        Sleep(self.sb)
        self.xScatter,self.yScatter = findEmbeddedCoords(sb=self.sb,checkWordList=scatterWordList)
        self.yScatter += 50 # add 50 px down for the btn
        ClickTheDom(sb=self.sb,xVal=self.xScatter,yVal=self.yScatter)
        Sleep(self.sb)
        xAccept,yAccept = findEmbeddedCoords(sb=self.sb,checkWordList=scatterWordList)
        yAccept += 50 # add 50 px down for the btn
        ClickTheDom(sb=self.sb,xVal=xAccept,yVal=yAccept)

    def defaultClick(self):
        if self.xScatter > 0:
            ClickTheDom(sb=self.sb,xVal=self.xScatter,yVal=self.yScatter)
        else:
            super().defaultClick()
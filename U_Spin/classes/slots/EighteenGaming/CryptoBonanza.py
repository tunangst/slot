from classes.nesting.EighteenGaming import EighteenGaming
from utilityFunctions import ClickTheDom

slotCode = '18gaming-crypto-bonanza'

class CryptoBonanza(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.x = self.y = 0        
        self.run()

    def setup(self):
        canvas = self.sb.find_element('canvas')
        self.x = int(canvas.size['width'] * .6)
        self.y = int(canvas.size['height'] * .5)
        self.setupAutoSpin()

    def defaultClick(self):
        ClickTheDom(sb=self.sb,xVal=self.x,yVal=self.y)
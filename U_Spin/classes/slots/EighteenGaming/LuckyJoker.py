from classes.nesting.EighteenGaming import EighteenGaming
from utilityFunctions import ClickTheDom

slotCode = '18gaming-lucky-joker'

class LuckyJoker(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.run()

    def setup(self):
        self.setupAutoSpin()
        # needed for bonus game
        canvas = self.sb.find_element('canvas')
        canvasWidth = canvas.size['width']
        canvasHeight = canvas.size['height']
        pt1x = canvasWidth * .3
        pt2x = canvasWidth * .4
        pt3x = canvasWidth * .5
        pt4x = canvasWidth * .6
        pt5x = canvasWidth * .7
        pty = canvasHeight * .5
        self.pt1 =(pt1x,pty)
        self.pt2 =(pt2x,pty)
        self.pt3 =(pt3x,pty)
        self.pt4 =(pt4x,pty)
        self.pt5 =(pt5x,pty)

    def defaultClick(self):
        ClickTheDom(sb=self.sb,xVal=self.pt1[0],yVal=self.pt1[1])
        ClickTheDom(sb=self.sb,xVal=self.pt2[0],yVal=self.pt2[1])
        ClickTheDom(sb=self.sb,xVal=self.pt3[0],yVal=self.pt3[1])
        ClickTheDom(sb=self.sb,xVal=self.pt4[0],yVal=self.pt4[1])
        ClickTheDom(sb=self.sb,xVal=self.pt5[0],yVal=self.pt5[1])
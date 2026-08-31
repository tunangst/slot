from classes.nesting.EighteenGaming import EighteenGaming
from utilityFunctions import ClickTheDom

slotCode = '18gaming-mystical-plum-grove'

class MysticalPlumGrove(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.x = self.y = 0
        self.bonusOption = 4
        self.run()

    def defaultClick(self):
        if self.x > 0 and self.y > 0:
            ClickTheDom(sb=self.sb,xVal=self.x,yVal=self.y)
        else:
            canvas = self.sb.find_element(self.canvasStr)
            self.x = int(canvas.size['width'] * .60) # 60%
            self.y = int(canvas.size['height'] * .5) # 50%
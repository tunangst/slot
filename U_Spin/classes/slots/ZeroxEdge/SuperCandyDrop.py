from classes.nesting.ZeroxEdge import ZeroxEdge

slotCode = '0xedge-super-candy-drop'

class SuperCandyDrop(ZeroxEdge):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.bonusOption = 5
        self.run()
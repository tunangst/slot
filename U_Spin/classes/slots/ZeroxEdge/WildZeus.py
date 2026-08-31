from classes.nesting.ZeroxEdge import ZeroxEdge

slotCode = '0xedge-wild-zeus'

class WildZeus(ZeroxEdge):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.bonusOption = 6
        self.run()
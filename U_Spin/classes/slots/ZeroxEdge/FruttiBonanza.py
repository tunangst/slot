from classes.nesting.ZeroxEdge import ZeroxEdge

slotCode = '0xedgefrutti-bonanza'

class FruttiBonanza(ZeroxEdge):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.bonusOption = 7
        self.run()
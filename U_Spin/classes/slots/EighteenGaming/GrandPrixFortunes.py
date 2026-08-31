from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-grand-prix-fortunes'

class GrandPrixFortunes(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.run()
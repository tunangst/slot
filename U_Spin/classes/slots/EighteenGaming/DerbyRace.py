from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-derby-race'

class DerbyRace(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.run()

    def setup(self):
        self.setupAutoSpin()
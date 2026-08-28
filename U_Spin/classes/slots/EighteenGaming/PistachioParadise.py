from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-pistachio-paradise'

class PistachioParadise(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.estimatedWaitTime = 60

        self.run()

    def setup(self):
        self.setupAutoSpin()
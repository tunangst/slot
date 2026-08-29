from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-phoenix-winter-parade'

class PhoenixWinterParade(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.estimatedWaitTime = 120

        self.run()
        
    def setup(self):
        self.setupAutoSpin()
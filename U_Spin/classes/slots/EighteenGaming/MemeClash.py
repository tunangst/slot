from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-meme-clash'

class MemeClash(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 60
        
        self.run()

    def setup(self):
        self.setupAutoSpin()
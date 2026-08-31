from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-meme-clash'

class MemeClash(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.run()

    def setup(self):
        self.setupAutoSpin()
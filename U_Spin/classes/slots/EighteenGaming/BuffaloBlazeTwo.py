from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-buffalo-blaze-2'

class BuffaloBlazeTwo(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.bonusOption = 4
        self.run()
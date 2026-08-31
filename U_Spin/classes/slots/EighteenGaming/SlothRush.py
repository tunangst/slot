from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-sloth-rush'

class SlothRush(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.run()
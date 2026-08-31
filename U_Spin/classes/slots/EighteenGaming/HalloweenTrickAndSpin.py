from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-halloween-trick-and-spin'

class HalloweenTrickAndSpin(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.run()
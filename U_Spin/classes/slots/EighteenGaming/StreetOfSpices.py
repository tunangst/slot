from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-street-of-spices'

class StreetOfSpices(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 30

        self.run()
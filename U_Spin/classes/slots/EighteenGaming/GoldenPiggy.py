from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-golden-piggy'

class GoldenPiggy(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 60
        self.bonusOption = 3

        self.run()
from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-wall-street-honey-stakes'

class WallStreetHoneyStakes(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 40

        self.run()
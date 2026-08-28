from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-wrath-of-olympus'

class WrathOfOlympus(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 60
        
        self.run()
from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-the-great-potato-war'

class TheGreatPotatoWar(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 100
        self.estimatedWaitTime = 30
        
        self.run()
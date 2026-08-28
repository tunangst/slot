from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-sushi-jet-dash'

class SushiJetDash(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 30

        self.run()
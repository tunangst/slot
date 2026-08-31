from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-rock-n-roll'

class RockNRoll(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.bonusOption = 3
        self.run()
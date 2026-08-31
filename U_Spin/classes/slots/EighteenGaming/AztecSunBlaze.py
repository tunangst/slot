from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-aztec-sun-blaze'

class AztecSunBlaze(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.bonusOption = 4
        self.run()
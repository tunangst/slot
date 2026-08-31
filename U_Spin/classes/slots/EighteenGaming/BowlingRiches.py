from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-bowling-riches'

class BowlingRiches(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.bonusOption = 2
        self.run()
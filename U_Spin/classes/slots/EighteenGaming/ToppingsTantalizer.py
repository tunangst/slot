from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-toppings-tantalizer'

class ToppingsTantalizer(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.run()

    def setup(self):
        self.setupAutoSpin()
from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-zombie-harvest'

class ZombieHarvest(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.run()
from classes.nesting.EighteenGaming import EighteenGaming

slotCode = '18gaming-kill-the-bill'

class KillTheBill(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.run()
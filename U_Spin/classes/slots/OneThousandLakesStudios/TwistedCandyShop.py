from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios

slotCode = '1000lakesstudios-twisted-candy-shop'

class TwistedCandyShop(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.run()
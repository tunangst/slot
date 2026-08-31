from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios

slotCode = '1000lakesstudios-yakuza-v-i-p'

class YakuzaVIP(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.run()
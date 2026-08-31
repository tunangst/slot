from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios

slotCode = '1000lakesstudios-arctic-runes'

class ArcticRunes(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.run()
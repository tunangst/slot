from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios

slotCode = '1000lakesstudios-flying-finns-1000'

class FlyingFinsOneThousand(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.run()
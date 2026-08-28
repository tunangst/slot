from classes.nesting.OneHundredElevenLightProductions import OneHundredElevenLightProductions

slotCode = '111lightproductions-dragon-fortunes'

class DragonFortunes(OneHundredElevenLightProductions):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 30
        self.bonusOption = 4
        
        self.run()
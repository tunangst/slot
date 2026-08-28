from classes.nesting.OneHundredElevenLightProductions import OneHundredElevenLightProductions

slotCode = '111lightproductions-legends-of-the-lost-grove'

class LegendsOfTheLostGrove(OneHundredElevenLightProductions):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 100
        self.estimatedWaitTime = 30
        self.bonusOption = 3
        
        self.run()
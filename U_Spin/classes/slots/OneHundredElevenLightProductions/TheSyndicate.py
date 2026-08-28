from classes.nesting.OneHundredElevenLightProductions import OneHundredElevenLightProductions

slotCode = '111lightproductions-the-syndicate'

class TheSyndicate(OneHundredElevenLightProductions):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.estimatedWaitTime = 30
        self.buyoutBalance = 200
        self.bonusOption = 3
        
        self.run()
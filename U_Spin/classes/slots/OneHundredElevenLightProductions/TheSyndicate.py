from classes.nesting.OneHundredElevenLightProductions import OneHundredElevenLightProductions

slotCode = '111lightproductions-the-syndicate'

class TheSyndicate(OneHundredElevenLightProductions):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.bonusOption = 3
        self.run()
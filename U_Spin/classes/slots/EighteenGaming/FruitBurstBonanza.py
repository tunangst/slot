from classes.nesting.EighteenGaming import EighteenGaming
from utilityFunctions import GetRandomNumber

slotCode = '18gaming-fruit-burst-bonanza'
bonusArr = [100,70,111,112,42]

class FruitBurstBonanza(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.bonusInd = GetRandomNumber(len(bonusArr)-1)
        self.buyoutBalance = bonusArr[self.bonusInd]
        self.bonusOption = self.bonusInd + 1

        count = 4
        while count > 0:
            count -=1
            self.run()
            self.bonusInd = GetRandomNumber(len(bonusArr)-1)
            self.buyoutBalance = bonusArr[self.bonusInd]
            self.bonusOption = self.bonusInd + 1
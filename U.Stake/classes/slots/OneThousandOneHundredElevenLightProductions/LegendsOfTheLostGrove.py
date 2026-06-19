from classes.nesting.OneThousandOneHundredElevenLightProductions import OneThousandOneHundredElevenLightProductions
from classes.classUtilityFunctions import cleanNumber, takePicture
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '111lightproductions-legends-of-the-lost-grove'
winningScreenshot = 'fin'
closingWordsList = ['conratulations','congratulations', 'cong', 'tions','ratulations']
nextWordList = ['youwon','you won', 'won', 'you']

class LegendsOfTheLostGrove(OneThousandOneHundredElevenLightProductions):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 100
        self.estimatedWaitTime = 30
        self.canvasStr = 'canvas#game'
        self.bonusOption = 3
        
        self.changeScene() # take the screen blocks off
        self.runSleepFive()
        self.passSplashScreen()
        self.runSleepThree()
        self.setup()
        self.runSleepTwenty()
        self.run()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin(closingWordsList)
        self.runSleepThree()
        self.findFinBal()

    def setup(self):
        self.clickBuyout()
        self.runSleepOne()
        scatterStr = f'//div[contains(@class,"cards")]/div[{self.bonusOption}]/div[contains(@class,"card-body")]/button'
        self.sb.find_element(scatterStr).click()
        self.runSleepOne()
        self.clickConfirmBtn()

    def run(self):
        self.sb.find_element(self.canvasStr).click()

    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,3)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance

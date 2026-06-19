from classes.nesting.OneThousandOneHundredElevenLightProductions import OneThousandOneHundredElevenLightProductions
from classes.classUtilityFunctions import cleanNumber, takePicture
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '111lightproductions-hearts-in-sync'
winningScreenshot = 'fin'
closingWordsList = ['total win','totalwin']
checkWordsList = ['free spins','freespins']
nextWordList = ['youwon','you won', 'won', 'you']

class HeartsInSync(OneThousandOneHundredElevenLightProductions):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 90
        self.canvasStr = 'canvas#game'
        self.bonusOption = 3
        
        self.changeScene() # take the screen blocks off
        self.runSleepThree()
        self.passSplashScreen()
        self.runSleepThree()
        self.setup()
        self.runSleepTwenty()
        self.run()
        self.runSleepThree()
        self.checkFin(closingWordsList=closingWordsList,eleStr=self.canvasStr)
        self.runSleepOne()
        self.findWinnings()

    def setup(self):
        self.clickBuyout()
        self.runSleepOne()
        scatterStr = f'//div[contains(@class,"cards")]/div[{self.bonusOption}]/div[contains(@class,"card-body")]/button'
        self.sb.find_element(scatterStr).click()
        self.runSleepOne()
        self.clickConfirmBtn()

    def run(self):
        self.timedScreenCheck(timeout=self.estimatedWaitTime,checkWordsList=checkWordsList,eleStr=self.canvasStr)

    def findWinnings(self):
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,3)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
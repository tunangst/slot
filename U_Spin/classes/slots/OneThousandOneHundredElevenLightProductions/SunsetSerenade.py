from classes.nesting.OneThousandOneHundredElevenLightProductions import OneThousandOneHundredElevenLightProductions
from classes.classUtilityFunctions import cleanNumber, takePicture
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '111lightproductions-sunset-serenade'
winningScreenshot = 'fin'
closingWordsList = ['conratulations','congratulations', 'cong', 'tions','ratulations']
nextWordList = ['youwon','you won', 'won', 'you']

class SunsetSerenade(OneThousandOneHundredElevenLightProductions):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 30
        self.canvasStr = 'canvas#game'

        self.changeScene() # take the screen blocks off
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb,10)
        # self.run()
        # Sleep(sb, self.estimatedWaitTime)
        self.checkFin(locLabel='top-mid-left')
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()

    def setup(self):
        self.clickBuyout()
        Sleep(self.sb)
        self.clickBonusCard()
        Sleep(self.sb)
        self.clickConfirm()

    def run(self):
        self.defaultClick()

    def findFinBal(self):
        self.defaultClick()
        Sleep(self.sb,3)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
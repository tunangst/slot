from classes.nesting.OneThousandOneHundredElevenLightProductions import OneThousandOneHundredElevenLightProductions
from classes.classUtilityFunctions import cleanNumber, takePicture
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '111lightproductions-the-syndicate'
winningScreenshot = 'fin'
closingWordsList = ['you won','youwon']
spinWords = ['free spins','free','spins']

class TheSyndicate(OneThousandOneHundredElevenLightProductions):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.estimatedWaitTime = 30
        self.buyoutBalance = 200
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb,15)
        # self.run()
        # Sleep(sb, self.estimatedWaitTime)
        self.checkFin(locLabel='top-third',action='check end words',targetWordList=spinWords)
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()

    def setup(self):
        self.clickBuyout()
        Sleep(self.sb)
        confirmBtnStr = '//button[contains(@class,"buy")]'
        self.sb.find_element(confirmBtnStr).click()
        Sleep(self.sb)
        self.clickConfirm()

    def run(self):
        self.defaultClick()

    def findFinBal(self):
        self.defaultClick()
        Sleep(self.sb,3)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
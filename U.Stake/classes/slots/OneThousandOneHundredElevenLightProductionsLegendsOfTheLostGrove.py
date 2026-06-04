from classes.Slot import Slot
from classes.classUtilityFunctions import cleanNumber, takePicture
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '111lightproductions-legends-of-the-lost-grove'
winningScreenshot = 'fin'
closingWordsList = ['conratulations','congratulations', 'cong', 'tions','ratulations']
nextWordList = ['youwon','you won', 'won', 'you']

class OneThousandOneHundredElevenLightProductionsLegendsOfTheLostGrove(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 100
        self.estimatedWaitTime = 30
        self.canvasStr = 'canvas#game'
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,7)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb,17)
        self.run()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin(closingWordsList)
        Sleep(sb,3)
        self.findFinBal()

    def setup(self):
        bonusStr = 'div.mg-buy-circle'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        scatterStr = '//div[contains(@class,"cards")]/div[3]/div[contains(@class,"card-body")]/button'
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb)
        yesStr = 'button.confirm-btn'
        self.sb.find_element(yesStr).click()

    def run(self):
        self.sb.find_element(self.canvasStr).click()

    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,3)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance

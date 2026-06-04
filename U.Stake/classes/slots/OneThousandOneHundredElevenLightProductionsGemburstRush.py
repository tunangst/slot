from classes.Slot import Slot
from classes.classUtilityFunctions import cleanNumber, takePicture
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '111lightproductions-gemburst-rush'
winningScreenshot = 'fin'
closingWordsList = ['conratulations','congratulations', 'cong', 'tions','ratulations']
nextWordList = ['youwon','you won', 'won', 'you']

class OneThousandOneHundredElevenLightProductionsGemburstRush(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
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
        # this is needed because the slot bugs and has two sets of dom elements
        editIndex = 1
        bonusStr = 'div.mg-buy-circle'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        scatterStr = 'div.bonus-cards > div.bonus-card > div.bonus-footer'
        self.sb.find_elements(scatterStr)[editIndex].click()
        Sleep(self.sb)
        yesStr = 'div.confirm-btn'
        self.sb.find_elements(yesStr)[editIndex].click()

    def run(self):
        self.sb.find_element(self.canvasStr).click()

    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,3)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
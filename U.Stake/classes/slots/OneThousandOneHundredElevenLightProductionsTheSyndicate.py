from classes.Slot import Slot
from classes.classUtilityFunctions import cleanNumber, takePicture
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '111lightproductions-the-syndicate'
winningScreenshot = 'fin'
closingWordsList = ['you won','youwon']

class OneThousandOneHundredElevenLightProductionsTheSyndicate(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.estimatedWaitTime = 30
        # need to pass two splash screens
        self.changeScene() # take the screen blocks off
        Sleep(self.sb,7)
        self.passSplashScreen()
        self.setup()
        self.run()
        # while check for same screenshots to see if game ended
        # record ending balance

    def setup(self):
        # click bonus
        bonusStr = 'div.mg-buy-circle'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        # choose scatter
        scatterStr = 'button.buy'
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb)
        yesStr = 'button.confirm-btn'
        self.sb.find_element(yesStr).click()

    def run(self):
        Sleep(self.sb,15)
        # find play btn
        canvasStr = 'canvas'
        canvas = self.sb.find_element(canvasStr).click()
       
        Sleep(self.sb, self.estimatedWaitTime)
        self.checkFin(closingWordsList)
        # find what was won
        self.findWinnings()

    def findWinnings(self):
        canvasStr = 'canvas'
        canvas = self.sb.find_element(canvasStr).click()
        # div.class="mg-data-panel > div.class="mg-data-panel-container > div[2] > span.class="mg-balance-value
        totalWinStr = '//div[contains(@class,"mg-data-panel")]/div[4]/div[2]/span[contains(@class,"mg-balance-value")]'
        totalWin = self.sb.find_element(totalWinStr).text
        self.winnings = cleanNumber(totalWin)
        pass
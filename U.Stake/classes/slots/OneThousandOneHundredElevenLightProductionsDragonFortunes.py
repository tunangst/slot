from classes.Slot import Slot
from classes.classUtilityFunctions import cleanNumber, takePicture, compareImages
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '111lightproductions-dragon-fortunes'
winningScreenshot = 'fin'
closingWordsList = ['total win', 'totalwin']
nextWordList = ['youwon','you won', 'won', 'you']

class OneThousandOneHundredElevenLightProductionsDragonFortunes(Slot):
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
        self.checkFin()
        Sleep(sb,3)
        self.findFinBal()

    def setup(self):
        # this is needed because the slot bugs and has two sets of dom elements
        bonusOption = 4
        bonusStr = 'div.mg-buy-circle'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        scatterStr = f'(//div[contains(@class,"container")]/div[contains(@class,"cards")]/div[{bonusOption}]//button)[1]'
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb)
        yesStr = 'button.confirm-btn'
        self.sb.find_element(yesStr).click()

    def run(self):
        self.sb.find_element(self.canvasStr).click()

    def checkFin(self):
        ssNum = 1
        while True:
            # take screenshot 1
            picLocation1 = takePicture(sb=self.sb,action='increment', increment=ssNum)
            # change increment
            ssNum = (ssNum % 2) + 1
            Sleep(self.sb,10)
            # take screenshot 2
            picLocation2 = takePicture(sb=self.sb,action='increment',increment=ssNum)
            # change increment
            ssNum = (ssNum % 2) + 1
            # compare
            sameImg = compareImages(picLocation1,picLocation2,similarity=.95)
            # exit if they are the same
            if sameImg:
                return

    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,3)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance

    
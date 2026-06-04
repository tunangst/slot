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
        # need to pass two splash screens
        self.changeScene() # take the screen blocks off
        Sleep(self.sb,7)
        self.passSplashScreen()
        Sleep(self.sb,3)
        self.setup()
        Sleep(self.sb,3)
        self.run()
        # while check for same screenshots to see if game ended
        # record ending balance

    def setup(self):
        # this is needed because the slot bugs and has two sets of dom elements
        bonusOption = 4
        bonusStr = 'div.mg-buy-circle'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        # choose scatter
        scatterStr = f'(//div[contains(@class,"container")]/div[contains(@class,"cards")]/div[{bonusOption}]//button)[1]'
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb)
        yesStr = 'button.confirm-btn'
        self.sb.find_element(yesStr).click()

    def run(self):
        Sleep(self.sb,17)
        # find play btn
        canvasStr = 'canvas'
        canvas = self.sb.find_element(canvasStr).click()
       
        Sleep(self.sb, self.estimatedWaitTime)
        self.checkFin()
        # find what was won
        self.findFinBal()

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
        canvasStr = 'canvas'
        self.sb.find_element(canvasStr).click()
        Sleep(self.sb,3)
        # totalWinStr = '//div[contains(@class,"mg-data-panel")]/div[4]/div[2]/span[contains(@class,"mg-balance-value")]'
        # totalWin = self.sb.find_element(totalWinStr).text
        # self.winnings = cleanNumber(totalWin)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance

    
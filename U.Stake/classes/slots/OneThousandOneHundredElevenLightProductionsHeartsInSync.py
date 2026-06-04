from classes.Slot import Slot
from classes.classUtilityFunctions import cleanNumber, takePicture
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '111lightproductions-hearts-in-sync'
winningScreenshot = 'fin'
closingWordsList = ['total win','totalwin']
checkWordsList = ['free spins','freespins']
nextWordList = ['youwon','you won', 'won', 'you']

class OneThousandOneHundredElevenLightProductionsHeartsInSync(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 200
        self.estimatedWaitTime = 90
        self.canvasStr = 'canvas#game'
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb,20)
        self.run()
        Sleep(sb,3)
        self.checkFin(closingWordsList=closingWordsList,eleStr=self.canvasStr)
        Sleep(sb)
        self.findWinnings()

    def setup(self):
        # this is needed because the slot bugs and has two sets of dom elements
        bonusIndex = 3
        bonusStr = 'div.mg-buy-circle'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        scatterStr = f'//div[contains(@class,"cards")]/div[{bonusIndex}]/div[contains(@class,"card-body")]/button'
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb)
        yesStr = 'button.confirm-btn'
        self.sb.find_element(yesStr).click()

    def run(self):
        self.timedScreenCheck(timeout=self.estimatedWaitTime,checkWordsList=checkWordsList,eleStr=self.canvasStr)

    def findWinnings(self):
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,3)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
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
        # need to pass two splash screens
        self.changeScene() # take the screen blocks off
        Sleep(self.sb,3)
        self.passSplashScreen()
        Sleep(self.sb,3)
        self.setup()
        Sleep(self.sb,3)
        self.run()
        # while check for same screenshots to see if game ended
        # record ending balance

    def setup(self):
        # this is needed because the slot bugs and has two sets of dom elements
        bonusIndex = 3
        bonusStr = 'div.mg-buy-circle'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        # choose scatter
        # div.cards > div[3] > div.card-body > button
        scatterStr = f'//div[contains(@class,"cards")]/div[{bonusIndex}]/div[contains(@class,"card-body")]/button'
        # scatterStr = 'div.bonus-cards > div.bonus-card > div.bonus-footer'
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb)
        yesStr = 'button.confirm-btn'
        self.sb.find_element(yesStr).click()

    def run(self):
        Sleep(self.sb,20)
        # find play btn
        canvasStr = 'canvas'
        # self.sb.find_element(canvasStr).click()
       
        self.timedScreenCheck(timeout=self.estimatedWaitTime,checkWordsList=checkWordsList,eleStr=canvasStr)
        # Sleep(self.sb, self.estimatedWaitTime)
        self.checkFin(closingWordsList=closingWordsList,eleStr=canvasStr)
        # find what was won
        self.findWinnings()

    def findWinnings(self):
        Sleep(self.sb,3)
        canvasStr = 'canvas'
        self.sb.find_element(canvasStr).click()
        Sleep(self.sb,3)
        # picLocation = takePicture(sb=self.sb,action='fin',fileName=winningScreenshot,eleStr=canvasStr)
        # cap = Capture(imageLocation=picLocation,action='find next',targetWordList=nextWordList)
        # if cap.targetBlock:
        #     winStr = cap.targetBlock['text']
        #     self.winnings = cleanNumber(winStr)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
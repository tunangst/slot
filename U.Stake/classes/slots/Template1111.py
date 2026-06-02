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
        self.estimatedWaitTime = 30
        # need to pass two splash screens
        self.changeScene() # take the screen blocks off
        Sleep(self.sb,3)
        self.passSplashScreen()
        Sleep(self.sb,2)
        self.setup()
        self.run()
        # while check for same screenshots to see if game ended
        # record ending balance

    def setup(self):
        # this is needed because the slot bugs and has two sets of dom elements
        editIndex = 1
        bonusStr = 'div.mg-buy-circle'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        # choose scatter
        scatterStr = 'div.bonus-cards > div.bonus-card > div.bonus-footer'
        self.sb.find_elements(scatterStr)[editIndex].click()
        Sleep(self.sb)
        yesStr = 'div.confirm-btn'
        self.sb.find_elements(yesStr)[editIndex].click()

    def run(self):
        Sleep(self.sb,17)
        # find play btn
        canvasStr = 'canvas'
        canvas = self.sb.find_element(canvasStr).click()
       
        Sleep(self.sb, self.estimatedWaitTime)
        self.checkFin(closingWordsList)
        # find what was won
        self.findWinnings()

    def findWinnings(self):
        picLocation = './U.Stake/images/screenshots/fin.png'
        # canvasStr = 'canvas'
        # canvas = self.sb.find_element(canvasStr)
        # picLocation = takePicture(sb=self.sb,action='fin',fileName=winningScreenshot,eleStr=canvasStr)
        cap = Capture(imageLocation=picLocation,action='find next',targetWordList=nextWordList)
        if cap.targetBlock:
            winStr = cap.targetBlock['text']
            self.winnings = cleanNumber(winStr)
        pass
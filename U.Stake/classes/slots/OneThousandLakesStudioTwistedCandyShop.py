from classes.Slot import Slot
from classes.classUtilityFunctions import takePicture, cleanNumber
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '1000lakesstudios-twisted-candy-shop'
winningScreenshot = 'fin'
closingWords = ['total win', 'totalwin']

class OneThousandLakesStudioTwistedCandyShop(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.estimatedWaitTime = 30
        # need to pass two splash screens
        self.changeScene() # take the screen blocks off
        Sleep(self.sb,10)
        self.passSplashScreen()
        self.setup()
        self.run()
        # while check for same screenshots to see if game ended
        # record ending balance

    def setup(self):
        # click bonus
        bonusStr = 'button[aria-label="Open BONUS"]'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        # choose scatter
        scatterStr = '//article[@data-offer-id="buy_12fs"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb)
        yesStr = 'button.frame-confirm__accept'
        self.sb.find_element(yesStr).click()

    def run(self):
        Sleep(self.sb,6)
        # find play btn
        canvasStr = '#game'
        canvas = self.sb.find_element(canvasStr).click()
       
        Sleep(self.sb, self.estimatedWaitTime)
        self.checkFin(closingWords)
        # find what was won
        self.findWinnings()

    def findWinnings(self):
        # crop the screenshot because it will pull in date and other out of range options
        canvasStr = 'canvas#game'
        canvas = self.sb.find_element(canvasStr)
        picLocation = takePicture(sb=self.sb,action='fin',eleStr=canvasStr)
        cap = Capture(imageLocation=picLocation,action='find number')
        winStr = cap.status
        self.winnings = cleanNumber(winStr)
        pass
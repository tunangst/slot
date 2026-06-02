from classes.Slot import Slot
from classes.classUtilityFunctions import cleanNumber, takePicture
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '1000lakesstudios-yakuza-v-i-p'
winningScreenshot = 'fin'
closingWords = ['total win', 'totalwin']
startingWords = ['congratulations']

class OneThousandLakesStudioYakuzaVIP(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 300
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
        bonusOption = 3
        bonusStr = 'button[aria-label="Open BONUS"]'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        # choose scatter
        scatterStr = '//article[@data-offer-id="super_buy"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb)
        yesStr = 'button.frame-confirm__accept'
        self.sb.find_element(yesStr).click()

        while True:
            # find congratulations screen
            # 'check end words'
            picLocation = takePicture(sb=self.sb,action='tmp')
            cap = Capture(imageLocation=picLocation,action='check end words',closingWordsList=startingWords)
            print(cap.targetBlock)
            if cap.fin:
                break

    def run(self):
        # Sleep(self.sb,20)
        # find play btn
        canvasStr = '#game'
        canvas = self.sb.find_element(canvasStr).click()
       
        Sleep(self.sb, self.estimatedWaitTime)
        self.checkFin(closingWords)
        # find what was won
        self.findFinBal()

    def findFinBal(self):
        canvasStr = '#game'
        self.sb.find_element(canvasStr).click()
        Sleep(self.sb,3)
        # winBlockStr = 'div[data-variant="win"]'
        # winBlock = self.sb.find_element(winBlockStr)
        # winTxt = winBlock.text
        # win = cleanNumber(winTxt)
        # self.winnings = win
        balanceStr = 'span.frame-hud__display-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance

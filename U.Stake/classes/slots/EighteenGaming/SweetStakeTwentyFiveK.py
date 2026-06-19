from classes.nesting.EighteenGaming import EighteenGaming
from classes.classUtilityFunctions import cleanNumber, takePicture, findEmbeddedCoords
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom, ClickTheDom
from selenium.webdriver.common.action_chains import ActionChains
import time

slotCode = '18gaming-sweet-stake-25k'
# winningScreenshot = 'fin'
closingWordsList = ['conratulations','congratulations', 'cong', 'tions','ratulations']
# nextWordList = ['youwon','you won', 'won', 'you']
bonusWords = ['super spins']
checkAllWordsList = ['congratulations','you won','free spins']

class SweetStakeTwentyFiveK(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 500
        self.estimatedWaitTime = 60
        
        self.changeScene() # take the screen blocks off
        self.runSleepThree()
        self.passSplashScreen()
        self.runSleepThree()
        self.setup()
        self.checkSpins()
        self.checkFin(closingWordsList)
        self.runSleepThree()
        self.findFinBal()

    def setup(self):
        xValBonus, yValBonus = findEmbeddedCoords(sb=self.sb,checkWordList=bonusWords)
        # switch it to take full screenshot and mark the click location
        ClickTheDom(sb=self.sb,xVal=xValBonus,yVal=yValBonus)
        self.runSleepOne()
        self.clickConfirmBtn()

    def run(self):
        # self.sb.find_element(self.canvasStr).click()
        pass

    def checkSpins(self):
        counter = self.estimatedWaitTime
        end_time = time.monotonic() + counter
        while True:
            remaining = max(0, int(end_time - time.monotonic()))
            seconds = remaining % 60
            timerText = f'{seconds}'
            print(timerText, end='\r')

            if remaining == 0:
                break
            time.sleep(0.1)

            picLocation = takePicture(sb=self.sb,action='check fin',eleStr=self.canvasStr)
            cap = Capture(imageLocation=picLocation,action='check all words',targetWordList=checkAllWordsList)
            if cap.status == True:
                self.sb.find_element(self.canvasStr).click()
         
    def findFinBal(self):
        # take pic of canvas, see if total win is there

        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,3)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance

from classes.Slot import Slot
from classes.classUtilityFunctions import cleanNumber, takePicture, findEmbeddedCoords
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom, ClickTheDom
from selenium.webdriver.common.action_chains import ActionChains
import time

slotCode = '18gaming-bowling-riches'
# winningScreenshot = 'fin'
closingWordsList = ['spinsplayed','spins played']
# nextWordList = ['youwon','you won', 'won', 'you']
bonusWords = ['bonus']
checkAllWordsList = ['congratulations','you won','free spins']

class EighteenGamingBowlingRiches(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 100
        self.estimatedWaitTime = 60
        self.canvasStr = 'canvas'
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb,15)
        self.run()
        self.checkSpins()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin(closingWordsList)
        Sleep(sb,3)
        self.findFinBal()
        # while check for same screenshots to see if game ended
        # record ending balance

    def setup(self):
        xValBonus, yValBonus = findEmbeddedCoords(sb=self.sb,checkWordList=bonusWords)
        # switch it to take full screenshot and mark the click location
        ClickTheDom(sb=self.sb,xVal=xValBonus,yVal=yValBonus)
        Sleep(self.sb,3)
        scatterBtn = 'button.buy'
        self.sb.find_element(scatterBtn).click()
        Sleep(self.sb,3)
        btnStr = 'button.confirm-btn'
        self.sb.find_element(btnStr).click()

    def run(self):
        self.sb.find_element(self.canvasStr).click()

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
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,3)
        balanceStr = 'span.mg-balance-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance

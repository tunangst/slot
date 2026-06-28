from classes.nesting.EighteenGaming import EighteenGaming
from classes.classUtilityFunctions import cleanNumber, takePicture, findEmbeddedCoords, findCircles
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom, ClickTheDom, GetRandomNumber
from selenium.webdriver.common.action_chains import ActionChains
import time

slotCode = '18gaming-fruit-burst-bonanza'
closingWordsList = ['conratulations','congratulations', 'cong', 'tions','ratulations']

bonusArr = [100,70,111,112,42]


class FruitBurstBonanza(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.bonusInd = GetRandomNumber(len(bonusArr)-1)
        self.buyoutBalance = bonusArr[self.bonusInd]
        self.estimatedWaitTime = 60
        
        self.changeScene() # take the screen blocks off
        self.runSleepThree()
        self.passSplashScreen()
        self.passTriangleScreen()
        self.runSleepThree()
        self.setup()
        self.runSleepMain()
        self.run()
        self.checkSpins()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin()
        self.runSleepThree()
        self.findFinBal()

    def setup(self):
        self.clickBuyout()
        self.runSleepOne()
        # + 1 because the dom doesn't use 0 index
        scatterStr = f'//div[contains(@class,"bonus-cards")]/div[{self.bonusInd + 1}]/div[contains(@class,"bonus-footer")]'
        self.sb.find_elements(scatterStr)[self.domAdjustment].click()
        self.runSleepOne()
        self.clickConfirmDivIncrement()
        Sleep(self.sb,30)
        self.setupAutoSpin()

    def run(self):
        # self.sb.find_element(self.canvasStr).click()
        pass
         
    def checkFin(self):
        countStr = '//div[contains(@class,"icon-spin")]/div[contains(@class,"mg-stop-icon")]/span'
        stuck = False
        while True:
            try:
                checkCount = self.sb.find_element(countStr).text
                print(checkCount)
                Sleep(self.sb,5)
                if checkCount == stuck:
                    self.sb.find_element(self.canvasStr).click()
                stuck = checkCount
            except:
                break

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
        balanceStr = '//div[contains(@class,"mg-data-panel-container")]/div[contains(@class,"mg-data-panel-item")]/span[contains(@class,"mg-balance-value")]'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
from classes.nesting.Slot import Slot
import json
import time
from utilityFunctions import Sleep
from classes.classUtilityFunctions import takePicture, cleanNumber
from classes.Capture import Capture

class EighteenGaming(Slot):
    def __init__(self, sb, slotCode, obs):
        super().__init__(sb, slotCode,obs)
        self.buyoutStr = '//div[contains(@class,"mg-buy-circle")]'
        self.confirmBtnStr = '//*[contains(@class,"confirm-btn")]'
        # self.confirmBtnStr2 = '//div[contains(@class,"confirm-btn")]'
        self.balanceStr = '//span[contains(@class,"mg-balance-value")]'
        self.countStr = '//div[contains(@class,"mg-right-container")]/div[contains(@class,"mg-action-autoplay")]/div[contains(@class,"mg-autoplay-icon")]'
        self.spinCountStr = '//div[contains(@class,"icon-spin")]/div[contains(@class,"mg-stop-icon")]/span'
        self.spinStr = '//div[contains(@class,"mg-action-play")]/div[contains(@class,"icon-spin")]/div[contains(@class,"mg-spin-icon")]'

    def run(self):
        self.changeScene() # take the screen blocks off
        self.passSplashScreen()
        Sleep(self.sb,3)
        self.setup()
        self.checkFinEle()
        Sleep(self.sb,3)
        self.findFinBal()
        self.calculateWinnings()

    def passSplashScreen(self):
        self.sb.switch_to_frame('iframe')
        while not self.sb.is_element_present(self.spinStr):
            self.passTriangleScreen()
            Sleep(self.sb,2)

    def setup(self):
        self.clickBuyout()
        Sleep(self.sb)
        self.clickBonusCard()
        Sleep(self.sb)
        self.clickConfirm()

    def clickBuyout(self):
        self.sb.find_element(self.buyoutStr).click()
    
    def clickBonusCard(self):
        # this needs to be function level for accurate bonusOption
        bonusEles = False
        scatterStr1 = f'//div[contains(@class,"bonus-cards")]/div[{self.bonusOption}]/div[contains(@class,"bonus-footer")]'
        scatterStr2 = f'//div[contains(@class,"cards")]/div[{self.bonusOption}]/div[contains(@class,"card-body")]/button'
        if self.sb.is_element_present(scatterStr1):
            bonusEles = self.sb.find_elements(scatterStr1)
        elif self.sb.is_element_present(scatterStr2):
            bonusEles = self.sb.find_elements(scatterStr2)
        match len(bonusEles):
            case n if n > 1:
                bonusEles[1].click()
            case n if n > 0:
                bonusEles[0].click()
            case _:
                print('error in clickbonus function')

    def clickConfirm(self):
        confirmEles = []
        if self.sb.is_element_present(self.confirmBtnStr):
            confirmEles = self.sb.find_elements(self.confirmBtnStr)
        match len(confirmEles):
            case n if n > 1:
                confirmEles[1].click()
            case n if n > 0:
                confirmEles[0].click()
            case _:
                print('error in clickConfirm function') 

    def setupAutoSpin(self):
        self.sb.find_element(self.countStr).click()
        Sleep(self.sb)
        numStr = f'//li[contains(., "{self.spinCount}")]'
        self.sb.find_element(numStr).click()
        Sleep(self.sb)
        autoStr = '//div[contains(@class,"mg-action-panel-container")]/div[contains(@class,"mg-action-play")]/div[contains(@class,"icon-spin")]/div[contains(@class,"mg-spin-autoplay-icon")]'
        self.sb.find_element(autoStr).click()

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

    # def checkAutoFin(self):
        # stuck = False
        # finCheck = False
        # while True:
        #     try:
        #         checkCount = self.sb.find_element(self.spinCountStr).text
        #         print(checkCount)
        #         Sleep(self.sb,5)
        #         if checkCount == stuck:
        #             self.defaultClick()
        #         stuck = checkCount
        #         finCheck = False
        #     except:
        #         if finCheck:
        #             return
        #         self.sb.find_element(self.canvasStr).click()
        #         # see if autospin is done
        #         try:
        #             self.sb.find_element(self.spinCountStr)
        #         except:
        #             finCheck = True

    def checkFinEle(self):
        while not self.sb.is_element_present(self.spinStr):
            self.defaultClick()
            Sleep(self.sb,3)

    def checkFin(self,crop=False,action='find any text',targetWordList=False):
        startSwitch = False
        endSwitch = 0 # 0-3
        endSwitchLimit = 3
        while True:
            try:
                self.defaultClick()
                Sleep(self.sb,3)
                # screenshot the spin count
                picLocation = takePicture(sb=self.sb,action='check fin',crop=crop)
                instance = Capture(imageLocation=picLocation,action=action,targetWordList=targetWordList)
                if instance.status: # count number is present
                    startSwitch = True
                    endSwitch = 0
                elif endSwitch >= endSwitchLimit:
                    break
                elif startSwitch == True:
                    endSwitch += 1
            except:
                print(f'{self.slotCode}, error in checkfin')

    def checkFin(self, closingWordsList,eleStr=False):
        while True:
            # compare screenshots
            picLocation = takePicture(sb=self.sb,action='check fin',crop='mid-fifty')
            # look for Click, Continue, etc
            instance = Capture(imageLocation=picLocation,action='check end words',targetWordList=closingWordsList)
            # if instance:
            if instance.fin:
                return True
            Sleep(self.sb,5)

    def findFinBal(self):
        self.defaultClick()
        Sleep(self.sb,3)
        self.endingBalance = cleanNumber(self.sb.find_element(self.balanceStr).text)
    
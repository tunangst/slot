from classes.nesting.Slot import Slot
import json
import time
from utilityFunctions import Sleep, ClickTheDom
from classes.classUtilityFunctions import takePicture, checkCaptcha, checkRegionChange
from classes.Capture import Capture

class EighteenGaming(Slot):
    def __init__(self, sb, slotCode, obs):
        super().__init__(sb, slotCode,obs)
        self.buyoutStr = '//div[contains(@class,"mg-buy-circle")]'
        self.confirmBtnStr = '//button[contains(@class,"confirm-btn")]'
        self.confirmDivStr = '//div[contains(@class,"confirm-btn")]'

    def clickBuyout(self):
        self.sb.find_element(self.buyoutStr).click()

    def clickBonusCard(self):
        bonusCardStr = f'//div[contains(@class,"bonus-cards")]/div[{self.bonusOption}]/div[contains(@class,"bonus-footer")]'
        self.sb.find_element(bonusCardStr)
    def clickBonusCardIncrement(self):
        bonusCardStr = f'//div[contains(@class,"bonus-cards")]/div[{self.bonusOption}]/div[contains(@class,"bonus-footer")]'
        self.sb.find_elements(bonusCardStr)[self.domAdjustment].click()

    def clickConfirmDiv(self):
        self.sb.find_element(self.confirmDivStr).click()
    def clickConfirmDivIncrement(self):
        self.sb.find_elements(self.confirmDivStr)[self.domAdjustment].click()
    def clickConfirmBtn(self):
        self.sb.find_element(self.confirmBtnStr).click()
    def clickConfirmBtnIncrement(self):
        self.sb.find_elements(self.confirmBtnStr)[self.domAdjustment].click()

    def setupAutoSpin(self):
        countStr = '//div[contains(@class,"mg-right-container")]/div[contains(@class,"mg-action-autoplay")]/div[contains(@class,"mg-autoplay-icon")]'
        self.sb.find_element(countStr).click()
        self.runSleepOne()
        numStr = f'//li[contains(., "{self.spinCount}")]'
        self.sb.find_element(numStr).click()
        self.runSleepOne()
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

    def checkAutoFin(self):
        countStr = '//div[contains(@class,"icon-spin")]/div[contains(@class,"mg-stop-icon")]/span'
        stuck = False
        finCheck = False
        while True:
            try:
                checkCount = self.sb.find_element(countStr).text
                print(checkCount)
                Sleep(self.sb,5)
                if checkCount == stuck:
                    self.sb.find_element(self.canvasStr).click()
                stuck = checkCount
                finCheck = False
            except:
                if finCheck:
                    return
                self.sb.find_element(self.canvasStr).click()
                # see if autospin is done
                try:
                    self.sb.find_element(countStr)
                except:
                    finCheck = True

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
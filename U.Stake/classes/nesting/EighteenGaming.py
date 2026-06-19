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
        self.runSleepShort()
        numStr = f'//li[contains(., "{self.spinCount}")]'
        self.sb.find_element(numStr).click()
        self.runSleepShort()
        autoStr = '//div[contains(@class,"mg-action-panel-container")]/div[contains(@class,"mg-action-play")]/div[contains(@class,"icon-spin")]/div[contains(@class,"mg-spin-autoplay-icon")]'
        self.sb.find_element(autoStr).click()
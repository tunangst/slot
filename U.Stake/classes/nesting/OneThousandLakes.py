from classes.nesting.Slot import Slot
import json
import time
from utilityFunctions import Sleep, ClickTheDom
from classes.classUtilityFunctions import takePicture, checkCaptcha, checkRegionChange
from classes.Capture import Capture

class OneThousandLakes(Slot):
    def __init__(self, sb, slotCode, obs):
        super().__init__(sb, slotCode, obs)
        self.optionStr = 'button[aria-label="Open menu"]'
        self.turboStr = 'span.frame-icon--turbo'
        self.closeStr = 'span.frame-icon--close'
        self.buyoutStr = 'button[aria-label="Open bonus shop"]'
        self.bonusCardStr = '//article[@data-offer-id="buy_12fs"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        self.confirmBtnStr = 'button.frame-confirm__accept'

    def clickOption(self):
        self.sb.find_element(self.optionStr).click()

    def clickTurbo(self):
        self.sb.find_element(self.turboStr).click()

    def clickClose(self):
        self.sb.find_element(self.closeStr).click()

    def clickBuyout(self):
        self.sb.find_element(self.buyoutStr).click()

    def clickBonusCard(self):
        self.sb.find_element(self.bonusCardStr).click()

    def clickConfirm(self):
        self.sb.find_element(self.confirmBtnStr).click()

    def setTurbo(self):
        self.clickOption()
        self.runSleepShort()
        self.clickTurbo()
        self.runSleepShort()
        self.clickClose()
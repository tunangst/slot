from classes.nesting.Slot import Slot
import json
import time
from utilityFunctions import Sleep, ClickTheDom
from classes.classUtilityFunctions import takePicture, checkCaptcha, checkRegionChange
from classes.Capture import Capture

class OneThousandLakesStudios(Slot):
    def __init__(self, sb, slotCode, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutStr = '//button[contains(@class,"game-buttons__bonus")]'
        self.bonusCardStr = '//div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        # self.bonusCardStr = '//article[@data-offer-id="buy_apex"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        self.confirmBtnStr = '//button[contains(@class,"frame-confirm__accept")]'

    def clickBuyout(self):
        self.sb.find_element(self.buyoutStr).click()

    # def clickBonusCard(self):
    #     self.sb.find_element(self.bonusCardStr).click()

    def clickConfirmBtn(self):
        self.sb.find_element(self.confirmBtnStr).click()
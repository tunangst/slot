from classes.nesting.Slot import Slot
import json
import time
from utilityFunctions import Sleep, ClickTheDom
from classes.classUtilityFunctions import takePicture, checkCaptcha, checkRegionChange
from classes.Capture import Capture

class ZeroxEdge(Slot):
    def __init__(self, sb, slotCode, obs):
        super().__init__(sb, slotCode, obs)
        self.turboStr = 'button[aria-label="Turbo mode"]'
        self.autoStr = 'button[aria-label="Autoplay"]'
        self.startStr = '//button[contains(@class,"start-btn")]'
        self.confirmStr = '//button[contains(@class,"confirm-yes")]'
        self.bonusStr = '//button[contains(@class,"bonus-outline-btn")]'
        self.bonusCardStr = f'//div[contains(@class, "tiles-grid")]/div[{self.bonusOption}]/div[contains(@class, "tile-footer")]/button'

    def clickTurbo(self):
        self.sb.find_element(self.turboStr).click()

    def clickAuto(self):
        self.sb.find_element(self.autoStr).click()

    def clickStart(self):
        self.sb.find_element(self.startStr).click()

    def clickBonus(self):
        self.sb.find_element(self.bonusStr).click()

    def clickBonusCard(self):
        self.sb.find_element(self.bonusCardStr).click()

    def clickConfirm(self):
        self.sb.find_element(self.confirmStr).click()
        
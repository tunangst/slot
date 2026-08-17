from classes.nesting.Slot import Slot
import json
import time
from utilityFunctions import Sleep
from classes.classUtilityFunctions import takePicture, cleanNumber
from classes.Capture import Capture

class OneThousandLakesStudios(Slot):
    def __init__(self, sb, slotCode, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutStr1 = '//button[contains(@class,"game-buttons__bonus")]'
        self.buyoutStr2 = '//button[@aria-label="Open BONUS"]'
        self.bonusCardStr1 = '//article[@data-offer-id="super_buy"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        self.bonusCardStr2 = '//article[@data-offer-id="buy_12fs"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        self.bonusCardStr3 = '//article[@data-offer-id="buy_super"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        # self.bonusCardStr = '//article[@data-offer-id="buy_apex"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        self.confirmBtnStr = '//button[contains(@class,"frame-confirm__accept")]'
        self.balanceStr = '//span[contains(@class,"frame-hud__display-value")]'

    # aria-label: Open BONUS
    # button.frame-hud__button--buy

    def setup(self):
        self.clickBuyout()
        Sleep(self.sb)
        self.clickBonusCard()
        Sleep(self.sb)
        self.clickConfirmBtn()

    def clickBuyout(self):
        if self.sb.is_element_present(self.buyoutStr1):
            self.sb.find_element(self.buyoutStr1).click()
        elif self.sb.is_element_present(self.buyoutStr2):
            self.sb.find_element(self.buyoutStr2).click()

    def clickBonusCard(self):
        if self.sb.is_element_present(self.bonusCardStr1):
            self.sb.find_element(self.bonusCardStr1).click()
        elif self.sb.is_element_present(self.bonusCardStr2):
            self.sb.find_element(self.bonusCardStr2).click()
        elif self.sb.is_element_present(self.bonusCardStr3):
            self.sb.find_element(self.bonusCardStr3).click()

    def clickConfirmBtn(self):
        self.sb.find_element(self.confirmBtnStr).click()

    def checkFin(self,crop,action='find any text',targetWordList=False):
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
                        endSwitch = 1
                    elif endSwitch >= endSwitchLimit:
                        break
                    elif startSwitch == True:
                        endSwitch += 1
                except:
                    print(f'{self.slotCode}, error in checkfin')

    def findFinBal(self):
            self.defaultClick()
            Sleep(self.sb,3)   
            self.endingBalance = cleanNumber(self.sb.find_element(self.balanceStr).text)
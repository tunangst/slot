from classes.nesting.Slot import Slot
import json
import time
from utilityFunctions import Sleep, ClickTheDom
from classes.classUtilityFunctions import takePicture, checkCaptcha, checkRegionChange
from classes.Capture import Capture

class OneThousandOneHundredElevenLightProductions(Slot):
    def __init__(self, sb, slotCode, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutStr = '//div[contains(@class,"mg-buy-circle")]'
        self.confirmBtnStr = '//button[contains(@class,"confirm-btn")]'
        self.confirmDivStr = '//div[contains(@class,"confirm-btn")]'

    def clickBuyout(self):
        self.sb.find_element(self.buyoutStr).click()

    def clickBonusCard(self):
        # this needs to be function level for accurate bonusOption
        bonusCardStr = f'//div[contains(@class,"bonus-cards")]/div[{self.bonusOption}]/div[contains(@class,"bonus-footer")]'
        bonusEles = self.sb.find_elements(bonusCardStr)
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
        if self.sb.is_element_present(self.confirmDivStr):
            confirmEles = self.sb.find_elements(self.confirmDivStr)
        match len(confirmEles):
            case n if n > 1:
                confirmEles[1].click()
            case n if n > 0:
                confirmEles[0].click()
            case _:
                print('error in clickConfirm function')      

    def checkFin(self,locLabel,action='find number',targetWordList=False):
        startSwitch = False
        endSwitch = False
        while True:
            try:
                self.defaultClick()
                Sleep(self.sb,2)
                # screenshot the spin count
                picLocation = takePicture(sb=self.sb,action='check fin',crop=locLabel)
                instance = Capture(imageLocation=picLocation,action=action,targetWordList=targetWordList)
                if instance.status: # count number is present
                    startSwitch = True
                    endSwitch = False
                elif endSwitch == True:
                    break
                elif startSwitch == True:
                    endSwitch = True
            except:
                print(f'{self.slotCode}, error in checkfin')
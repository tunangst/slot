from classes.nesting.Slot import Slot
from utilityFunctions import Sleep
from classes.classUtilityFunctions import takePicture, cleanNumber
from classes.Capture import Capture

class OneHundredElevenLightProductions(Slot):
    def __init__(self, sb, slotCode, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutStr = '//div[contains(@class,"mg-buy-circle")]'
        self.confirmBtnStr = '//button[contains(@class,"confirm-btn")]'
        self.confirmDivStr = '//div[contains(@class,"confirm-btn")]'
        self.balanceStr = '//span[contains(@class,"mg-balance-value")]'

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
    # def clickBonusCard(self):
    #     # this needs to be function level for accurate bonusOption
    #     bonusCardStr = f'//div[contains(@class,"bonus-cards")]/div[{self.bonusOption}]/div[contains(@class,"bonus-footer")]'
    #     bonusEles = self.sb.find_elements(bonusCardStr)
    #     match len(bonusEles):
    #         case n if n > 1:
    #             bonusEles[1].click()
    #         case n if n > 0:
    #             bonusEles[0].click()
    #         case _:
    #             print('error in clickbonus function')

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

    def checkFin(self,crop,action='find any text',targetWordList=False):
        startSwitch = False
        endSwitch = False
        while True:
            try:
                self.defaultClick()
                Sleep(self.sb,3)
                # screenshot the spin count
                picLocation = takePicture(sb=self.sb,action='check fin',crop=crop)
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

    def findFinBal(self):
        self.defaultClick()
        Sleep(self.sb,3)
        self.endingBalance = cleanNumber(self.sb.find_element(self.balanceStr).text)
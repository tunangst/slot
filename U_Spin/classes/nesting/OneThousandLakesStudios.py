from classes.nesting.Slot import Slot
from utilityFunctions import Sleep
from classes.classUtilityFunctions import takePicture, cleanNumber
from classes.Capture import Capture

class OneThousandLakesStudios(Slot):
    def __init__(self, sb, slotCode, obs):
        super().__init__(sb, slotCode, obs)
        self.splashCheckStr = '//div[@aria-label="Press anywhere to continue"]'

        self.buyoutStr1 = '//button[contains(@class,"game-buttons__bonus")]'
        self.buyoutStr2 = '//button[@aria-label="Open BONUS"]'

        self.bonusCardStr1 = '//article[@data-offer-id="super_buy"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        self.bonusCardStr2 = '//article[@data-offer-id="buy_12fs"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        self.bonusCardStr3 = '//article[@data-offer-id="buy_super"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        self.bonusCardStr4 = '//article[@data-offer-id="bonus3"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'        
        self.bonusCardStr5 = '//article[@data-offer-id="super_modifier"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        self.bonusCardStr6 = '//article[@data-offer-id="buy_ultimate"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'  
        self.bonusCardStr7 = '//article[@data-offer-id="buy_apex"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
      

        self.confirmBtnStr = '//button[contains(@class,"frame-confirm__accept")]'
        self.balanceStr = '//span[contains(@class,"frame-hud__display-value")]'

        self.counterStr = '//button[@aria-label="SPIN"]/span[contains(@class,"frame-hud__spin-label--counter")]'
        self.spinStr = '//button[@aria-label="SPIN"]/span[contains(@class,"frame-hud__spin-label")]/img[contains(@class,"frame-hud__spin-icon")]'

    def findSplashLoaded(self):
        self.sb.switch_to_frame('iframe')
        self.sb.wait_for_element_visible(
            self.splashCheckStr,
            by="xpath",
            timeout=30
        )

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
        elif self.sb.is_element_present(self.bonusCardStr4):
            self.sb.find_element(self.bonusCardStr4).click()
        elif self.sb.is_element_present(self.bonusCardStr5):
            self.sb.find_element(self.bonusCardStr5).click()
        elif self.sb.is_element_present(self.bonusCardStr6):
            self.sb.find_element(self.bonusCardStr6).click()
        elif self.sb.is_element_present(self.bonusCardStr7):
            self.sb.find_element(self.bonusCardStr7).click()

    def clickConfirmBtn(self):
        self.sb.find_element(self.confirmBtnStr).click()

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

    def checkFinEles(self):
        # make sure the spin starts
        while not self.sb.is_element_present(self.counterStr):
            Sleep(self.sb,2)
            self.defaultClick()
        # find when the spin finishes
        while not self.sb.is_element_present(self.spinStr):
            Sleep(self.sb,2)
            self.defaultClick()

    def findFinBal(self):
        self.defaultClick()
        Sleep(self.sb,3)   
        self.endingBalance = cleanNumber(self.sb.find_element(self.balanceStr).text)
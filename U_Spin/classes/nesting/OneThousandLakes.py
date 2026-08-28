from classes.nesting.Slot import Slot
from utilityFunctions import Sleep
from classes.classUtilityFunctions import takePicture
from classes.Capture import Capture

class OneThousandLakes(Slot):
    def __init__(self, sb, slotCode, obs):
        super().__init__(sb, slotCode, obs)
        self.splashCheckStr = '//div[@aria-label="Press anywhere to continue"]'

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
        Sleep(self.sb)
        self.clickTurbo()
        Sleep(self.sb)
        self.clickClose()

    def findSplashLoaded(self):
        self.sb.switch_to_frame('iframe')
        self.sb.wait_for_element_visible(
            self.splashCheckStr,
            by="xpath",
            timeout=30
        )

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
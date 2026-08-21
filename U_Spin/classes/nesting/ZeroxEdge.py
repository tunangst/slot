from classes.Capture import Capture
from classes.nesting.Slot import Slot
from utilityFunctions import Sleep
from classes.classUtilityFunctions import cleanNumber, takePicture

class ZeroxEdge(Slot):
    def __init__(self, sb, slotCode, obs):
        super().__init__(sb, slotCode, obs)
        self.turboStr = 'button[aria-label="Turbo mode"]'
        self.autoStr = 'button[aria-label="Autoplay"]'
        self.startStr = '//button[contains(@class,"start-btn")]'
        self.confirmStr = '//button[contains(@class,"confirm-yes")]'

        self.bonusStr1 = '//button[contains(@class,"bonus-outline-btn")]'
        self.bonusStr2 = '//button[contains(@class,"bonus-x-btn")]'

        self.counterStr = '//button[contains(@class,"play-btn-circle")]/span[contains(@class,"fs-btn-counter")]/span[contains(@class,"fs-btn-num") and not(contains(@class,"fs-btn-total"))]'
        self.balanceStr = '//div[contains(@class,"bar-left")]/div[contains(@class,"info-stack")]/div[contains(@class,"info-row")]/span[contains(@class,"info-value")]'

        # self.counterStr = '//button[contains(@class,"play-btn-circle")]/span'
        self.spinStr = '//button[contains(@class,"play-btn-circle")]/*[local-name()="svg"]'

    def clickTurbo(self):
        self.sb.find_element(self.turboStr).click()

    def clickAuto(self):
        self.sb.find_element(self.autoStr).click()

    def clickStart(self):
        self.sb.find_element(self.startStr).click()

    def clickBonus(self):
        if self.sb.is_element_present(self.bonusStr1):
            self.sb.find_element(self.bonusStr1).click()
        if self.sb.is_element_present(self.bonusStr2):
            self.sb.find_element(self.bonusStr2).click()
        
    def clickBonusCard(self):
        # needs to be here otherwise it will initialize bonusCardStr as 1, the init value
        self.bonusCardStr1 = f'//div[contains(@class, "tiles-grid")]/div[{self.bonusOption}]/div[contains(@class, "tile-body")]/button'
        self.bonusCardStr2 = f'//div[contains(@class, "tiles-grid")]/div[{self.bonusOption}]/div[contains(@class, "tile-footer")]/button'
        self.bonusCardStr3 = f'//div[contains(@class, "tiles-row")]/div[{self.bonusOption}]//div[contains(@class, "tile-body")]//button'

        if self.sb.is_element_present(self.bonusCardStr1):
            self.sb.find_element(self.bonusCardStr1).click()
        if self.sb.is_element_present(self.bonusCardStr2):
            self.sb.find_element(self.bonusCardStr2).click()
        if self.sb.is_element_present(self.bonusCardStr3):
            self.sb.find_element(self.bonusCardStr3).click()

    def clickConfirm(self):
        self.sb.find_element(self.confirmStr).click()

    def run(self):
        self.changeScene() # take the screen blocks off
        self.findSplashLoaded()
        Sleep(self.sb,3) # loading time
        self.passSplashScreen()
        Sleep(self.sb,3)
        self.setup()
        self.checkFinEles()
        # self.checkFin()
        Sleep(self.sb,3)
        self.findFinBal()
        self.calculateWinnings()

    def findSplashLoaded(self):
        self.sb.switch_to_frame('iframe')
        while not self.sb.is_element_visible(self.spinStr):
            Sleep(self.sb,2)
            self.defaultClick()

    def passSplashScreen(self):
        self.defaultClick()
        Sleep(self.sb)
        self.defaultClick()

    def setup(self):
        self.clickBonus()
        Sleep(self.sb)
        self.clickBonusCard()
        Sleep(self.sb)
        self.clickConfirm()

    # def checkFin(self):
    #     while True:
    #         try:
    #             Sleep(self.sb,2)
    #             self.defaultClick()
    #             if self.sb.is_element_present(self.counterStr):
    #                 counterNum = self.sb.find_element(self.counterStr).text
    #             elif self.sb.is_element_present(self.balanceStr):
    #                 break
    #         except:
    #             print(f'{self.slotCode}, error in checkfin')

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
        balance = self.sb.find_element(self.balanceStr).text
        self.endingBalance = cleanNumber(balance)
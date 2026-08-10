from classes.nesting.Slot import Slot
from utilityFunctions import Sleep
from classes.classUtilityFunctions import cleanNumber

class ZeroxEdge(Slot):
    def __init__(self, sb, slotCode, obs):
        super().__init__(sb, slotCode, obs)
        self.turboStr = 'button[aria-label="Turbo mode"]'
        self.autoStr = 'button[aria-label="Autoplay"]'
        self.startStr = '//button[contains(@class,"start-btn")]'
        self.confirmStr = '//button[contains(@class,"confirm-yes")]'
        self.bonusStr = '//button[contains(@class,"bonus-outline-btn")]'
        self.counterStr = '//button[contains(@class,"play-btn-circle")]/span[contains(@class,"fs-btn-counter")]/span[contains(@class,"fs-btn-num") and not(contains(@class,"fs-btn-total"))]'
        self.balanceStr = '//div[contains(@class,"bar-left")]/div[contains(@class,"info-stack")]/div[contains(@class,"info-row")]/span[contains(@class,"info-value")]'

    def clickTurbo(self):
        self.sb.find_element(self.turboStr).click()

    def clickAuto(self):
        self.sb.find_element(self.autoStr).click()

    def clickStart(self):
        self.sb.find_element(self.startStr).click()

    def clickBonus(self):
        self.sb.find_element(self.bonusStr).click()

    def clickBonusCard(self):
        # needs to be here otherwise it will initialize bonusCardStr as 1, the init value
        self.bonusCardStrBody = f'//div[contains(@class, "tiles-grid")]/div[{self.bonusOption}]/div[contains(@class, "tile-body")]/button'
        self.bonusCardStrFooter = f'//div[contains(@class, "tiles-grid")]/div[{self.bonusOption}]/div[contains(@class, "tile-footer")]/button'
        if self.sb.is_element_present(self.bonusCardStrBody):
            self.sb.find_element(self.bonusCardStrBody).click()
        if self.sb.is_element_present(self.bonusCardStrFooter):
            self.sb.find_element(self.bonusCardStrFooter).click()

    def clickConfirm(self):
        self.sb.find_element(self.confirmStr).click()

    def checkStart(self):
            while True:
                Sleep(self.sb,2)
                self.defaultClick()
                if self.sb.is_element_present(self.counterStr):
                    self.sb.find_element(self.counterStr)
                    break

    def checkFin(self):
        while True:
            try:
                Sleep(self.sb,2)
                self.defaultClick()
                if self.sb.is_element_present(self.counterStr):
                    counterNum = self.sb.find_element(self.counterStr).text
                elif self.sb.is_element_present(self.balanceStr):
                    break
            except:
                print(f'{self.slotCode}, error in checkfin')

    def findFinBal(self):
            balance = self.sb.find_element(self.balanceStr).text
            self.endingBalance = cleanNumber(balance)

    def passSplashScreen(self):
        self.sb.switch_to_frame('iframe')
        self.defaultClick()
        Sleep(self.sb)
        self.defaultClick()

    def setup(self):
        self.clickBonus()
        Sleep(self.sb)
        self.clickBonusCard()
        Sleep(self.sb)
        self.clickConfirm()
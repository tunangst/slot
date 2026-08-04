from classes.nesting.ZeroxEdge import ZeroxEdge
from classes.classUtilityFunctions import takePicture, compareImages, cleanNumber
from utilityFunctions import Sleep, MarkTheDom,ClickTheDom

slotCode = '0xedge-super-candy-drop'

class SuperCandyDrop(ZeroxEdge):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 213
        self.estimatedWaitTime = 35
        self.bonusOption = 5
        self.canvasStr = '//canvas'
        self.bonusCardStr = f'//div[contains(@class, "tiles-grid")]/div[{self.bonusOption}]/div[contains(@class, "tile-body")]/button'
        self.counterStr = '//button[contains(@class,"play-btn-circle")]/span[contains(@class,"fs-btn-counter")]/span[contains(@class,"fs-btn-num") and not(contains(@class,"fs-btn-total"))]'
        self.inProgressClickableStr = '//div[contains(@class,"board-layer")]'
        self.checkEndFlag = False
        
        self.changeScene() # take the screen blocks off
        self.runSleepThree()
        self.passSplashScreen()
        self.runSleepThree()
        self.setup()
        # self.runSleepMain()
        # self.run()
        # Sleep(sb, self.estimatedWaitTime)
        self.checkStart()
        self.checkFin()
        self.runSleepThree()
        self.findFinBal()

    def passSplashScreen(self):
        self.sb.switch_to_frame('iframe')
        self.defaultClick()
        Sleep(self.sb)
        self.defaultClick()

    def setup(self):
        self.clickBonus()
        self.runSleepOne()
        self.clickBonusCard()
        self.runSleepOne()
        self.clickConfirm()

    def checkStart(self):
        while True:
            Sleep(self.sb,2)
            self.defaultClick()
            counterStatus = self.sb.is_element_present(self.counterStr)
            if counterStatus:
                self.sb.find_element(self.counterStr)
                break

    def checkFin(self):
        while True:
            Sleep(self.sb,2)
            # when it ends, this is no longer clickable, I need to find a reoccurring clickable element or cycle through them with is_element_presents
            self.defaultClick()
            if self.sb.is_element_present(self.counterStr):
                try:
                    counterNum = self.sb.find_element(self.counterStr).text
                    self.checkEndFlag = False
                except:
                    continue
            else:
                if not self.checkEndFlag:
                    self.checkEndFlag = True
                else:
                    break

    def findFinBal(self):
        balanceStr = '//div[contains(@class,"bar-left")]/div[contains(@class,"info-stack")]/div[contains(@class,"info-row")]/span[contains(@class,"info-value")]'
        while not self.sb.is_element_present(balanceStr):
            Sleep(self.sb,2)
            print('not present, still loading')
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
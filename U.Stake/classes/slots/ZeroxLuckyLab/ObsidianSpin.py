from classes.nesting.ZeroxLuckyLab import ZeroxLuckyLab
from classes.classUtilityFunctions import cleanNumber
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '0xluckylab-obsidian-spin'
winningScreenshot = 'fin'
closingWordsList = ['totalwin','total win']

class ObsidianSpin(ZeroxLuckyLab):
    def __init__(self, sb, obs):
        Sleep(sb,2)
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 30
        self.estimatedWaitTime = 60
        self.bonusOption = 3
        
        self.changeScene() # take the screen blocks off
        self.runSleepMain()
        self.passSplashScreen()
        self.runSleepThree()
        self.setup()
        # Sleep(self.sb,3)
        # self.run()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin()
        self.runSleepThree()
        self.findFinBal()

    def setup(self):              
        bonusStr = '//div[contains(@class,"right-controls")]/div[contains(@class, "button-stack")]/button[@title="Modes"]'
        self.sb.find_element(bonusStr).click()
        self.runSleepOne()
        bonusCardStr = f'//div[contains(@class,"modal-body")]//div[contains(@class, "mode-cards")]/div[{self.bonusOption}]/div[contains(@class,"mode-card-right")]/button'
        self.sb.find_element(bonusCardStr).click()
        self.runSleepOne()
        yesStr = '//button[contains(text(), "Confirm")]'
        self.sb.find_element(yesStr).click()

        self.runSleepMain()
        # set up turbo speed
        settingBtn = '//button[@title="Settings"]'
        self.sb.find_element(settingBtn).click()
        self.runSleepOne()
        speedBtn = '//button[@aria-label="Spin Speed"]'
        self.sb.find_element(speedBtn).click()
        self.runSleepOne()
        closeBtn = '//button[@aria-label="Close"]'
        self.sb.find_element(closeBtn).click()
        self.runSleepOne()
        autoSpin = '//div[contains(@class,"right-controls")]/div[contains(@class,"button-stack")]/button[@title="Auto Play"]'
        self.sb.find_element(autoSpin).click()
        self.runSleepOne()
        numBar = f'//div[contains(@class,"modal-content")]/div[contains(@class,"modal-body")]/div[contains(@class,"rounds-grid")]/button[contains(., "{self.spinCount}")]'
        self.sb.find_element(numBar).click()
        self.runSleepOne()
        startBar = '//div[contains(@class,"modal-content")]/div[contains(@class,"modal-footer")]//button'
        self.sb.find_element(startBar).click()

    def run(self):
        pass

    def checkFin(self):
        spinCountStr = 'span.autoplay-counter-overlay'
        count = self.spinCount
        while count > 0:
            try:
                countText = self.sb.find_element(spinCountStr).text
                countInt = int(countText)
                count = countInt
                Sleep(self.sb,5)
            except:
                count = 0
                print('counter has been removed')

    def findFinBal(self):
        balanceStr = '//div[contains(@class,"info-display-container")]/div[contains(@class,"info-content")]/div[contains(@class,"info-row")]/div[contains(@class,"info-item-inline")]/span[@class="info-value"]'
        balance = self.sb.find_element(balanceStr).text
        self.endingBalance = cleanNumber(balance)
        self.finalBalance = self.endingBalance - self.startingBalance
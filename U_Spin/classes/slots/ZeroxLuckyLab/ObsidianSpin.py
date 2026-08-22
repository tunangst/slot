from classes.nesting.ZeroxLuckyLab import ZeroxLuckyLab
from classes.classUtilityFunctions import cleanNumber
from utilityFunctions import Sleep

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
        self.findSplashLoaded()
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin(crop=slotCode)
        Sleep(sb,3)
        self.findFinBal()
        self.calculateWinnings()

    def defaultClick(self):
        self.sb.find_element('body').click()

    def findSplashLoaded(self):
        spinStr = '//button[contains(@class,"btn-play")]'
        self.sb.switch_to_frame('iframe')
        while not self.sb.is_element_visible(spinStr):
            Sleep(self.sb,2)
            self.defaultClick() 

    def setup(self):              
        bonusStr = '//div[contains(@class,"right-controls")]/div[contains(@class, "button-stack")]/button[@title="Modes"]'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        bonusCardStr = f'//div[contains(@class,"modal-body")]//div[contains(@class, "mode-cards")]/div[{self.bonusOption}]/div[contains(@class,"mode-card-right")]/button'
        self.sb.find_element(bonusCardStr).click()
        Sleep(self.sb)
        yesStr = '//button[contains(text(), "Confirm")]'
        self.sb.find_element(yesStr).click()

        Sleep(self.sb,15)
        # set up turbo speed
        settingBtn = '//button[@title="Settings"]'
        self.sb.find_element(settingBtn).click()
        Sleep(self.sb)
        speedBtn = '//button[@aria-label="Spin Speed"]'
        self.sb.find_element(speedBtn).click()
        Sleep(self.sb)
        closeBtn = '//button[@aria-label="Close"]'
        self.sb.find_element(closeBtn).click()
        Sleep(self.sb)
        autoSpin = '//div[contains(@class,"right-controls")]/div[contains(@class,"button-stack")]/button[@title="Auto Play"]'
        self.sb.find_element(autoSpin).click()
        Sleep(self.sb)
        numBar = f'//div[contains(@class,"modal-content")]/div[contains(@class,"modal-body")]/div[contains(@class,"rounds-grid")]/button[contains(., "{self.spinCount}")]'
        self.sb.find_element(numBar).click()
        Sleep(self.sb)
        startBar = '//div[contains(@class,"modal-content")]/div[contains(@class,"modal-footer")]//button'
        self.sb.find_element(startBar).click()

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
from classes.Slot import Slot
from classes.classUtilityFunctions import cleanNumber
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = ''
winningScreenshot = 'fin'
closingWordsList = ['totalwin','total win']

class Template(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = False
        self.estimatedWaitTime = 30
        # need to pass two splash screens
        self.changeScene() # take the screen blocks off
        Sleep(self.sb,3)
        self.passSplashScreen()
        Sleep(self.sb,3)
        self.setup()
        Sleep(self.sb,3)
        self.run()
        # while check for same screenshots to see if game ended
        # record ending balance

    def setup(self):
        # click bonus
        bonusOption = 3
        bonusStr = 'button[aria-label="Open BONUS"]'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        # choose scatter
        # frame-bonus__grid > artical > frame-bonus__card-body > frame-bonus__card-footer > button
        scatterStr = '//article[@data-offer-id="bonus3"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        # scatterStr = f'(//div[contains(@class, "tiles-row")]/div[{bonusOption}]//div[contains(@class, "tile-body")]//button)[1]'
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb)
        yesStr = 'button.frame-confirm__accept'
        self.sb.find_element(yesStr).click()

    def run(self):
        Sleep(self.sb,15)
        # find play btn
        canvasStr = '#game'
        canvas = self.sb.find_element(canvasStr).click()
       
        Sleep(self.sb, self.estimatedWaitTime)
        self.checkFin(closingWordsList)
        # find what was won
        self.findFinBal()

    def findFinBal(self):
        alanceStr = '//div[contains(@class,"bar-left")]/div[contains(@class,"info-stack")]/div[contains(@class,"info-row")]/span[contains(@class,"info-value")]'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
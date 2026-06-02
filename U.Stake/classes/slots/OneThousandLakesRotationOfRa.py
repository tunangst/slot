from classes.Slot import Slot
from classes.classUtilityFunctions import cleanNumber
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '1000lakes-rotation-of-ra'
winningScreenshot = 'fin'
closingWordsList = ['totalwin','total win']

class OneThousandLakesRotationOfRa(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 500
        self.estimatedWaitTime = 240
        # need to pass two splash screens
        self.changeScene() # take the screen blocks off
        Sleep(self.sb,3)
        self.passSplashScreen()
        self.setup()
        self.run()
        # while check for same screenshots to see if game ended
        # record ending balance

    def setup(self):
        # enable turbo
        optionStr = 'button[aria-label="Open menu"]'
        self.sb.find_element(optionStr).click()
        turboStr = 'span.frame-icon--turbo'
        self.sb.find_element(turboStr).click()
        closeStr = 'span.frame-icon--close'
        self.sb.find_element(closeStr).click()
        # click bonus
        bonusStr = 'button[aria-label="Open bonus shop"]'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        # choose scatter
        scatterStr = '//article[@data-offer-id="buy_12fs"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
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
        # winBlockStr = 'div[data-variant="win"]'
        # winBlock = self.sb.find_element(winBlockStr)
        # winTxt = winBlock.text
        # win = cleanNumber(winTxt)
        # self.winnings = win

        Sleep(self.sb,5)
        canvasStr = 'canvas#game'
        self.sb.find_element(canvasStr).click()

        Sleep(self.sb,5)
        balanceStr = 'span.frame-hud__display-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
from classes.Slot import Slot
from classes.classUtilityFunctions import cleanNumber
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '1000lakesstudios-candy-carnival-spring-spritz'
winningScreenshot = 'fin'
closingWords = ['total win', 'totalwin']

class OneThousandLakesStudioCandyCarnivalSpringSpritz(Slot):
    def __init__(self, sb, obs):
        Sleep(sb,3)
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 500
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
        Sleep(self.sb,3)
        bonusStr = 'button.game-buttons__bonus'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        # choose scatter
        scatterStr = '//article[@data-offer-id="super_modifier"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
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
        self.checkFin(closingWords)
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
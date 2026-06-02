from classes.Slot import Slot
from classes.classUtilityFunctions import takePicture, clickDomElement, cleanNumber
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
import re

slotCode = '1000lakesstudios-disco-cubes'
winningScreenshot = 'fin'
closingWords = ['total win']

class OneThousandLakesStudiosDiscoCubes(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 500
        self.estimatedWaitTime = 90
        # need to pass two splash screens
        # add more time to pass splash screen
        self.changeScene() # take the screen blocks off
        Sleep(sb,5)
        self.passSplashScreen()
        self.setup()
        self.run()
        # while check for same screenshots to see if game ended
        # record ending balance

    def setup(self):
        # click bonus
        bonusOption = 3
        bonusStr = 'button.game-buttons__bonus'
        self.sb.find_element(bonusStr).click()
        # choose scatter
        scatterStr = '//article[@data-offer-id="buy_12fs"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb,3)
        yesStr = 'button.frame-confirm__accept'
        self.sb.find_element(yesStr).click()

    def run(self):
        Sleep(self.sb,15)
        # find play btn
        canvasStr = '#game'
        canvas = self.sb.find_element(canvasStr)
        info = clickDomElement(sb=self.sb,selector=canvasStr)
       
        Sleep(self.sb, self.estimatedWaitTime)
        self.checkFin()
        # find what was won
        self.findFinBal()

    def checkFin(self):
        # need to keep element inside the loop due to needing to rerefrence the element
        pattern = r'^(\d+)/\1$'
        counterStr = '//button[@aria-label="SPIN"]/span[contains(@class,"frame-hud__spin-label--counter")]'
        while True:
            Sleep(self.sb, 10)
            counter = self.sb.find_element(counterStr)
            value = counter.text
            if re.match(pattern, value):
                return
            else:
                print(f'Not quite finished checking if finished: {value}')

    def findFinBal(self):
        # winStr = 'div.frame-hud__display--win > span.frame-hud__display-value'
        # winEle = self.sb.find_element(winStr)
        # val = cleanNumber(winEle.text)
        # self.winnings = val
        Sleep(self.sb,10)
        canvasStr = '#game'
        self.sb.find_element(canvasStr).click()
        Sleep(self.sb,30)
        balanceStr = 'span.frame-hud__display-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
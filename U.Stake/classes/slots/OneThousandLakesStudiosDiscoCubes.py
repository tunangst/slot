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
        self.canvasStr = 'canvas#game'
        
        self.changeScene() # take the screen blocks off
        Sleep(sb,5)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb,15)
        self.run()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin()
        Sleep(sb,15)
        self.findFinBal()

    def setup(self):
        bonusStr = 'button.game-buttons__bonus'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        scatterStr = '//article[@data-offer-id="buy_12fs"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb)
        yesStr = 'button.frame-confirm__accept'
        self.sb.find_element(yesStr).click()

    def run(self):
        self.sb.find_element(self.canvasStr)
        clickDomElement(sb=self.sb,selector=self.canvasStr)

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
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,30)
        balanceStr = 'span.frame-hud__display-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
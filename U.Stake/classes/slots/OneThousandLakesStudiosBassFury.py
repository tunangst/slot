from classes.Slot import Slot
from classes.classUtilityFunctions import takePicture, clickDomElement, cleanNumber
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
import re

slotCode = '1000lakesstudios-bass-fury'
winningScreenshot = 'fin'
closingWords = ['the big catch over'] # 'totalwin'

class OneThousandLakesStudiosBassFury(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 250
        self.estimatedWaitTime = 50
        self.canvasStr = 'canvas#game'

        self.changeScene() # take the screen blocks off
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb,17)
        self.run()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin(closingWords)
        Sleep(sb,5)
        self.findFinBal()

    def setup(self):
        bonusStr = 'button.game-buttons__bonus'
        self.sb.find_element(bonusStr).click()
        Sleep(self.sb)
        scatterStr = '//article[@data-offer-id="buy_ultimate"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'        
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb)
        yesStr = 'button.frame-confirm__accept'
        self.sb.find_element(yesStr).click()

    def run(self):
        clickDomElement(sb=self.sb,selector=self.canvasStr)

    def findFinBal(self):
        self.sb.find_element(self.canvasStr).click()
        Sleep(self.sb,5)
        balanceStr = 'span.frame-hud__display-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance

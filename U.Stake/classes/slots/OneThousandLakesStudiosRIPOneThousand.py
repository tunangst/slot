from classes.Slot import Slot
from classes.classUtilityFunctions import clickDomElement, cleanNumber, findEmbeddedCoords
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom,ClickTheDom
import re

slotCode = '1000lakesstudios-r-i-p-1000'
winningScreenshot = 'fin'
bonusWords = ['getbonus','get bonus']
closingWords = ['freespinsover'] # 'totalwin'
findWord = ['total win','totalwin']


class OneThousandLakesStudiosRIPOneThousand(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 500
        self.estimatedWaitTime = 60
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
        xVal, yVal = findEmbeddedCoords(sb=self.sb,checkWordList=bonusWords)
        # switch it to take full screenshot and mark the click location
        ClickTheDom(sb=self.sb,xVal=xVal,yVal=yVal)
        Sleep(self.sb)
        # the rest are in dom
        scatterStr = '//article[@data-offer-id="super_buy"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'        
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

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
        self.startingBalance = 1000.00
        self.estimatedWaitTime = 60
        # need to pass two splash screens
        # add more time to pass splash screen
        Sleep(sb,3)
        self.changeScene() # take the screen blocks off
        self.passSplashScreen()
        self.setup()
        self.run()
        # while check for same screenshots to see if game ended
        # record ending balance

    def setup(self):
        Sleep(self.sb,3)
        xVal, yVal = findEmbeddedCoords(sb=self.sb,checkWordList=bonusWords)
        # switch it to take full screenshot and mark the click location
        ClickTheDom(sb=self.sb,xVal=xVal,yVal=yVal)
        # the rest are in dom
        # choose scatter
        scatterStr = '//article[@data-offer-id="super_buy"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'        
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb)
        yesStr = 'button.frame-confirm__accept'
        self.sb.find_element(yesStr).click()

    def run(self):
        Sleep(self.sb,17)
        # find play btn
        canvasStr = '#game'
        clickDomElement(sb=self.sb,selector=canvasStr)
       
        Sleep(self.sb, self.estimatedWaitTime)
        self.checkFin(closingWords)
        # find what was won
        self.findWinnings()

    def findWinnings(self):
        location = './U.Stake/images/checkFin.png'
        cap = Capture(imageLocation=location,action='find next',targetWordList=findWord)
        winTxt = cap.targetBlock['text']
        val = cleanNumber(winTxt)
        self.winnings = val
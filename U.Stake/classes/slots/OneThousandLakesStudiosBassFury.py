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
        # need to pass two splash screens
        # add more time to pass splash screen
        self.changeScene() # take the screen blocks off
        Sleep(sb,3)
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
        # frame-bonus__grid > artical > frame-bonus__card-body > frame-bonus__card-footer > button
        scatterStr = '//article[@data-offer-id="buy_ultimate"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'        
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb)
        yesStr = 'button.frame-confirm__accept'
        self.sb.find_element(yesStr).click()

    def run(self):
        Sleep(self.sb,17)
        # find play btn
        canvasStr = '#game'
        info = clickDomElement(sb=self.sb,selector=canvasStr)
       
        Sleep(self.sb, self.estimatedWaitTime)
        self.checkFin(closingWords)
        # find what was won
        self.findFinBal()


    def findFinBal(self):
        # crop the screenshot because it will pull in date and other out of range options
        Sleep(self.sb,5)
        canvasStr = 'canvas#game'
        self.sb.find_element(canvasStr).click()
        # picLocation = takePicture(sb=self.sb,action='fin',fileName=winningScreenshot,eleStr=canvasStr)
        # cap = Capture(imageLocation=picLocation,action='find number')
        # winStr = cap.status
        # self.winnings = cleanNumber(cap.status)
        
        Sleep(self.sb,5)
        balanceStr = 'span.frame-hud__display-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance

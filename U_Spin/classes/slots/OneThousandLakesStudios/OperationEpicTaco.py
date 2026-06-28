from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios
from classes.classUtilityFunctions import takePicture, clickDomElement, cleanNumber
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
import re

slotCode = '1000lakesstudios-operation-epic-taco'
winningScreenshot = 'fin'
closingWords = ['the big catch over'] # 'total win'

class OperationEpicTaco(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 500
        self.estimatedWaitTime = 60
        self.canvasStr = 'canvas#game'
        
        self.changeScene() # take the screen blocks off
        self.runSleepThree()
        self.passSplashScreen()
        self.runSleepThree()
        self.setup()
        self.runSleepTwenty()
        self.run()
        Sleep(self.sb, self.estimatedWaitTime)
        self.checkFin()
        self.runSleepFive()
        self.findFinBal()

    def setup(self):
        self.clickBuyout()
        self.runSleepOne()
        scatterStr = '//article[@data-offer-id="bonus3"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'        
        self.sb.find_element(scatterStr).click()
        self.runSleepOne()
        self.clickConfirmBtn()

    def run(self):
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
        Sleep(self.sb,5)
        balanceStr = 'span.frame-hud__display-value'
        self.endingBalance = cleanNumber(self.sb.find_element(balanceStr).text)
        self.finalBalance = self.endingBalance - self.startingBalance
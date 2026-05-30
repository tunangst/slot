from classes.Slot import Slot
from classes.classUtilityFunctions import takePicture, clickDomElement, cleanNumber
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '1000lakesstudios-toivo'
winningScreenshot = 'fin'
closingWords = ['total win']

class OneThousandLakesStudiosToivo(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.startingBalance = 1000.00
        self.estimatedWaitTime = 30
        # need to pass two splash screens
        self.changeScene() # take the screen blocks off
        self.passSplashScreen()
        self.setup()
        self.run()
        # while check for same screenshots to see if game ended
        # record ending balance

    def passSplashScreen(self):
        Sleep(self.sb)
        bodyStr = 'body'
        self.sb.switch_to_frame('iframe')
        self.sb.find_element(bodyStr).click()
        Sleep(self.sb)
        skipStr = 'button.finnisher-intro__skip'
        self.sb.find_element(skipStr).click()

    def setup(self):
        # click bonus
        bonusOption = 3
        bonusStr = 'button.game-buttons__bonus'
        self.sb.find_element(bonusStr).click()
        # choose scatter
        # frame-bonus__grid > artical > frame-bonus__card-body > frame-bonus__card-footer > button
        scatterStr = '//article[@data-offer-id="buy_super"]/div[contains(@class, "frame-bonus__card-body")]/div[contains(@class, "frame-bonus__card-footer")]/button'
        # scatterStr = f'(//div[contains(@class, "tiles-row")]/div[{bonusOption}]//div[contains(@class, "tile-body")]//button)[1]'
        self.sb.find_element(scatterStr).click()
        Sleep(self.sb)
        yesStr = 'button.frame-confirm__accept'
        self.sb.find_element(yesStr).click()

    def run(self):
        Sleep(self.sb,15)
        # find play btn
        canvasStr = '#game'
        canvas = self.sb.find_element(canvasStr)
        info = clickDomElement(sb=self.sb,selector=canvasStr)
       
        Sleep(self.sb, self.estimatedWaitTime)
        self.checkFin(closingWords)
        # find what was won
        self.findWinnings()

    def findWinnings(self):
        picLocation = takePicture(sb=self.sb,action='custom',fileName=winningScreenshot)
        cap = Capture(imageLocation=picLocation,action='find number')
        winStr = cap.status
        self.winnings = cleanNumber(winStr)

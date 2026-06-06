import json
import time
from utilityFunctions import Sleep
from classes.classUtilityFunctions import takePicture, checkCaptcha, checkRegionChange
from classes.Capture import Capture

slotUrl = 'https://stake.com/casino/games/'
checkFinFileName = 'checkFin'

class Slot:
    def __init__(self, sb, slotCode, obs):
        self.sb = sb
        self.slotCode = slotCode
        self.obs = obs
        self.gameBoardInfo = None
        self.width = 0
        self.height = 0
        self.splashScreenCoords = (0,0)
        self.buyBonusCoords = (0,0)
        self.startingBalance = 1000.00
        self.buyoutBalance = 0
        self.endingBalance = 0
        self.winnings = 0
        self.finalBalance = 0

        #self.checkSlotNameInput(slotNameInput)
        self.loadSlotPage()
        Sleep(self.sb,10)
        checkCaptcha(self.sb)
        Sleep(self.sb, 3)
        checkRegionChange(self.sb)
        Sleep(self.sb, 3)
        self.fullScreen()
        self.findDimensions()

    def fullScreen(self):
        # find fullscreen btn and click it
        maximizeBtnIdentifier = '.game-footer > div > div > button'
        self.sb.find_element(maximizeBtnIdentifier).click()

    def findDimensions(self):
        Sleep(self.sb)
        bodyString = 'body'
        if self.sb.is_element_present(bodyString):
                body = self.sb.find_element(bodyString)
                self.gameBoardInfo = body.get_position()
        else:
            print('canvas element not found')

    def loadSlotPage(self):
        Sleep(self.sb)
        self.sb.open(slotUrl + self.slotCode)
        # self.sb.minimize_window()

    def passSplashScreen(self):
        # Sleep(self.sb,2)
        bodyStr = 'body'
        self.sb.switch_to_frame('iframe')
        continueBtn = self.sb.find_element(bodyStr)
        continueBtn.click()

    def run(self):
        pass

    def checkFin(self, closingWordsList,eleStr=False):
        while True:
            # compare screenshots
            if eleStr:
                picLocation = takePicture(sb=self.sb,action='custom',fileName=checkFinFileName,eleStr=eleStr)
            else:
                picLocation = takePicture(sb=self.sb,action='custom',fileName=checkFinFileName)
                # look for Click, Continue, etc
            instance = Capture(imageLocation=picLocation,action='check end words',targetWordList=closingWordsList)
            # if instance:
            if instance.fin:
                return True
            Sleep(self.sb,5)

    def findWinnings(self):
        pass

    def findFinBal(self):
        pass

    def changeScene(self):
        # obs scene codes here
        self.obs.runMainScene()
        pass

    def timedScreenCheck(self,timeout,checkWordsList,eleStr):
        counter = timeout
        end_time = time.monotonic() + counter
        while True:
            remaining = max(0, int(end_time - time.monotonic()))
            seconds = remaining % 60
            timerText = f'{seconds}'
            print(timerText, end='\r')
            if remaining == 0:
                break
            time.sleep(0.1)

            # compare screenshots
            picLocation = takePicture(sb=self.sb,action='tmp',eleStr=eleStr)
            # look for Click, Continue, etc
            instance = Capture(imageLocation=picLocation,action='check end words',closingWordsList=checkWordsList)
            # if instance:
            if instance.fin:
                self.sb.find_element(eleStr).click()
            Sleep(self.sb,5)
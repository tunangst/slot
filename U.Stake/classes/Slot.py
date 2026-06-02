import json
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
        # check captcha, if so solve
        checkCaptcha(self.sb)
        # Sleep(sb, 4)
        checkRegionChange(self.sb)
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
        Sleep(self.sb,2)
        bodyStr = 'body'
        self.sb.switch_to_frame('iframe')
        continueBtn = self.sb.find_element(bodyStr)
        continueBtn.click()

    def run(self):
        pass

    def checkFin(self, closingWordsList):
        while True:
            Sleep(self.sb,10)
            # compare screenshots
            picLocation = takePicture(sb=self.sb,action='custom',fileName=checkFinFileName)
            # look for Click, Continue, etc
            instance = Capture(imageLocation=picLocation,action='check end words',closingWordsList=closingWordsList)
            # if instance:
            if instance.fin:
                return

    def findWinnings(self):
        pass

    def findFinBal(self):
        pass

    def changeScene(self):
        # obs scene codes here
        self.obs.runMainScene()
        pass
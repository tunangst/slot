import json
import time
from utilityFunctions import Sleep, ClickTheDom
from classes.classUtilityFunctions import takePicture, checkCaptcha, checkRegionChange
from classes.Capture import Capture

slotUrl = 'https://stake.com/casino/games/'

class Slot:
    def __init__(self, sb, slotCode, obs):
        self.sb = sb
        self.slotCode = slotCode
        self.obs = obs
        self.canvasStr = 'canvas'
        self.buyoutBalance = 0
        self.startingBalance = 1000.00
        self.endingBalance = 0
        self.winnings = 0
        self.bonusOption = 1
        self.domAdjustment = 1
        self.betValue = 1
        self.spinCount = 50
        self.defaultClickCoords = (0,0)

        self.loadSlotPage()
        checkCaptcha(sb)
        checkRegionChange(sb)
        self.fullScreen()
        self.findDimensions()
        self.setDefaultClick()

    def fullScreen(self):
        maximizeBtnIdentifier = '//div[contains(@class,"game-footer")]/div/div/button'
        self.sb.find_element(maximizeBtnIdentifier).click()

    def findDimensions(self):
        Sleep(self.sb)
        bodyString = 'body'
        if self.sb.is_element_present(bodyString):
            body = self.sb.find_element(bodyString)
            self.gameBoardInfo = body.get_position()
        else:
            print('canvas element not found')

    def setDefaultClick(self):
        x = self.gameBoardInfo.width * .5
        y = self.gameBoardInfo.height * .025
        self.defaultClickCoords = (x,y)

    def loadSlotPage(self):
        Sleep(self.sb)
        self.sb.open(slotUrl + self.slotCode)

    def passSplashScreen(self):
        # self.sb.switch_to_frame('iframe')
        self.defaultClick()

    def run(self):
        self.defaultClick()

    def checkFin(self, closingWordsList,eleStr=False):
        while True:
            # compare screenshots
            picLocation = takePicture(sb=self.sb,action='check fin',eleStr=eleStr)
            # look for Click, Continue, etc
            instance = Capture(imageLocation=picLocation,action='check end words',targetWordList=closingWordsList)
            # if instance:
            if instance.fin:
                return True
            Sleep(self.sb,5)
            self.defaultClick()

    def checkStuckAndFin(self,checkList,finList):
        while True:
            picLocation = takePicture(sb=self.sb,action='check fin')
            checkInstance = Capture(imageLocation=picLocation,action='check all words',targetWordList=checkList)
            if checkInstance.fin:
                self.sb.find_element(self.canvasStr).click()
            else:
                finInstance = Capture(imageLocation=picLocation,action='check end words',targetWordList=finList)
                if finInstance.fin:
                    break

    def checkFiftyFin(self,spinWordsList):
        countStr = '//div[contains(@class,"icon-spin")]/div[contains(@class,"mg-stop-icon")]/span'
        stuck = False
        finCheck = False
        while True:
            try:
                checkCount = self.sb.find_element(countStr).text
                print(checkCount)
                Sleep(self.sb,5)
                if checkCount == stuck:
                    self.sb.find_element(self.canvasStr).click()
                stuck = checkCount
            except:
                try:
                    picLocation = takePicture(sb=self.sb,action='check fin')
                    instance = Capture(imageLocation=picLocation,action='check end words',targetWordList=spinWordsList)
                    if instance.fin: 
                        self.sb.find_element(self.canvasStr).click()
                    else:
                        if finCheck:
                            break
                        else:
                            finCheck = True
                except:
                    break

    def findFinBal(self):
        pass

    def changeScene(self):
        self.obs.runMainScene()

    def passTriangleScreen(self):
        canvas = self.sb.find_element(self.canvasStr)
        x = canvas.size['width'] * .5 # 50%
        y = canvas.size['height'] * .80 # 80%
        ClickTheDom(sb=self.sb,xVal=x,yVal=y)

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

    def defaultClick(self):
        ClickTheDom(sb=self.sb,xVal=self.defaultClickCoords[0],yVal=self.defaultClickCoords[1])

    def calculateWinnings(self):
        self.winnings = self.startingBalance - self.endingBalance
        pass
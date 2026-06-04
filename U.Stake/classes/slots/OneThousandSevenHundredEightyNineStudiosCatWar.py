from classes.Slot import Slot
from classes.classUtilityFunctions import cleanNumber, takePicture, findEmbeddedCoords
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom, ClickTheDom
from selenium.webdriver.common.action_chains import ActionChains

slotCode = '1789studios-cat-war'
winningScreenshot = 'fin'
closingWordsList = ['complete']
nextWordList = ['base bet'] # base bet    
bonusWords = ['bonus buy','bonus']
scatterWords = ['10 spins']
confirmWords = ['confirm']

class OneThousandSevenHundredEightyNineStudiosCatWar(Slot):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.buyoutBalance = 180
        self.estimatedWaitTime = 30
        self.canvasStr = 'canvas'

        self.changeScene() # take the screen blocks off
        Sleep(sb,3)
        self.passSplashScreen()
        Sleep(sb,3)
        self.setup()
        Sleep(sb,15)
        self.run()
        Sleep(sb, self.estimatedWaitTime)
        self.checkFin(closingWordsList)
        Sleep(sb,3)
        self.sb.find_element(self.canvasStr).click()
        Sleep(sb,5)
        self.findFinBal()

    def setup(self):
        xValBonus, yValBonus = findEmbeddedCoords(sb=self.sb,checkWordList=bonusWords)
        # switch it to take full screenshot and mark the click location
        ClickTheDom(sb=self.sb,xVal=xValBonus,yVal=yValBonus)
        Sleep(self.sb,3)
        xValScatter, yValScatter = findEmbeddedCoords(sb=self.sb,checkWordList=scatterWords)
        ClickTheDom(sb=self.sb,xVal=xValScatter,yVal=yValScatter)
        Sleep(self.sb,3)
        xValConfirm, yValConfirm = findEmbeddedCoords(sb=self.sb,checkWordList=confirmWords)
        ClickTheDom(sb=self.sb,xVal=xValConfirm,yVal=yValConfirm)

    def run(self):
        self.sb.find_element(self.canvasStr).click()

    def findFinBal(self):
        picLocation = takePicture(sb=self.sb,action='fin')
        cap = Capture(imageLocation=picLocation,action='find next',targetWordList=nextWordList)
        winStr = cap.targetBlock
        self.endingBalance = cleanNumber(winStr['text'])
        self.finalBalance = self.endingBalance - self.startingBalance
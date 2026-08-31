from classes.nesting.OneThousandLakesStudios import OneThousandLakesStudios
from classes.classUtilityFunctions import findEmbeddedCoords, takePicture
from utilityFunctions import Sleep,ClickTheDom
from classes.Capture import Capture

slotCode = '1000lakesstudios-r-i-p-1000'
bonusWords = ['getbonus','get bonus','getbonos','get bonos']

class RIPOneThousand(OneThousandLakesStudios):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.run()

    def setup(self):
        xVal, yVal = findEmbeddedCoords(sb=self.sb,checkWordList=bonusWords)
        # switch it to take full screenshot and mark the click location
        ClickTheDom(sb=self.sb,xVal=xVal,yVal=yVal)
        Sleep(self.sb)
        self.clickBonusCard()
        Sleep(self.sb)
        self.clickConfirmBtn()

    def checkFin(self,crop,action='find any text',targetWordList=False):
        startSwitch = False
        endSwitch = 0 # 0-3
        endSwitchLimit = 3
        while True:
            try:
                self.defaultClick()
                Sleep(self.sb,3)
                # screenshot the spin count
                picLocation = takePicture(sb=self.sb,action='check fin',crop=crop)
                instance = Capture(imageLocation=picLocation,action=action,targetWordList=targetWordList)
                if instance.textBlocks[0]['text'].lower() in bonusWords:
                    break
                elif instance.status: # count number is present
                    startSwitch = True
                    endSwitch = 0
                elif endSwitch >= endSwitchLimit:
                    break
                elif startSwitch == True:
                    endSwitch += 1
            except:
                print(f'{self.slotCode}, error in checkfin')
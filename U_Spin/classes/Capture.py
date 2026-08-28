from utilityFunctions import GetRandomNumber
from PIL import Image
from paddleocr import PaddleOCR
import logging

logging.getLogger("ppocr").setLevel(logging.ERROR)

ssDir = './U.Stake/images/screenshots/'

# Variables
# ss
# ocr
# textBlocks
# clickTarget

class Capture:
    def __init__(self, imageLocation, action=False, targetWordList=False):
        self.ocr = PaddleOCR(
            use_doc_orientation_classify=False,
            use_doc_unwarping=False,
            use_textline_orientation=False,
            engine="transformers",
        )
        self.action = action
        self.imageLocation = imageLocation
        self.targetWordList = targetWordList
        self.textBlocks = []
        self.textBlocksRange = 0
        self.targetBlock = {}
        self.imgHeight = 0
        self.imgWidth = 0
        self.image = False
        self.fin = False
        self.status = False

        self.run()

    def run(self):
        self.openImg()
        self.getPicSize()
        self.extractText()

        # account for the cases where the screenshot is taken and does not find words
        if not self.textBlocksRange:
            return False

        match self.action:
            case 'find shape':
                pass
            case 'find number':
                self.status = self.findNumber()
            case 'find any text':
                self.status = self.textBlocks[0]
            case 'find next':
                self.status = self.findNext()
            case 'check end words':
                self.status = self.checkGameEndWords()
            case 'check all words':
                self.status = self.checkAllWords()
            case _:
                print('no action given to Capture')


    def openImg(self):
        try:
            self.image = Image.open(self.imageLocation)
        except:
            print(f'no image found at location: {ssDir}{self.image}')

    def getPicSize(self):
        self.imgWidth, self.imgHeight = self.image.size

    def extractText(self):
        fullTxtArr = []
        allText = self.ocr.ocr(self.imageLocation)[0]
        if allText == None:
            return
        # Loop through detected text areas
        for i in range(len(allText)):
            block = allText[i]
            # loop over all of the allText and do the others
            # Bounding box coordinates
            box = block[0]
            # Detected text
            text = block[1][0]
            # Confidence score
            confidence = block[1][1]
            textObj = {
                'text': text,
                'confidence': confidence,
                'box': box
            }
            fullTxtArr.append(textObj)
            print("TEXT:", text)
            print("CONFIDENCE:", confidence)
            print("BOX:", box)
            print("------------------")
        self.textBlocks = fullTxtArr
        self.textBlocksRange = range(len(self.textBlocks))

    def checkGameEndWords(self):
        # loop over textBlocks and see if any match the words in targetWords
        
        for i in self.textBlocksRange:
            block = self.textBlocks[i]
            lowerText = self.textBlocks[i]['text'].lower()
            # compare lowerText with each word in target words
            for word in self.targetWordList:
                if word in lowerText:
                    print(f'found word matching target words: {word}')
                    self.fin = True
                    self.targetBlock = block
                    return True
                
    def checkAllWords(self):
        yesList = []
        for i in self.textBlocksRange:
            block = self.textBlocks[i]
            lowerText = self.textBlocks[i]['text'].lower()
            # compare lowerText with each word in target words
            for word in self.targetWordList:
                if word in lowerText:
                    yesList.append(True)
        if len(yesList) == len(self.targetWordList):
            self.fin = True
            return True
        else:
            return False
    
    def findNumber(self):
        # loop over textBlocks and see if any match the words in targetWords
        for i in self.textBlocksRange:
            block = self.textBlocks[i]
            text = self.textBlocks[i]['text']
            try:
                targetValue = text
                if text[0] == '$':
                    targetValue = text[1:] 
                floatValue = float(targetValue)
                return floatValue
            except:
                print(f'this increment did not find a number in findNumber: {text}')
                return False
        
    def findNext(self):
        for i in self.textBlocksRange:
            block = self.textBlocks[i]
            lowerText = self.textBlocks[i]['text'].lower()
            # compare lowerText with each word in target words
            for word in self.targetWordList:
                if word in lowerText:
                    print(f'found word matching target words: {lowerText}, I will send the next text')
                    self.fin = True
                    self.targetBlock = self.textBlocks[i+1]
                    return
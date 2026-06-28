from classes.classUtilityFunctions import checkCaptcha, checkRegionChange, Sleep, splitSlotNames
from utilityFunctions import SaveFile
import json

stake = 'https://stake.com/casino/group/slots'
voidNames = ["Play'n Go","Stacy's Cookies"]

class ScrapeSlots:
    def __init__(self, sb):
        self.locationName = 'slotdata.json'
        self.sb = sb
        self.providerBtnStr = '//div[contains(@id, "main-content")]/div/div/div/div/div/button/span'
        self.providerNameStr = '//div[contains(@class,"provider-list")]/div/label/span/p/div/span'
        self.cutPubListInd = 13
        self.pubNameLabelStr = ''
        self.loadMoreEle = '//div[contains(@class,"load-more-container")]/button'
        self.slotCard = '//div[contains(@class,"game-card-wrap")]//div[contains(@class,"img-wrap")]'
        # self.slotCard = '//div[contains(@id,"main-content")]/div/div[4]/div[2]'
        self.publisherList = []
        self.slotId = ''
        self.slotInfoObj = {}
        self.slotNames = []
        # self.fullSlotList = []
        # self.finalSlotList = []

        sb.open(stake)
        checkCaptcha(sb)
        Sleep(self.sb,10)
        checkRegionChange(sb)
        # self.stripAndSaveAllSlots()
        self.startFile()
        self.run()
        self.endFile()

    def startFile(self):
        with open(self.locationName, 'w') as file:
            file.write('[')

    def writeSlotToFile(self):
        with open(self.locationName, 'a') as file:
            json.dump(self.slotInfoObj, file)
            file.write(', \n')

    def endFile(self):
        with open(self.locationName, 'w') as file:
            file.write(']')

    def run(self):
        self.clickPublisherBtn()
        self.extractPublisherNames()
        self.clickPublisherBtn()
        self.cyclePublishers()
        # self.populateSlotInfo()
        # self.saveSlotInfo()
        
    def clickPublisherBtn(self):
        self.sb.find_element(self.providerBtnStr).click()

    def extractPublisherNames(self):
        publisherEles = self.sb.find_elements(self.providerNameStr)
        indexCheck = 0
        for ele in publisherEles:
            # start recording after popular publishers
            if indexCheck <= self.cutPubListInd:
                indexCheck += 1
            else:
                pubName = ele.text
                self.pubName = pubName.replace('$','')
                # skip play'n go until I figure out how to add it in
                if self.pubName in voidNames:
                    continue
                self.publisherList.append(self.pubName)

    def buildSlotObj(self):
        splitNames = splitSlotNames(self.slotId)
        self.slotInfoObj = {
            'name': splitNames[1], 
            'creator': splitNames[0],
            'full': self.slotId
        }

    def cyclePublishers(self):
        while len(self.publisherList) > 1:
            pubName = self.publisherList.pop(0)
            self.clickPublisherBtn()
            self.pubNameLabelStr = fr'//p/div/*[contains(.,"{pubName}")]'

            self.clickProvider()
            # close provider list
            self.clickPublisherBtn()
            self.loadAllSlots()
            # save 
            self.listAvailableSlots()
            self.unclickProvider()

    def clickProvider(self):
        if self.sb.is_element_present(self.pubNameLabelStr):
            print(self.pubNameLabelStr)
            self.sb.find_element(self.pubNameLabelStr).click()
            return
        else:
            self.refreshPage()
            self.clickPublisherBtn()
            self.clickProvider()

    def unclickProvider(self):
        self.clickPublisherBtn()
        self.clickProvider()
        self.clickPublisherBtn()

    def loadAllSlots(self):
        # Click the "load more" button to load more slots
        count = 0
        while True:
            # see if "load more" button is still at the bottom of the list
            if self.sb.is_element_present(self.loadMoreEle):
                try:
                    print('found load more button')
                    self.sb.scroll_to(self.loadMoreEle)
                    self.sb.find_element(self.loadMoreEle).click()
                    count += 1
                except:
                    print('failed to press load more btn')
            else:
                print('load more btn not found')
                break
            print(count)

    def listAvailableSlots(self):
        # self.slotNames = []
        parentElement = self.sb.find_elements(self.slotCard)
        # loop over parent element
        for element in parentElement:
            try:
                # text overlay location
                if element.children[3].children[4].text == 'Not available in your region':
                    continue
            except:
                self.slotId = element.children[0].id
                self.buildSlotObj()
                self.writeSlotToFile()
                # available slot, push it to the list
                # self.slotNames.append(element.children[0].id)
            # random empty comments might mess up this 
        # self.fullSlotList.append(self.slotNames)

    # def populateSlotInfo(self):
    #     for name in self.fullSlotList:
    #         splitNames = splitSlotNames(name)
    #         slotInfoObj = {
    #             'name': splitNames[1], 
    #             'creator': splitNames[0],
    #             'full': name
    #         }
    #         self.writeSlotToFile(slotInfoObj)
    #         # self.finalSlotList.append(slotInfoObj)

    def refreshPage(self):
        self.sb.refresh_page()
        Sleep(self.sb,10)
        checkCaptcha(self.sb)
        Sleep(self.sb,10)
        checkRegionChange(self.sb)
        Sleep(self.sb,5)

    # def saveSlotInfo(self):
    #     SaveFile(location=self.locationName,list=self.finalSlotList)
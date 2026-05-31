from classes.classUtilityFunctions import checkCaptcha, checkRegionChange, Sleep, splitSlotNames
from utilityFunctions import SaveFile

stake = 'https://stake.com/casino/group/slots'

class ScrapeSlots:
    def __init__(self, sb):
        self.locationName = 'slotdata.json'
        self.sb = sb
        self.fullSlotList = []
        sb.open(stake)
        checkCaptcha(sb)
        checkRegionChange(sb)
        self.stripAndSaveAllSlots()

    def stripAndSaveAllSlots(self):
        self.cycleProvidersList()
        print('stripAndSaveAllSlots is complete')
    
    def cycleProvidersList(self):
        providersBtnStr = '//div[contains(@class, "main-content")]//button[.//span[normalize-space()="Publishers"]]'
        providerString = '.provider-list > div > label > span:nth-of-type(2) > p > div > span'
        
        Sleep(self.sb)
        # click providers
        self.sb.click(providersBtnStr)
        # get count of elements to use index to loop over
        count = len(self.sb.find_elements(providerString)) -1
        manualPopularCount = 14
        print(f'count of providers: {count}')

        for i in range(count):
            # target only slots after popular ones
            if i < manualPopularCount:
                continue
            # refind elements (needed)
            providers = self.checkRefresh(providerString)
            print(providers[i].text)
            # click provider
            providers[i].click()
            # unselect provider bar
            self.sb.click(providersBtnStr)
            # get provider slot list
            providerSlotList = self.getSlotList()
            self.fullSlotList.append(providerSlotList)
            # reopen provider bar
            self.sb.click(providersBtnStr)
            # refind elements (needed)
            providers = self.sb.find_elements(providerString)
            # unclick added provider
            self.checkBuggedProviders(providers)
            providers[i].click()
        # add indexes
        self.addIndexes()
        SaveFile(self.locationName,self.fullSlotList)

    def checkRefresh(self,providerString):
        providers = self.sb.find_elements(providerString)
        while len(providers) < 3:
            providers = self.sb.find_elements(providerString)
            # refresh page
            self.sb.refresh_page()
        return providers

    def getSlotList(self):
        slotObjList = []
        self.loadMore()
        # select the icons
        availableIdList = self.checkAvailable()
        # break out if no slots available
        if availableIdList == None:
            return
        # slotElements = self.sb.find_elements('.game-card-wrap > .link > .img-wrap > img')
        for id in availableIdList:
            splitNames = splitSlotNames(id)
            slotElementObj = {
                'name': splitNames[1], 
                'creator': splitNames[0],
                'full': id
            }
            slotObjList.append(slotElementObj)
        print('finished provider')    
        return slotObjList
    
    # def splitSlotNames(self,string):
    #     arr = string.split('-')
    #     publisher = ''
    #     slot = ''
    #     for i in range(len(arr)):
    #         match i:
    #             case 0:
    #                 publisher += arr[i]
    #             case 1:
    #                 slot += arr[i]
    #             case _:
    #                 slot += f' {arr[i]}'
    #     return (publisher, slot)
    
    def checkBuggedProviders(self,providers):
        pass
        captchaString = '#main-wrapper > #content > #verifying'
        # while len(providers == 0):
        # refresh page and 
        # if captcha, solve
        # if redirect, close
        # find providers again

    def addIndexes(self):
        for i in range(len(self.fullSlotList)):
            for j in range(len(self.fullSlotList[i])):
                self.fullSlotList[i][j]['index1'] = i
                self.fullSlotList[i][j]['index2'] = j
    
    def loadMore(self):
        # Click the "load more" button to load more slots
        isThere = True
        count = 0
        loadMoreElement = '.load-more-container button'
        while isThere:
            # make sure button loads
            Sleep(self.sb)
            # see if "load more" button is still at the bottom of the list
            if self.sb.is_element_present(loadMoreElement):
                print('found load more button')
                self.sb.click(loadMoreElement)
                count += 1
            else:
                print('load more btn not found')
                isThere = False
            print(count)

    def checkAvailable(self):
        idList = []
        parentElement = self.sb.find_elements('.game-card-wrap > .link > .img-wrap')
        #slotElements = self.sb.find_elements('.game-card-wrap > .link > .img-wrap > img')
        #notAvailable = self.sb.find_elements('.game-card-wrap > .link > .img-wrap > .overlay-text > span:nth-of-type(2)')
        # loop over parent element
        for element in parentElement:
            try:
                if element.children[3].children[4].text == 'Not available in your region':
                    continue
            except:
                idList.append(element.children[0].id)
            # random empty comments might mess up this 
        if len(idList) > 0:
            return idList
        else:
            return
from classes.InputValidation import builtSlotList, rejectSlotList
from classes.classUtilityFunctions import pullScrapedSlots
from utilityFunctions import SaveFile

class FindNextToBuild:
    def __init__(self):
        self.saveLocation = 'nextToBuild.md'
        self.popList = []
        self.nextList = []
        self.scrapedList = pullScrapedSlots()
        self.builtList = builtSlotList

        self.compareNames()
        self.bulkRemove()
        self.buildFile()
        # get list from file
        # loop through
        # 
        pass

    def compareNames(self):
        for i in range(len(self.scrapedList)):
            scrapedTarget = self.scrapedList[i]
            scrapedName = scrapedTarget['full']
            for j in range(len(self.builtList)):
                builtName = self.builtList[j]
                if scrapedName == builtName:
                    self.popList.append(i)
                    break
                elif scrapedName in rejectSlotList:
                    self.popList.append(i)
                    break

    def bulkRemove(self):
        removed = [self.scrapedList[i] for i in self.popList]
        for i in sorted(self.popList, reverse=True):
            self.scrapedList.pop(i)
        print(removed)
        print(self.scrapedList)
        self.nextList = self.scrapedList

    def buildFile(self):
        SaveFile(self.saveLocation,self.nextList)
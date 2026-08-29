from classes.InputValidation import InputValidation
from classes.ScrapeSlots import ScrapeSlots
from classes.ChatGrabber import ChatGrabber
from classes.OBS import OBS
from classes.BuildSpreadsheet import BuildSpreadsheet
from classes.FindNextToBuild import FindNextToBuild
from utilityFunctions import Sleep
from classes.classUtilityFunctions import createErrorLog
from classes.findSubclass import findSubclass
from seleniumbase import SB
import threading

slotDataLocation = 'slotdata.json'
inputOverride = '18gaming-diamond-luxe' #'0xedge-5-alpha-planets', False
scrapeSlotsToggle = False
buildSpreadsheetToggle = False
findNextToBuildToggle = False
errorHandling = False
votingTimeout = 0 #10
loopIncrement = 1

if buildSpreadsheetToggle:
    try:
        BuildSpreadsheet()
    except: print('failed to run BuildSpreadsheet')
if findNextToBuildToggle:
    try:
        FindNextToBuild()
    except:
        print('failed to run FindNextToBuild, probably due to slotdata.json file not written complete')

obs = OBS()

class Main:
    def __init__(self):
        self.run()

    def run(self):
        # obs scene blocker
        obs.runWelcomeScene()
        with SB(uc=True, incognito=True) as self.sb:
            self.sb.minimize_window()
            # fill in chrome window details to capture
            # sb.driver.get(f'data:text/html,<title>{pageTitle}</title>')
            obs.runFindChromeWindowToCapture()
            if scrapeSlotsToggle:
                ScrapeSlots(sb=self.sb)
                return
            else:
                # run program
                while True:
                    if errorHandling:
                        try:
                            self.mainCodeBlock()
                        except Exception as e:
                            # append to error log
                            try:
                                createErrorLog(self.sb,name=self.iv.slotObj['full'],exception=e)
                            except:
                                createErrorLog(self.sb,name='undefined, no name obj',exception=e)


                    else:
                        self.mainCodeBlock()

    def mainCodeBlock(self):
        # find chat message randomly
        ## obs scene pick a slot
        obs.runPickSlotScene()
        # needs to run separate from main code

        threading.Thread(
            target=obs.runSetPickASlot,
            args=(votingTimeout,),
            daemon=True
        ).start()

        cg = ChatGrabber(votingTimeout)
        if inputOverride:    # run make input find the override slot
            cg.winner['slotChoice'] = inputOverride
        self.iv = InputValidation(input=cg.winner['slotChoice'])
        # get slot information from scraped info based on fullName

        for i in range(loopIncrement):
            ## OBS to change scene to block screen
            obs.runSetSelectedScene(self.iv.slotObj)
            obs.runSelectedScene()
            slotObj = findSubclass(slotName=self.iv.validatedSlot , sb=self.sb, obs=obs, override=inputOverride)
            # remove images in image directory
            obs.runSetWinnerScene(cg.winner,self.iv.validatedSlot,slotObj.winnings)
            obs.runWinnerScene()
            Sleep(self.sb,5)
                

Main()

from classes.InputValidation import InputValidation
from classes.ScrapeSlots import ScrapeSlots
from classes.ChatGrabber import ChatGrabber
from classes.OBS import OBS
from classes.BuildSpreadsheet import BuildSpreadsheet
from classes.FindNextToBuild import FindNextToBuild
from utilityFunctions import keepAlive, Sleep
# from classes.classUtilityFunctions import checkSlotNameInput
from classes.findSubclass import findSubclass
from seleniumbase import SB
import threading

# pageTitle = 'U Spin Chrome'
scrapeSlotsToggle = False
buildSpreadsheetToggle = False
findNextToBuildToggle = True
errorHandling = False
votingTimeout = 0 #30
loopIncrement = 1

if buildSpreadsheetToggle:
    BuildSpreadsheet()
if findNextToBuildToggle:
    FindNextToBuild()

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
            else:
                # run program
                while True:
                    if errorHandling:
                        try:
                            self.mainCodeBlock()
                        except:
                            obs.runErrorScene()
                            Sleep(self.sb,5)
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
        iv = InputValidation(input=cg.winner['slotChoice'])
        # get slot information from scraped info based on fullName

        for i in range(loopIncrement):
            ## OBS to change scene to block screen
            obs.runSetSelectedScene(iv.slotObj)
            obs.runSelectedScene()
            slotObj = findSubclass(slotName=iv.validatedSlot , sb=self.sb, obs=obs)
            # remove images in image directory
            obs.runSetWinnerScene(cg.winner,iv.validatedSlot,slotObj.winnings)
            obs.runWinnerScene()
            Sleep(self.sb,5)
    # keepAlive()
                

Main()

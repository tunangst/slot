from classes.InputValidation import InputValidation
from classes.ScrapeSlots import ScrapeSlots
from classes.ChatGrabber import ChatGrabber
from classes.OBS import OBS
from classes.BuildSpreadsheet import BuildSpreadsheet
from utilityFunctions import keepAlive
# from classes.classUtilityFunctions import checkSlotNameInput
from classes.findSubclass import findSubclass
from seleniumbase import SB

# pageTitle = 'U Spin Chrome'
scrapeSlots = False
buildSpreadsheet = False
loopIncrement = 1

if buildSpreadsheet:
    BuildSpreadsheet()

obs = OBS()

# obs scene blocker
obs.activeCheckWrapper(obs.welcomeScene)
with SB(uc=True, incognito=True) as sb:
    sb.minimize_window()
    # fill in chrome window details to capture
    # sb.driver.get(f'data:text/html,<title>{pageTitle}</title>')
    obs.activeCheckWrapper(obs.findChromeWindowToCapture)
    if scrapeSlots:
        ScrapeSlots(sb=sb)
    else:
        # run program
        while True:
            # find chat message randomly
            ## obs scene pick a slot
            obs.activeCheckWrapper(obs.pickSlotScene)
            cg = ChatGrabber()
            iv = InputValidation(input=cg.winner['slotChoice'])
            # get slot information from scraped info based on fullName
            #

            for i in range(loopIncrement):
                ## OBS to change scene to block screen
                obs.activeCheckWrapper(obs.setWinnerScene,iv.slotObj)
                obs.activeCheckWrapper(obs.winnerScene)
                findSubclass(slotName=iv.validatedSlot , sb=sb, obs=obs)
                # remove images in image directory

        keepAlive()

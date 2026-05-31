from obsws_python import ReqClient
from dotenv import load_dotenv
# import asyncio
import os
import time

host = os.getenv('OBS_HOST')
port = os.getenv('OBS_PORT')
passw = os.getenv('OBS_PASS')

loadingSlotCommand = 'winning command'
loadingSlotName = 'slot name'
loadingSlotDev = 'slot dev'
winnerName = 'winner name'
winnerSlot = 'winner slot'
winnerAmount = 'winner amount'
pickCountdown = 'countdown'
mainWindowCapture = 'Window Capture'

class OBS:
    def __init__(self):
        self.client = False
        try:
            self.client = ReqClient(
                host=host,
                port=port,
                password=passw
            )
            print('Connected to OBS')
        except:
            print('OBS is down')

    def startStream(self):
        self.client.start_stream()
        print('started stream')

    def endStream(self):
        self.client.stop_stream()
        print('ended stream')

    def mainScene(self):
        self.client.set_current_program_scene('main')
        print('changed scene to: main')
    def runMainScene(self):
        self.activeCheckWrapper(self.mainScene)

    def welcomeScene(self):
        self.client.set_current_program_scene('welcome')
        print('changed scene to: welcome')
    def runWelcomeScene(self):
        self.activeCheckWrapper(self.welcomeScene)
    
    def pickSlotScene(self):
        self.client.set_current_program_scene('pick a slot')
        print('changed scene to: choose-a-slot')
    def runPickSlotScene(self):
        self.activeCheckWrapper(self.pickSlotScene)

    def selectedScene(self):
        self.client.set_current_program_scene('selected')
        print('changed scene to: loading')
    def runSelectedScene(self):
        self.activeCheckWrapper(self.selectedScene)

    def winnerScene(self):
        self.client.set_current_program_scene('winner')
        print('changed scene to: winner')
    def runWinnerScene(self):
        self.activeCheckWrapper(self.winnerScene)

    def findChromeWindowToCapture(self):
        # move to main scene to make sure the asset changes
        self.mainScene()
        windows = self.client.get_input_properties_list_property_items(
            'Chrome Capture',
            'window'
        )
        windowStr = self.findWindow(windows)
        self.setWindow(windowStr)
        # print(windows)
        # get out of main scene
        self.winnerScene()
    def runFindChromeWindowToCapture(self):
        self.activeCheckWrapper(self.findChromeWindowToCapture)

    def findWindow(self, list):
        newChrome = list.property_items[0]['itemValue']
        print(newChrome)
        return newChrome
    def runFindWindow(self,list):
        self.activeCheckWrapper(self.findWindow,list)

    def setWindow(self, windowStr):
        self.client.set_input_settings(
            name=mainWindowCapture,
            settings={
                'window': windowStr
            },
            overlay=True
        )
    def runSetWindow(self,windowStr):
        self.activeCheckWrapper(self.setWindow,windowStr)
    
    def setPickASlot(self, timeout):
        counter = timeout
        end_time = time.monotonic() + counter
        while True:
            remaining = max(0, int(end_time - time.monotonic()))
            minutes = remaining // 60
            seconds = remaining % 60
            timerText = f'{seconds}'
            print(timerText, end='\r')
            if remaining == 0:
                break
            time.sleep(0.1)

            self.client.set_input_settings(
                name=pickCountdown,
                settings={
                    'text': timerText
                },
                overlay=True
            )
    def runSetPickASlot(self,timeout):
        self.activeCheckWrapper(self.setPickASlot,timeout)
    
    def setSelectedScene(self, slotObj):
        name = slotObj['name']
        creator = slotObj['creator']
        fullName = '||' + slotObj['full'] + '||'

        self.client.set_input_settings(
            name=loadingSlotCommand,
            settings={
                'text': fullName
            },
            overlay=True
        )
        self.client.set_input_settings(
            name=loadingSlotName,
            settings={
                'text': name
            },
            overlay=True
        )
        self.client.set_input_settings(
            name=loadingSlotDev,
            settings={
                'text': creator
            },
            overlay=True
        )
    def runSetSelectedScene(self,slotObj):
        self.activeCheckWrapper(self.setSelectedScene,slotObj)
    
    def setWinnerScene(self,obj,validatedSlot,winnings):
        platform = obj['platform']
        username = obj['username']
        chatMessage = obj['chatMessage']
        slotChoice = obj['slotChoice']
        stakeTag = obj['stakeTag']
        validatedSlotCode = '||' + validatedSlot + '||'
        winningAmount = f'${winnings:,.2f}'

        self.client.set_input_settings(
            name=winnerName,
            settings={
                'text': username
            },
            overlay=True
        )
        self.client.set_input_settings(
            name=winnerSlot,
            settings={
                'text': validatedSlotCode
            },
            overlay=True
        )
        self.client.set_input_settings(
            name=winnerAmount,
            settings={
                'text': winningAmount
            },
            overlay=True
        )
        pass
    def runSetWinnerScene(self,obj,validatedSlot,winnings):
        self.activeCheckWrapper(self.setWinnerScene,obj,validatedSlot,winnings)

    def activeCheckWrapper(self, func, *args, **kwargs):
        if self.client:
            result = func(*args, **kwargs)
            return result
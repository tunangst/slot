from obsws_python import ReqClient
from dotenv import load_dotenv
import os

host = os.getenv('OBS_HOST')
port = os.getenv('OBS_PORT')
passw = os.getenv('OBS_PASS')

loading_slotCommand = 'winning command'
loading_slotName = 'slot name'
loading_slotDev = 'slot dev'
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

    def welcomeScene(self):
        self.client.set_current_program_scene('welcome')
        print('changed scene to: welcome')

    def pickSlotScene(self):
        self.client.set_current_program_scene('pick a slot')
        print('changed scene to: choose-a-slot')

    def winnerScene(self):
        self.client.set_current_program_scene('winner')
        print('changed scene to: loading')

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

    def findWindow(self, list):
        newChrome = list.property_items[0]['itemValue']
        print(newChrome)
        return newChrome
    #     print(list.property_items)
    #     for item in list.property_items:
    #         print(item)

    def setWindow(self, windowStr):
        self.client.set_input_settings(
            name=mainWindowCapture,
            settings={
                'window': windowStr
            },
            overlay=True
        )
        
    def setWinnerScene(self, slotObj):
        name = slotObj['name']
        creator = slotObj['creator']
        fullName = '||' + slotObj['full'] + '||'

        self.client.set_input_settings(
            name=loading_slotCommand,
            settings={
                'text': fullName
            },
            overlay=True
        )
        self.client.set_input_settings(
            name=loading_slotName,
            settings={
                'text': name
            },
            overlay=True
        )
        self.client.set_input_settings(
            name=loading_slotDev,
            settings={
                'text': creator
            },
            overlay=True
        )

    def activeCheckWrapper(self, func, *args, **kwargs):
        if self.client:
            result = func(*args, **kwargs)
            return result
from utilityFunctions import GetRandomNumber
from datetime import datetime, timedelta
from websockets import connect
from dotenv import load_dotenv
import asyncio
import json
import re
import os

class ChatGrabber:
    def __init__(self, timeout):
        self.timeout = timeout
        self.startTime = datetime.now()
        self.endTime = self.calcEndTime()
        self.msgPool = []
        self.winner = {'platform': '','username': '','chatMessage': '','slotChoice': '','stakeTag': ''}
        self.sessionID = os.getenv('SSN_SESSION')
        self.url = f'wss://io.socialstream.ninja/join/{self.sessionID}/4'
        self.run()
        
    def run(self):
        asyncio.run(self.listen())
        self.randSelect()

    async def listen(self):
        async with connect(self.url) as ws:
            print('Connected to Social Stream Ninja')
            while datetime.now() < self.endTime:
                try:
                    res = await asyncio.wait_for(
                        ws.recv(),
                        timeout=1
                    )
                    data = json.loads(res)
                    # Chat messages
                    if 'chatname' in data:
                        username = data['chatname']
                        chatMessage = data.get(
                            'chatmessage',
                            ''
                        )
                        platform = data.get(
                            'type',
                            'unknown'
                        )
                        platform = f'[{platform}]'
                        username = f'{username}:'
                        chatMessage = f'{chatMessage}'
                        msgBlock = {
                            'platform': platform,
                            'username': username,
                            'chatMessage': chatMessage,
                            'slotChoice': '',
                            'stakeTag': ''
                        }
                        print(msgBlock)
                        self.filterMsg(msgBlock)
                        # stop listening
                except asyncio.TimeoutError:
                    print('tick')
            print('boom')

    def calcEndTime(self):
        return self.startTime + timedelta(seconds=self.timeout)
    
    def filterMsg(self, msgBlock):
        # search whole string for 
        regex = r'\|\|(.*?)\|\|'
        msg = msgBlock['chatMessage']
        match = re.search(regex,msg)
        if match:
            print(match.group())
            slot = match.group().replace('||','')
            msgBlock['slotChoice'] = slot
            self.msgPool.append(msgBlock)

    def randSelect(self):
        size = len(self.msgPool)
        if size > 0:
            rng = GetRandomNumber() - 1
            self.winner = self.msgPool[rng]

    # def end(self):
    #     if datetime.now() > self.endTime:
    #         return True
    #     else:
    #         return False

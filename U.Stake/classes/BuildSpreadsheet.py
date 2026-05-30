import os
import json
import gspread
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from classes.classUtilityFunctions import splitSlotNames
from classes.InputValidation import builtSlotList

sheetName = 'U Spin Slot List'

class BuildSpreadsheet:
    def __init__(self):
        self.slotDataArr = []
        load_dotenv()

        self.buildData()
        self.connectToSheetsAPI()
        self.addData()
        # self.resizeColumns()

    def addData(self):
        # ERASE EVERYTHING
        self.ws.clear()
        self.ws.update('A1:C1', [['Input Code', 'Slot Title', 'Publisher']])
        for slotObj in self.slotDataArr:
            self.ws.append_row([slotObj['input'],slotObj['name'],slotObj['creator']])

    def connectToSheetsAPI(self):
        self.credsJson = os.getenv('GOOGLE_CREDS')
        self.credsDict = json.loads(self.credsJson)
        self.scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        self.creds = Credentials.from_service_account_info(
            self.credsDict,
            scopes=self.scopes
        )
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open(sheetName)
        self.ws = self.sheet.sheet1

    def buildData(self):
        for slotCode in builtSlotList:
            publisher,slot = splitSlotNames(slotCode)
            slotObj = {
                'name': slot.upper(),
                'creator': publisher,
                'input': f'||{slotCode}||'
            }
            self.slotDataArr.append(slotObj)
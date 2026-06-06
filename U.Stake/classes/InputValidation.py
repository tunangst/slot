from classes.classUtilityFunctions import getInfoFromScrapedSlots
from utilityFunctions import GetRandomNumber

rejectSlotList = [
    '0daygames-corsairs-hex',
    '18gaming-lucky-joker',
    '18gaming-santas-christmas-magic'
]

builtSlotList = [
    '0xedge-wild-zeus',
    '0xedgefrutti-bonanza',
    '0xedge-super-candy-drop',
    '0xedge-do-not-redeem-it',
    '0xedge-5-alpha-planets',
    '0xluckylab-obsidian-spin',
    '1000lakesstudios-toivo',
    '1000lakesstudios-disco-cubes',
    '1000lakesstudios-bass-fury',
    '1000lakesstudios-operation-epic-taco',
    '1000lakesstudios-r-i-p-1000',
    '1000lakesstudios-flying-finns-1000',
    '1000lakesstudios-bloom-em',
    '1000lakesstudios-apex-syndicate',
    '1000lakesstudios-candy-carnival-spring-spritz',
    '1000lakesstudios-twisted-candy-shop',
    '1000lakesstudios-arctic-runes',
    '1000lakesstudios-yakuza-v-i-p',
    '1000lakes-rotation-of-ra',
    '111lightproductions-the-syndicate',
    '111lightproductions-gemburst-rush',
    '111lightproductions-nfl-touchdown',
    '111lightproductions-dragon-fortunes',
    '111lightproductions-legends-of-the-lost-grove',
    '111lightproductions-hearts-in-sync',
    '111lightproductions-sunset-serenade',
    '1789studios-cat-war',
    '18gaming-sweet-stake-25k',
    '18gaming-bowling-riches',
    '18gaming-golden-piggy',
    '18gaming-rock-n-roll',
    '18gaming-buffalo-blaze-2',
    '18gaming-mystical-plum-grove',
    '18gaming-aztec-sun-blaze',
    '18gaming-wrath-of-olympus',
    '18gaming-crypto-bonanza',
    '18gaming-dragon-fortune',
    '18gaming-sheriffs-bounty',
    '18gaming-wall-street-honey-stakes',
    '18gaming-buffalo-blaze',
    '18gaming-derby-race',
    '18gaming-beachside-betties',
    '18gaming-diamond-luxe'
]

class InputValidation:
    def __init__(self,input):
        self.input = input
        self.validatedSlot = False

        self.checkList()
        self.getSlotInfo()
        # self.validateInput()
    
    def checkList(self):
        if self.input in builtSlotList:
            self.validatedSlot = self.input
        else:
            self.pickSlot()

    def pickSlot(self):
        ind = len(builtSlotList) -1
        rng = GetRandomNumber(ind)
        self.validatedSlot = builtSlotList[rng]

        # find how to pull from Youtube
        # if too long, maybe 1 min then pull a random one

    def getSlotInfo(self):
        self.slotObj = getInfoFromScrapedSlots(self.validatedSlot)
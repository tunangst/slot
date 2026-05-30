from classes.slots.ZeroxEdgeWildZeus import ZeroxEdgeWildZeus
from classes.slots.ZeroxEdgeFruttiBonanza import ZeroxEdgeFruttiBonanza
from classes.slots.ZeroxEdgeSuperCandyDrop import ZeroxEdgeSuperCandyDrop
from classes.slots.ZeroxEdgeDoNotRedeemIt import ZeroxEdgeDoNotRedeemIt
from classes.slots.ZeroxEdgeFiveAlphaPlanets import ZeroxEdgeFiveAlphaPlanets
from classes.slots.OneThousandLakesStudiosToivo import OneThousandLakesStudiosToivo
from classes.slots.OneThousandLakesStudiosDiscoCubes import OneThousandLakesStudiosDiscoCubes
from classes.slots.OneThousandLakesStudiosBassFury import OneThousandLakesStudiosBassFury
from classes.slots.OneThousandLakesStudiosOperationEpicTaco import OneThousandLakesStudiosOperationEpicTaco
from classes.slots.OneThousandLakesStudiosRIPOneThousand import OneThousandLakesStudiosRIPOneThousand
from classes.slots.OneThousandLakesStudiosFlyingFinsOneThousand import OneThousandLakesStudiosFlyingFinsOneThousand
from classes.slots.OneThousandLakesStudiosBloomEm import OneThousandLakesStudiosBloomEm
from classes.slots.OneThousandLakesStudioApexSyndicate import OneThousandLakesStudioApexSyndicate
from classes.slots.OneThousandLakesStudioYakuzaVIP import OneThousandLakesStudioYakuzaVIP
from classes.slots.OneThousandLakesStudioCandyCarnivalSpringSpritz import OneThousandLakesStudioCandyCarnivalSpringSpritz
from classes.slots.OneThousandLakesStudioTwistedCandyShop import OneThousandLakesStudioTwistedCandyShop
from classes.slots.OneThousandLakesStudioArcticRunes import OneThousandLakesStudioArcticRunes
from classes.slots.OneThousandLakesRotationOfRa import OneThousandLakesRotationOfRa
from classes.slots.OneThousandOneHundredElevenLightProductionsTheSyndicate import OneThousandOneHundredElevenLightProductionsTheSyndicate
from classes.slots.OneThousandOneHundredElevenLightProductionsGemburstRush import OneThousandOneHundredElevenLightProductionsGemburstRush
from classes.slots.OneThousandOneHundredElevenLightProductionsNFLTouchdown import OneThousandOneHundredElevenLightProductionsNFLTouchdown
from classes.slots.OneThousandOneHundredElevenLightProductionsDragonFortunes import OneThousandOneHundredElevenLightProductionsDragonFortunes
from classes.slots.OneThousandOneHundredElevenLightProductionsLegendsOfTheLostGrove import OneThousandOneHundredElevenLightProductionsLegendsOfTheLostGrove


# slotTotal = [
#         '0xedge-wild-zeus',
#         '0xedgefrutti-bonanza',
#         '0xedge-super-candy-drop',
#         '0xedge-do-not-redeem-it',
#         '0xedge-5-alpha-planets',
#         '1000lakesstudios-toivo',
#         '1000lakesstudios-disco-cubes',
#         '1000lakesstudios-bass-fury',
#         '1000lakesstudios-operation-epic-taco',
#         '1000lakesstudios-r-i-p-1000',
#         '1000lakesstudios-flying-finns-1000',
#         '1000lakesstudios-bloom-em',
#         '1000lakesstudios-apex-syndicate',
#         '1000lakesstudios-yakuza-v-i-p',
#         '1000lakesstudios-candy-carnival-spring-spritz'
# ]

override = True
overrideName = '111lightproductions-legends-of-the-lost-grove'

def findSubclass(sb, slotName, obs):
        if override:
                slotName = overrideName     # override
        match slotName:
                # this game is a web based one and breaks with spins over 50
                        # case '0daygames-corsairs-hex':
                # newSubclass = ZeroDayGamesCorsairsHex(sb, slotObj)
                case '0xedge-wild-zeus':
                        ZeroxEdgeWildZeus(sb,obs)
                case '0xedgefrutti-bonanza':
                        ZeroxEdgeFruttiBonanza(sb,obs)
                case '0xedge-super-candy-drop':
                        ZeroxEdgeSuperCandyDrop(sb,obs)
                case '0xedge-do-not-redeem-it':
                        ZeroxEdgeDoNotRedeemIt(sb,obs)
                case '0xedge-5-alpha-planets':
                        ZeroxEdgeFiveAlphaPlanets(sb,obs)
                case '1000lakesstudios-toivo':
                        OneThousandLakesStudiosToivo(sb,obs)
                case '1000lakesstudios-disco-cubes':
                        OneThousandLakesStudiosDiscoCubes(sb,obs)
                case '1000lakesstudios-bass-fury':
                        OneThousandLakesStudiosBassFury(sb,obs)
                case '1000lakesstudios-operation-epic-taco':
                        OneThousandLakesStudiosOperationEpicTaco(sb,obs)
                case '1000lakesstudios-r-i-p-1000':
                        OneThousandLakesStudiosRIPOneThousand(sb,obs)
                case '1000lakesstudios-flying-finns-1000':
                        OneThousandLakesStudiosFlyingFinsOneThousand(sb,obs)
                case '1000lakesstudios-bloom-em':
                        OneThousandLakesStudiosBloomEm(sb,obs)
                case '1000lakesstudios-apex-syndicate':
                        OneThousandLakesStudioApexSyndicate(sb,obs)
                case '1000lakesstudios-yakuza-v-i-p':
                        OneThousandLakesStudioYakuzaVIP(sb,obs)
                case '1000lakesstudios-candy-carnival-spring-spritz':
                        OneThousandLakesStudioCandyCarnivalSpringSpritz(sb,obs)
                case '1000lakesstudios-twisted-candy-shop':
                        OneThousandLakesStudioTwistedCandyShop(sb,obs)
                case '1000lakesstudios-arctic-runes':
                        OneThousandLakesStudioArcticRunes(sb,obs)
                case '1000lakes-rotation-of-ra':
                        OneThousandLakesRotationOfRa(sb,obs)
                case '111lightproductions-the-syndicate':
                        OneThousandOneHundredElevenLightProductionsTheSyndicate(sb,obs)
                case '111lightproductions-gemburst-rush':
                        OneThousandOneHundredElevenLightProductionsGemburstRush(sb,obs)
                case '111lightproductions-nfl-touchdown':
                        OneThousandOneHundredElevenLightProductionsNFLTouchdown(sb,obs)
                case '111lightproductions-dragon-fortunes':
                        OneThousandOneHundredElevenLightProductionsDragonFortunes(sb,obs)
                case '111lightproductions-legends-of-the-lost-grove':
                        OneThousandOneHundredElevenLightProductionsLegendsOfTheLostGrove(sb,obs)
                case _:
                        print('no subclass found')
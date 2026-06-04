from classes.slots.ZeroxEdgeWildZeus import ZeroxEdgeWildZeus
from classes.slots.ZeroxEdgeFruttiBonanza import ZeroxEdgeFruttiBonanza
from classes.slots.ZeroxEdgeSuperCandyDrop import ZeroxEdgeSuperCandyDrop
from classes.slots.ZeroxEdgeDoNotRedeemIt import ZeroxEdgeDoNotRedeemIt
from classes.slots.ZeroxEdgeFiveAlphaPlanets import ZeroxEdgeFiveAlphaPlanets
from classes.slots.ZeroxLuckyLabObsidianSpin import ZeroxLuckyLabObsidianSpin
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
from classes.slots.OneThousandOneHundredElevenLightProductionsHeartsInSync import OneThousandOneHundredElevenLightProductionsHeartsInSync
from classes.slots.OneThousandOneHundredElevenLightProductionsSunsetSerenade import OneThousandOneHundredElevenLightProductionsSunsetSerenade
from classes.slots.OneThousandSevenHundredEightyNineStudiosCatWar import OneThousandSevenHundredEightyNineStudiosCatWar
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
overrideName = '1000lakesstudios-yakuza-v-i-p'

def findSubclass(sb, slotName, obs):
        if override:
                slotName = overrideName     # override
        match slotName:
                # this game is a web based one and breaks with spins over 50
                        # case '0daygames-corsairs-hex':
                # newSubclass = ZeroDayGamesCorsairsHex(sb, slotObj)
                case '0xedge-wild-zeus':
                        return ZeroxEdgeWildZeus(sb,obs)
                case '0xedgefrutti-bonanza':
                        return ZeroxEdgeFruttiBonanza(sb,obs)
                case '0xedge-super-candy-drop':
                        return ZeroxEdgeSuperCandyDrop(sb,obs)
                case '0xedge-do-not-redeem-it':
                        return ZeroxEdgeDoNotRedeemIt(sb,obs)
                case '0xedge-5-alpha-planets':
                        return ZeroxEdgeFiveAlphaPlanets(sb,obs)
                case '0xluckylab-obsidian-spin':
                        return ZeroxLuckyLabObsidianSpin(sb,obs)
                case '1000lakesstudios-toivo':
                        return OneThousandLakesStudiosToivo(sb,obs)
                case '1000lakesstudios-disco-cubes':
                        return OneThousandLakesStudiosDiscoCubes(sb,obs)
                case '1000lakesstudios-bass-fury':
                        return OneThousandLakesStudiosBassFury(sb,obs)
                case '1000lakesstudios-operation-epic-taco':
                        return OneThousandLakesStudiosOperationEpicTaco(sb,obs)
                case '1000lakesstudios-r-i-p-1000':
                        return OneThousandLakesStudiosRIPOneThousand(sb,obs)
                case '1000lakesstudios-flying-finns-1000':
                        return OneThousandLakesStudiosFlyingFinsOneThousand(sb,obs)
                case '1000lakesstudios-bloom-em':
                        return OneThousandLakesStudiosBloomEm(sb,obs)
                case '1000lakesstudios-apex-syndicate':
                        return OneThousandLakesStudioApexSyndicate(sb,obs)
                case '1000lakesstudios-yakuza-v-i-p':
                        return OneThousandLakesStudioYakuzaVIP(sb,obs)
                case '1000lakesstudios-candy-carnival-spring-spritz':
                        return OneThousandLakesStudioCandyCarnivalSpringSpritz(sb,obs)
                case '1000lakesstudios-twisted-candy-shop':
                        return OneThousandLakesStudioTwistedCandyShop(sb,obs)
                case '1000lakesstudios-arctic-runes':
                        return OneThousandLakesStudioArcticRunes(sb,obs)
                case '1000lakes-rotation-of-ra':
                        return OneThousandLakesRotationOfRa(sb,obs)
                case '111lightproductions-the-syndicate':
                        return OneThousandOneHundredElevenLightProductionsTheSyndicate(sb,obs)
                case '111lightproductions-gemburst-rush':
                        return OneThousandOneHundredElevenLightProductionsGemburstRush(sb,obs)
                case '111lightproductions-nfl-touchdown':
                        return OneThousandOneHundredElevenLightProductionsNFLTouchdown(sb,obs)
                case '111lightproductions-dragon-fortunes':
                        return OneThousandOneHundredElevenLightProductionsDragonFortunes(sb,obs)
                case '111lightproductions-legends-of-the-lost-grove':
                        return OneThousandOneHundredElevenLightProductionsLegendsOfTheLostGrove(sb,obs)
                case '111lightproductions-hearts-in-sync':
                        return OneThousandOneHundredElevenLightProductionsHeartsInSync(sb,obs)
                case '111lightproductions-sunset-serenade':
                        return OneThousandOneHundredElevenLightProductionsSunsetSerenade(sb,obs)
                case '1789studios-cat-war':
                        return OneThousandSevenHundredEightyNineStudiosCatWar(sb,obs)
                case _:
                        print('no subclass found')
from classes.nesting.EighteenGaming import EighteenGaming
from classes.classUtilityFunctions import cleanNumber, takePicture, findEmbeddedCoords, findCircles
from classes.Capture import Capture
from utilityFunctions import Sleep, MarkTheDom, ClickTheDom
from selenium.webdriver.common.action_chains import ActionChains
import time

slotCode = '18gaming-toppings-tantalizer'
closingWordsList = ['conratulations','congratulations', 'cong', 'tions','ratulations']
spinWordsList = ['free spins']

class ToppingsTantalizer(EighteenGaming):
    def __init__(self, sb, obs):
        super().__init__(sb, slotCode, obs)
        self.estimatedWaitTime = 120

        self.run()

    def setup(self):
        self.setupAutoSpin()
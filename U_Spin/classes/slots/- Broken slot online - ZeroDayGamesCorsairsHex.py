from classes.Slot import Slot
from selenium.webdriver.common.keys import Keys


class ZeroDayGamesCorsairsHex(Slot):
    def __init__(self, driver):
        super().__init__(driver)
        self.startingBalance = 1000.00
        self.sendingBalance = 0

        self.passSplashScreen()
        self.setup()
        # run
        # while check for same screenshots to see if game ended
        # record ending balance
    
    
    def setup(self):
        # go to fast mode
        spinCount = 250
        # select spin count 
        turboBtnStr = '[aria-label="Enable turbo"]'
        autoPlayStr = '.autospin-root'
        spinCountStr = f'//button[contains(@class, "rounds-btn") and contains(., "{spinCount}")]'
        startBtnStr = '.start-btn'
        
        self.driver.find_element(turboBtnStr).click()
        self.driver.find_element(autoPlayStr).click()
        self.driver.find_element(spinCountStr).click()
        self.driver.find_element(startBtnStr).click()
        pass

    def passSplashScreen(self):
        continueStr = '.intro-continue-btn'
        self.driver.switch_to_frame('iframe')
        continueBtn = self.driver.find_element(continueStr)
        continueBtn.click()

 

        

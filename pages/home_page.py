


import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LaunchPage():

    def __init__(self,driver, wait):
        self.driver = driver
        self.wait = wait


   # def homepage(self):
    #    time.sleep(5)

    def Whatsnewbutton(self):
         whatsnew = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@id='ui-id-3']")))
         time.sleep(2)
         whatsnew.click()
         time.sleep(4)


import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class womenpage:

    def __init__(self, driver,wait):
        self.wait = wait
        self.driver = driver





    def click_shopBytop_50(self):
        buttontop50 = self.wait.until(EC.element_to_be_clickable((By.XPATH , "//a[contains(text(),'Tops')]")))
        time.sleep(2)
        buttontop50.click()
        #//a[contains(text(),'Tops')]

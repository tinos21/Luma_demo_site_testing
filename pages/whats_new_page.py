
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class whatsnew():

    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait


    ### New in women's clickable links
    def test_TC02_click_Hoodies_Sweatshirts_women_verify_navigation(self):
        hoodie_shirts = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//main[@id='maincontent']//ul[1]//li[1]//a[1]")))
        time.sleep(1)
        hoodie_shirts.click()
        time.sleep(2)
        #################################################################
        tino_page_test =self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='base']")))

        # Wait for the page title element to be present
        page_title_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='base']"))
        )

        # Verify the page title text
        page_title_text = page_title_element.text
        assert page_title_text == "Hoodies & Sweatshirts", f"Expected title 'Hoodies & Sweatshirts', but got '{page_title_text}'"
        time.sleep(2)
        self.driver.back()  ## clicking the backward button
        print("Test Passed: Correct page loaded with title -", page_title_text)


    def test_TC03_click_Jackets_women_verify_navigation(self):
        pass

    def test_TC04_click_Tees_women_verify_navigation(self):
        pass

    def test_TC07_click_Bras_Tanks_women_verify_navigation(self):
        pass

    def test_TC08_click_Pants_women_verify_navigation(self):
        pass

    def test_TC09_click_Shorts_women_verify_navigation(self):
        pass




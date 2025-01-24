import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

import pytest



@pytest.fixture(scope="class")
def setup(request):
    # Path to chromedriver
    chromedriver_path = '/Users/tinopro14/browser_drivers/chromedriver-mac-arm64/chromedriver'
    # Initialize the Chrome WebDriver service
    service = Service(executable_path=chromedriver_path)

    # Chrome options
    options = webdriver.ChromeOptions()

    # Optional: Uncomment the next line to run the browser in headless mode
    # options.add_argument("--headless")

    # Initialize WebDriver with the service object and options
    driver = webdriver.Chrome(service=service, options=options)

    # Explicit wait (set to 60 seconds)
    wait = WebDriverWait(driver, 60)

    # Open magento
    driver.get("https://magento.softwaretestingboard.com/")
    time.sleep(1)
    driver.maximize_window()

    # Assign driver and wait to the test class
    request.cls.driver = driver
    request.cls.wait = wait
    # Ensure the test completes before closing the driver
    yield
    # Cleanup after test
    time.sleep(10)
    driver.quit()  # Quit the driver at the end of the test

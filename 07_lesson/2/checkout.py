from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Сheckout:
    def __init__(self, browser):
        self.driver = browser

    def button_checkout(self):
            self.checkout_button = self.driver.find_element(By.ID, "checkout").click()
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:

    def __init__(self, driver): 
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def input_field(self):
        number = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        number.clear()
        number.send_keys("45")

    def input_symbols(self):
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    def result(self):
        res = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert res == "15"





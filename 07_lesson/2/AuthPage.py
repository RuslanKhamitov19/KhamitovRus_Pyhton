
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Authorization:

    def __init__(self, browser):
        self.driver = browser
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        
    def string_un(self):
        self.username = self.driver.find_element(By.ID, ("user-name")).send_keys("standard_user")
        
    def string_pw(self):
        self.password = self.driver.find_element (By.ID, ("password")).send_keys("secret_sauce")
        
    def button_log(self):
        self.button = self.driver.find_element(By.ID, ("login-button")).click()

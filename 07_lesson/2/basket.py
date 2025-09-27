from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Basket:
    def __init__(self, browser):
        self.driver = browser
        
    def remove(self):
        self.backpack = self.driver.find_element(By.ID, ("add-to-cart-sauce-labs-backpack")).click()
        self.bts = self.driver.find_element(By.ID, ("add-to-cart-sauce-labs-bolt-t-shirt")).click()
        self.onesie = self.driver.find_element(By.ID, ("add-to-cart-sauce-labs-onesie")).click()
        self.bl = self.driver.find_element(By.ID, ("add-to-cart-sauce-labs-bike-light")).click()
        self.fj = self.driver.find_element(By.ID, ("add-to-cart-sauce-labs-fleece-jacket")).click()
        self.tsr = self.driver.find_element(By.ID, ("add-to-cart-test.allthethings()-t-shirt-(red)")).click()
        
    def basket(self):
        self.cart_link = self.driver.find_element(By.CLASS_NAME, ("shopping_cart_link")).click()

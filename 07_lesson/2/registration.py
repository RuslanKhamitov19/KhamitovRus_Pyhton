from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Registration:

    def __init__(self, browser):
        self.driver = browser
        
    def input_info(self, first_name, last_name, post_code):
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code"). send_keys(post_code)
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
        self.driver.implicitly_wait(4)
        
    def check_price(self):
        result_text = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        print(result_text)
        assert "$140.34" in result_text

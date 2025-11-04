from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("http://the-internet.herokuapp.com/login")

sleep(5)

username = driver.find_element(By.CSS_SELECTOR, "input#username")
username.send_keys("tomsmith")
password = driver.find_element(By.CSS_SELECTOR, "input#password")
password.send_keys("SuperSecretPassword!")

button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
flash = driver.find_element(By.CSS_SELECTOR, "div#flash")
print (flash.text)

sleep(5)

driver.quit()
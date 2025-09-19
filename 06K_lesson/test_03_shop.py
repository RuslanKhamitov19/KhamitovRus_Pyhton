from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("https://www.saucedemo.com/")
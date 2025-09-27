import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from AuthPage import Authorization
from basket import Basket
from checkout import Сheckout
from registration import Registration

def test_shop():
    options = webdriver.FirefoxOptions()
    browser = webdriver.Firefox(options=options)

    auth_page = Authorization(browser)
    auth_page.string_un()
    auth_page.string_pw()
    auth_page.button_log()
    
    page_basket = Basket(browser)
    page_basket.remove()
    page_basket.basket()

    check_page = Сheckout(browser)
    check_page.button_checkout()

    reg_page = Registration(browser)
    reg_page.input_info("Кристина", "Хамитова", "454000")
    reg_page.check_price()


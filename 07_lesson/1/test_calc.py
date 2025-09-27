from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from СalcPage import CalculatorPage

def test_slow_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    calc_page = CalculatorPage(browser)
    calc_page.input_field()
    calc_page.input_symbols()
    calc_page.result()


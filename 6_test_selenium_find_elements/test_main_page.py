import time

from selenium.webdriver.common.by import By
from locators import MainPage
from locators import SearchPage


def test_search_product(parametrize_browser):
    bro = parametrize_browser
    bro.maximize_window()
    bro.find_element(By.CSS_SELECTOR, MainPage.MainPage.search_field).send_keys("iphone")
    bro.find_element(By.CSS_SELECTOR, MainPage.MainPage.search_button).click()
    #time.sleep(10)
    bro.find_element(By.CSS_SELECTOR, SearchPage.SearchPage.product)

import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#css selector ->>>>> [class="btn btn-lg btn-primary btn-add-to-basket"]
def test_find_basket_button(browser) :
    browser.get(link)
    basket_button = browser.find_elements_by_css_selector("[class='btn btn-lg btn-primary btn-add-to-basket']")
    """
    !!!!!!! the examiner has himself add time.sleep !!!!!!!
    """
    #time.sleep(5)
    assert basket_button,"There is no element of basket button"

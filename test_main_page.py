from .pages.main_page import MainPage
from .pages.main_page import BasePage
from selenium.webdriver.common.by import By
from .pages.login_page import LoginPage
from .pages.locators import BasketPageLocators
import pytest

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket() 
    assert page.is_not_element_present(*BasketPageLocators.PRODUCT), "Product is presented, but should not be"
    assert page.is_element_present(*BasketPageLocators.MESSAGE_BASKET), "Basket isn't empty" 





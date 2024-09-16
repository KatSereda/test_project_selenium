from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from .pages.locators import ProductPageLocators

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.MESSAGE_ADDING), "Success message is presented, but should not be"
         
    
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.MESSAGE_ADDING), "Success message is presented, but should not be"
        
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    time.sleep(1) 
    assert page.is_disappeared(*ProductPageLocators.MESSAGE_ADDING), "Sucsess messege isn't disappeared"

         

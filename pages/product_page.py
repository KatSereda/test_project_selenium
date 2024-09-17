from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators
from .locators import BasketPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()
    
    def message_about_product_in_basket(self):
        product = self.is_element_present(*ProductPageLocators.MESSAGE_ADDING)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        assert product, "Product isn't adding to the basket"
        assert product_name.text == product_name_message.text, "Product is incorrect"

    def message_about_basket_price(self):
        message_price = self.is_element_present(*ProductPageLocators.MESSAGE_PRICE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        message_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE)
        assert message_price, "Product isn't adding to the basket"
        assert product_price.text == message_price.text, "Product's price is incorrect"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADDING), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADDING), \
            "Success message is not disappeared"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT), "Product is presented, but should not be"
        #Ожидаем, что в корзине нет товаров

    def should_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET), "Basket isn't empty"

           
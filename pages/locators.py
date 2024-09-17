from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ADDING = (By.CSS_SELECTOR, ".alert:nth-child(1)") 
    MESSAGE_PRICE = (By.CSS_SELECTOR, ".alert:nth-child(3)")   
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, "//div[@class='alertinner ']/strong")
    PRODUCT_NAME = (By.XPATH, "//h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color:nth-child(2)")
    PRICE_IN_MESSAGE = (By.XPATH, "//div[@class='alertinner ']/p/strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    PRODUCT = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_BASKET = (By.XPATH, "//p[contains(text(), 'empty')]")
  

from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ADDING = (By.CSS_SELECTOR, ".alert:nth-child(1)") 
    MESSAGE_PRICE = (By.CSS_SELECTOR, ".alert:nth-child(3)")   
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, "//div[@class='alertinner ']/strong")
    PRODUCT_NAME = (By.XPATH, "//h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color:nth-child(2)")
    PRICE_IN_MESSAGE = (By.XPATH, "//div[@class='alertinner ']/p/strong")
  

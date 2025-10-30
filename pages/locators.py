from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocator():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    from selenium.webdriver.common.by import By

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alert-success strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "div.alert-info")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert-info strong")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn-default")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
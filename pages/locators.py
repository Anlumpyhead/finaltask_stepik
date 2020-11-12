from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#register_form #id_registration-email")
    REG_PASS = (By.CSS_SELECTOR, "#register_form #id_registration-password1")
    REG_PASS_CONF = (By.CSS_SELECTOR, "#register_form #id_registration-password2")
    REG_BTN = (By.NAME, "registration_submit")
    
class ProductPageLocators():
    BTN_CARD = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_TO_CART = (By.CSS_SELECTOR, ".alert-success:first-child .alertinner strong")
    PRICE_TO_CART = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "checkout-quantity")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner")
    
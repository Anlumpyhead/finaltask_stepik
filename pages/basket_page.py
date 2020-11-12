from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
#проверка на то что в корзине нет товаров
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Success message is presented, but should not be"

#проверка на текст о пустой корзине           
    def should_be_text_about_empty_basket(self):
        basket_text_message = self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET).text
        assert 'Your basket is empty' in basket_text_message, \
            'The basket is not exist the message that basket is empty'
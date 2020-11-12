from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        #найти кнопку и добавить товар в корзину
        btn = self.browser.find_element(*ProductPageLocators.BTN_CARD)
        btn.click()
       
    def right_book_and_right_price_message(self):
        self.should_be_right_book_name()
        self.should_be_right_price_for_book()        
      
    def should_be_right_book_name(self):
        # проверка сообщения о добавлении в корзину нужной книги
        title_of_book = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_in_cart = self.browser.find_element(*ProductPageLocators.BOOK_TO_CART).text
        assert title_of_book == book_in_cart, 'book title is not the same'
     
    def should_be_right_price_for_book(self):
        # проверка сообщения о цене товара в корзине
        price_of_book = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        cart_total = self.browser.find_element(*ProductPageLocators.PRICE_TO_CART).text
        assert price_of_book == cart_total, 'price of book is not mutch'
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_TO_CART), \
           "Success message is presented, but should not be"
           
    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.BOOK_TO_CART),  \
            "Success message is presented, but should be disappeared"

         
    
     
    
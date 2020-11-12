from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import pytest


product_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"

@pytest.mark.user_test
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        #сетап функция, которая выполняется перед запуском каждого теста - 
        #открывает страницу регистрации, регистрирует пользователя и проверяет, пользователь залогинен
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        login_page.register_new_user(email=email, password=password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open() #открываем страницу
        page.should_not_be_success_message()
    
    @pytest.mark.need_review    
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open() #открываем страницу
        page.add_to_cart()  # добавляем товар в корзину
        page.right_book_and_right_price_message()

#@pytest.mark.parametrize('promo_code', ["0","1", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
#def test_guest_can_add_product_to_basket(browser, promo_code):
#    link = ('http://selenium1py.pythonanywhere.com/catalogue/'
#                   'coders-at-work_207/?promo=offer{}'.format(promo_code))
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open() #открываем страницу
    
    page.add_to_cart()  # добавляем товар в корзину
    page.solve_quiz_and_get_code()
    page.right_book_and_right_price_message()

@pytest.mark.skip   
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open() #открываем страницу
    page.add_to_cart()  # добавляем товар в корзину
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open() #открываем страницу
    page.should_not_be_success_message()
    
@pytest.mark.skip  
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open() #открываем страницу
    page.add_to_cart()  # добавляем товар в корзину
    page.should_be_disappeared()
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    
@pytest.mark.need_review    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_not_be_product_in_basket()
    page.should_be_text_about_empty_basket()
    
    
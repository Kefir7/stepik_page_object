Если программа выдает ERROR collecting test_main_page.py и ERROR collecting test_product_page.py
Замените в test_product_page.py 
вместо
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
это 
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

И в test_main_page.py
вместо
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
это
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

## Исправление импортов

Замените в тестовых файлах:

### В `test_product_page.py`
```python
# Было:
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

# Стало:
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

### В `test_main_page.py`
# Было:
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

# Стало:
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

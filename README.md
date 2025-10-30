## Исправление импортов

Замените в тестовых файлах: если будут ошибки ERROR collecting test_product_page.py и ERROR collecting test_main_page.py

### В `test_product_page.py`
```python
# Было:
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

# Стало:
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

### В `test_main_page.py`
# Было:
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

# Стало:
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

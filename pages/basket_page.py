from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_items()
        self.should_be_empty_basket_message()
        
    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, \
        "Basket url is not correct"
        
    def should_be_basket_items(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), \
        "Basket items section is not presented"
        
    def should_be_empty_basket(self):
        self.should_not_be_basket_items()
        self.should_be_empty_basket_text()

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
        "Empty basket message is not presented"
        
    def should_not_be_basket_items(self):
        # Отрицательная проверка - товаров в корзине быть не должно
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
        "Basket items are presented, but should not be"
        
    def should_be_empty_basket_text(self):
        # Проверяем текст о пустой корзине
        empty_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        expected_text = "Your basket is empty"  # или другой текст в зависимости от языка
        assert expected_text in empty_message, f"Empty basket text is not correct. Expected: {expected_text},\
        got: {empty_message}"
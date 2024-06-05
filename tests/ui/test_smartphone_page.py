from modules.ui.page_objects.rozetka_Smartphone_in_page import RozetkaSmartphonePage
import pytest

@pytest.mark.rz
def test_rozetka_smartphone_page():
    # створення об'єкту сторінки
    rozetka_Smartphone_in_page = RozetkaSmartphonePage()

    # відкриваємо сторінку 'https://rozetka.com.ua/ua/xiaomi-6941812709726/p434702867/'
    rozetka_Smartphone_in_page.go_to()
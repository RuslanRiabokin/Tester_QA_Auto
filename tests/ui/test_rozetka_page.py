from modules.ui.page_objects.rozetka_sign_in_page import RozetkaSignInPage
import pytest


@pytest.mark.ui
def test_rozetka_username_page():
    # створення об'єкту сторінки
    rozetka_sign_in_page = RozetkaSignInPage()

    # відкриваємо сторінку https://seller.rozetka.com.ua/
    rozetka_sign_in_page.go_to()

    # виконуємо спробу увійти в систему GitHub
    rozetka_sign_in_page.try_login("0972620960r@gmail.com", "abcd")

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert rozetka_sign_in_page.get_title() == "Вхід - Особистий кабінет"

    # Закриваємо браузер
    rozetka_sign_in_page.close()

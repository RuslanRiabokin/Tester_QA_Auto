from modules.ui.page_objects.np_search_page import NpSearchInPage
import pytest


@pytest.mark.np
def test_np_search_page():
    # створення об'єкту сторінки
    np_search_page = NpSearchInPage()

    # відкриваємо сторінку https://novaposhta.ua/
    np_search_page.go_to()

    # Вводимо номер накладної
    np_search_page.enter_the_invoice_number("20450928489856")
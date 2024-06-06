from modules.ui.page_objects.np_search_page import NpSearchInPage
import pytest
import time


@pytest.mark.np
def test_np_search_page():
    # створення об'єкту сторінки
    np_search_page = NpSearchInPage()

    # відкриваємо сторінку https://novaposhta.ua/
    np_search_page.go_to()

    # Вводимо номер накладної
    np_search_page.enter_the_invoice_number("20450928489856")

    np_search_page.click_xpath('//*[@id="top_block"]/div[1]/div/div[2]/form/input[2]')
    time.sleep(5)
    np_search_page.click_xpath('//*[@id="chat"]/div[2]/button')

    # Перевіряемо, що текст статусу рівен "Отримана"
    assert np_search_page.get_status_text() == "Отримана"

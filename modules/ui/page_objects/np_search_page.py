from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_page import BasePage
import time

class NpSearchInPage(BasePage):
    URL = 'https://novaposhta.ua/'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(self.URL)
        self.driver.refresh()  # Перевантаження сторінки після її завантаження

    def enter_the_invoice_number(self, number):
        # Знаходимо поле, номер накладної
        invoice_number = self.driver.find_element(By.ID, "cargo_number")

        # Вводимо номер накладної
        invoice_number.send_keys(number)

    def click_xpath(self, xpath):
        # Знаходимо кнопку по XPATH та Емулюємо клік лівою кнопкою мишки
        self.driver.find_element(By.XPATH, xpath).click()

    def get_status_text(self):
        # Знаходимо элемент с текстом статусу
        status_element = self.driver.find_element(By.XPATH, '//*[@id="chat"]/header/div[2]/div[2]/div[2]')

        # Получаемо текст із элемента
        status_text = status_element.text

        return status_text








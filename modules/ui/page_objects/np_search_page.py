from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_page import BasePage
import time

class NpSearchInPage(BasePage):
    URL = 'https://novaposhta.ua/'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(self.URL)

    def enter_the_invoice_number(self, number):
        # Знаходимо поле, номер накладної
        invoice_number = self.driver.find_element(By.ID, "cargo_number")

        # Вводимо номер накладної
        invoice_number.send_keys(number)

        time.sleep(10)

        # Закрываем браузер
        self.driver.quit()


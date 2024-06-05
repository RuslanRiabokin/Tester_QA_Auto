from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_page import BasePage
import time


class RozetkaSmartphonePage(BasePage):
    URL = 'https://rozetka.com.ua/ua/xiaomi-6941812709726/p434702867/'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(RozetkaSmartphonePage.URL)

        # Знаходимо кнопку Купити
        btn_elem = self.driver.find_element(By.CSS_SELECTOR, 'button.buy-button')

        # Емулюємо клік лівою кнопкою мишки
        btn_elem.click()

        time.sleep(10)

        # Закрываем браузер
        self.driver.quit()
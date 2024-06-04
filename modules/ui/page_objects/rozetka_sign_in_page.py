from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_page import BasePage


class RozetkaSignInPage(BasePage):
    URL = 'https://seller.rozetka.com.ua/'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(RozetkaSignInPage.URL)

    def try_login(self, username, password):
        # Знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
        login_elem = self.driver.find_element(By.ID, "username")

        # Вводимо неправильне ім'я користувача або поштову адрІесу
        login_elem.send_keys(username)

        # Знаходимо поле, в яке будемо вводити неправильний пароль
        pass_elem = self.driver.find_element(By.ID, "password")

        # Вводимо неправильний пароль
        pass_elem.send_keys(password)

        # Знаходимо кнопку Увійти
        btn_elem = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

        # Емулюємо клік лівою кнопкою мишки
        btn_elem.click()

    def get_title(self):
        return self.driver.title




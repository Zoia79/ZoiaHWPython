import allure
from selenium.webdriver.common.by import By


class ClassPersonalInfo:

    def __init__(self, browser):
        self._driver = browser

    @allure.step("Заполнить поле имя")
    def first_name(self, term: str) -> None:
        """
        Заполняет поле "имя"
        :param term:
        :return:
        """
        self._driver.find_element(By.ID, 'first-name').send_keys(term)

    @allure.step("Заполнить поле фамилия")
    def last_name(self, term: str) -> None:
        """
        Заполняет поле "фамилия"
        :param term:
        :return:
        """
        self._driver.find_element(By.ID, 'last-name').send_keys(term)

    @allure.step("Заполнить поле индекс")
    def postal_code(self, term: int) -> None:
        """
        Заполяет поле "индекс"
        :param term:
        :return:
        """
        self._driver.find_element(By.ID, 'postal-code').send_keys(term)

    @allure.step("Нажать продолжить")
    def continue_btn(self) -> None:
        """
        Нажимает продолжить
        :return:
        """
        self._driver.find_element(By.ID, 'continue').click()

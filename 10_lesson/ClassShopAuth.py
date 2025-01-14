import allure
from selenium.webdriver.common.by import By


class ClassShopAuth:

    def __init__(self, browser):
        self._driver = browser

    @allure.step("Открыть сайт")
    def get(self):
        """
        открыть сайт
        :return:
        """
        self._driver.get(
            "https://www.saucedemo.com/")

    @allure.step("Ввести логин ")
    def username(self, term):
        """
        Ввести логин
        :param term:
        :return:
        """
        self._driver.find_element(By.ID, 'user-name').send_keys(term)

    @allure.step("Ввести пароль")
    def password(self, term):
        """
        ввести пароль
        :param term:
        :return:
        """
        self._driver.find_element(By.ID, 'password').send_keys(term)

    @allure.step("Нажать Login")
    def login(self):
        """
        Нажимает Login
        :return:
        """
        self._driver.find_element(By.ID, 'login-button').click()

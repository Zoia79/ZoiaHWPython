import allure
from selenium.webdriver.common.by import By


class ClassForm:

    def __init__(self, browser):
        self._driver = browser

    @allure.step("Открыть браузер")
    def get(self):
        """
        открыть браузер
        """
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    @allure.step("Заполнить форму")
    def put_data(self) -> None:
        """
        Заполняет форму
        :return:
        """
        form_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        for field, value in form_data.items():
            self._driver.find_element(By.CSS_SELECTOR,
                                      f"[name={field}]").send_keys(value)

    @allure.step("Нажать подтвердить")
    def submit(self) -> None:
        """
        Нажимает подтвердить
        :return:
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "button[type=submit]").click()

    @allure.step("Проверить что заполненные поля зеленые")
    def success(self):
        """
        Проверяет что заполненные поля
        :return:
        """
        form_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }
        for field_id in list(form_data.keys()):
            assert ("alert-success" in self._driver.find_element(
              By.ID, field_id).get_attribute("class"))

    @allure.step("Проверяет что Zip code красное")
    def danger(self):
        """
        Проверяет что поле zip-code не заполнено
        :return:
        """
        assert ("alert-danger" in self._driver.find_element(
            By.ID, 'zip-code').get_attribute("class")
                )

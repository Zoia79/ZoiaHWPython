import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ClassCalc:

    def __init__(self, browser):
        self._driver = browser

    @allure.step("Открыть браузер")
    def get(self):
        """
        Открывает браузер
        :return:
        """
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Очистить таймер")
    def clear_time(self) -> None:
        """
        Очищает таймер
        :return:
        """
        self._driver.find_element(By.ID, 'delay').clear()

    @allure.step("Установить новое время в таймере")
    def set_time(self, term: int) -> None:
        """
        Устанавливает новое значение в таймере
        """
        self._driver.find_element(By.ID, 'delay').send_keys(term)

    @allure.step("Нажать на 7")
    def seven(self) -> None:
        """
        Нажимает на 7
        """
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()

    @allure.step("Нажать на +")
    def plus(self) -> None:
        """
        Нажимает на  +
        """
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()

    @allure.step("Нажать на 8")
    def eight(self) -> None:
        """
        Нажимает на 8
        """
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()

    @allure.step("Нажать на =")
    def equals(self) -> None:
        """
        Нажимает на =
        """
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    @allure.step("Подождать результат вычисления")
    def wait(self):
        """
        Ожидает
        """
        wait = WebDriverWait(self._driver, 50)
        result = wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "div.screen"), "15"
            )
        )
        assert result, f"Expected '15', but got {result}"

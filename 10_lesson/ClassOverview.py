import allure
from selenium.webdriver.common.by import By


class ClassOverview:

    def __init__(self, browser):
        self._driver = browser

    @allure.step("Проверить что итоговая сумма ровна 58.29")
    def total(self):
        """
        Сравнивает чтобы сумма совпадала
        """
        total_text = self._driver.find_element(
            By.CLASS_NAME, 'summary_total_label').text
        total = float(total_text.split(" ")[1][1:])
        expected_total = 58.29
        assert total == expected_total, \
            f"Expected '{expected_total}', but got {total}"

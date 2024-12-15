from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ClassCalc:

    def __init__(self, browser):
        self._driver = browser

    def get(self):
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def clear_time(self):
        self._driver.find_element(By.ID, 'delay').clear()

    def set_time(self, term):
        self._driver.find_element(By.ID, 'delay').send_keys(term)

    def seven(self):
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()

    def plus(self):
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()

    def eight(self):
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()

    def equals(self):
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    def wait(self):
        wait = WebDriverWait(self._driver, 50)
        result = wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "div.screen"), "15"
            )
        )
        assert result, f"Expected '15', but got {result}"

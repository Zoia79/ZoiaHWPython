from selenium.webdriver.common.by import By


class ClassPersonalInfo:

    def __init__(self, browser):
        self._driver = browser

    def first_name(self, term):
        self._driver.find_element(By.ID, 'first-name').send_keys(term)

    def last_name(self, term):
        self._driver.find_element(By.ID, 'last-name').send_keys(term)

    def postal_code(self, term):
        self._driver.find_element(By.ID, 'postal-code').send_keys(term)

    def continue_btn(self):
        self._driver.find_element(By.ID, 'continue').click()

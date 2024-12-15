from selenium.webdriver.common.by import By


class ClassShopAuth:

    def __init__(self, browser):
        self._driver = browser

    def get(self):
        self._driver.get(
            "https://www.saucedemo.com/")

    def username(self, term):
        self._driver.find_element(By.ID, 'user-name').send_keys(term)

    def password(self, term):
        self._driver.find_element(By.ID, 'password').send_keys(term)

    def login(self):
        self._driver.find_element(By.ID, 'login-button').click()

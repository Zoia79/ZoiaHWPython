from selenium.webdriver.common.by import By


class ClassForm:

    def __init__(self, browser):
        self._driver = browser

    def get(self):
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def put_data(self):
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

    def submit(self):
        self._driver.find_element(
            By.CSS_SELECTOR, "button[type=submit]").click()

    def success(self):
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

    def danger(self):
        assert ("alert-danger" in self._driver.find_element(
            By.ID, 'zip-code').get_attribute("class")
                )

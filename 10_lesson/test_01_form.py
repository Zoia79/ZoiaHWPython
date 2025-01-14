import allure
from selenium import webdriver
from ClassForm import ClassForm


@allure.story("Проверка заполнения обязательных полей в форме")
@allure.feature("Форма")
@allure.title("Форма для заполнения")
@allure.description("Проверяем что поле Zip code подсвечено красным. Остальные поля подсвечены зеленым.")
@allure.severity("critical")
def test_form():
    browser = webdriver.Chrome()

    class_form = ClassForm(browser)
    class_form.get()
    class_form.put_data()
    class_form.submit()
    class_form.success()
    class_form.danger()
    browser.quit()

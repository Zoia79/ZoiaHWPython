from selenium import webdriver
from ClassForm import ClassForm


def test_form():
    browser = webdriver.Chrome()

    class_form = ClassForm(browser)
    class_form.get()
    class_form.put_data()
    class_form.submit()
    class_form.success()
    class_form.danger()
    browser.quit()

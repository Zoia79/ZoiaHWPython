from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from ClassCalc import ClassCalc


def test_calc():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    class_calc = ClassCalc(browser)
    class_calc.get()
    class_calc.clear_time()
    class_calc.set_time('45')
    class_calc.seven()
    class_calc.plus()
    class_calc.eight()
    class_calc.equals()
    class_calc.wait()
    browser.quit()

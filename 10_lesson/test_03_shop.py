import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from ClassShopAuth import ClassShopAuth
from ClassShopInventory import ClassShopInventory
from ClassPersonalInfo import ClassPersonalInfo
from ClassOverview import ClassOverview


@allure.story("Проверка работы сайта магазина")
@allure.feature("Магазин")
@allure.title("Расчет суммы в онлайн магазине")
@allure.description("Проверяет что итоговая сумма равна $58.29.")
@allure.severity("critical")
def test_shop():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    classshopauth = ClassShopAuth(browser)
    classshopauth.get()
    classshopauth.username("standard_user")
    classshopauth.password("secret_sauce")
    classshopauth.login()

    classshopinventory = ClassShopInventory(browser)
    classshopinventory.backpack()
    classshopinventory.tshirt()
    classshopinventory.onesie()
    classshopinventory.go_to_cart()
    classshopinventory.checkout()

    classpersonalinfo = ClassPersonalInfo(browser)
    classpersonalinfo.first_name("Zoia")
    classpersonalinfo.last_name("Tumorkhonova")
    classpersonalinfo.postal_code("670024")
    classpersonalinfo.continue_btn()

    classoverview = ClassOverview(browser)
    classoverview.total()
    browser.quit()

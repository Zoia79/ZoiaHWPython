import allure
from selenium.webdriver.common.by import By


class ClassShopInventory:

    def __init__(self, browser):
        self._driver = browser

    @allure.step("Нажать Add to card у товара Sauce Labs Backpack")
    def backpack(self):
        """
        Добавить в корзину рюкзак
        :return:
        """
        self._driver.find_element(By.ID,
                                  'add-to-cart-sauce-labs-backpack').click()

    @allure.step("Нажать Add to card у товара Sauce Labs Bolt T-Shirt")
    def tshirt(self):
        """
        добавить в корзину футболку
        :return:
        """
        self._driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt'
        ).click()

    @allure.step("Нажать Add to card у товара Sauce Labs Onesie")
    def onesie(self):
        """
        добавить в корзину боди
        :return:
        """
        self._driver.find_element(By.ID,
                                  'add-to-cart-sauce-labs-onesie').click()

    @allure.step("Нажать на корзину")
    def go_to_cart(self):
        """
        перейти в корзину
        :return:
        """
        self._driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    @allure.step("Нажать на Checkout")
    def checkout(self):
        """
        пройти дальше
        :return:
        """
        self._driver.find_element(By.ID, 'checkout').click()

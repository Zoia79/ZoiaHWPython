from selenium.webdriver.common.by import By


class ClassShopInventory:

    def __init__(self, browser):
        self._driver = browser

    def backpack(self):
        self._driver.find_element(By.ID,
                                  'add-to-cart-sauce-labs-backpack').click()

    def tshirt(self):
        self._driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt'
        ).click()

    def onesie(self):
        self._driver.find_element(By.ID,
                                  'add-to-cart-sauce-labs-onesie').click()

    def go_to_cart(self):
        self._driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    def checkout(self):
        self._driver.find_element(By.ID, 'checkout').click()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_shop():

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, 'user-name').send_keys("standard_user")
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.ID, 'login-button').click()

    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    driver.find_element(By.ID, 'checkout').click()

    driver.find_element(By.ID, 'first-name').send_keys('Zoya')
    driver.find_element(By.ID, 'last-name').send_keys('Tumorkhonova')
    driver.find_element(By.ID, 'postal-code').send_keys('670024')

    driver.find_element(By.ID, 'continue').click()

    total_text = driver.find_element(By.CLASS_NAME, 'summary_total_label').text

    total = float(total_text.split(" ")[1][1:])

    expected_total = 58.29
    assert total == expected_total, \
        f"Expected '{expected_total}', but got {total}"

    driver.quit()

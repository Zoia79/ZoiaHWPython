from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait

# Откройте страницу
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://uitestingplayground.com/classattr")

button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
button.click()
wait = WebDriverWait(driver, timeout=10)
alert = wait.until(lambda d: d.switch_to.alert)
text = alert.text
alert.accept()
assert text == "Primary button pressed"

# button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
# button.click()
# button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
#button.click()
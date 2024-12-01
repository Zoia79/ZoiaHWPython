from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")
button = driver.find_element(By.CSS_SELECTOR, '[type="number"]')
button.send_keys("1000")
button.clear()
button.send_keys("999")
driver.quit()
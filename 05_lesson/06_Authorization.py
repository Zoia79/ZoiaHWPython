from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
button = driver.find_element(By.ID, 'username')
button.send_keys("tomsmith")
button = driver.find_element(By.ID, 'password')
button.send_keys("SuperSecretPassword!")
button = driver.find_element(By.CSS_SELECTOR, 'i.fa.fa-2x.fa-sign-in')
button.click()
sleep(5)
driver.quit()
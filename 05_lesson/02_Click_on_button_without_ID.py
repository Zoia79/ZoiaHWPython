from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Откройте страницу
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://uitestingplayground.com/dynamicid")

button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")
sleep(5)
button.click()

button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")
sleep(5)
button.click()

button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")
sleep(5)
button.click()

sleep(5)
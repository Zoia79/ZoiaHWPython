from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

driver.find_element(By.ID, 'landscape')

find = driver.find_element(By.ID, 'award').get_attribute("src")
print(find)
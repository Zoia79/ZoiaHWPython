from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://uitestingplayground.com/textinput")

rename = driver.find_element(By.ID, 'newButtonName')
rename.send_keys("SkyPro")
driver.find_element(By.ID, 'updatingButton').click()
new_name = driver.find_element(By.ID, 'updatingButton').text
print(new_name)
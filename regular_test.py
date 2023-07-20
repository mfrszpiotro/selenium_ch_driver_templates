from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Set up the WebDriver to connect to an existing Chrome session
options = webdriver.ChromeOptions()
options.debugger_address = "localhost:9222"  # Replace with the actual address of the existing Chrome session in debug mode
driver = webdriver.Chrome(options=options)
driver.get("https://nowsecure.nl")
test_btn = driver.find_element(By.CSS_SELECTOR, "div")
test_btn.click()
sleep(2)
div_elements = driver.find_elements(By.CSS_SELECTOR, "div.sc-koErNt.jYRhog")
driver.quit()
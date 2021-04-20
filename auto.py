from selenium import webdriver
import time

options = webdriver.ChromeOptions()
driver = webdriver.Remote('http://localhost:4444/wd/hub', options.to_capabilities())
driver.get("http://web.whatsapp.com")
time.sleep(30)
driver.quit()
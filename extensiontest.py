from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time

ext = webdriver.ChromeOptions()
ext.add_extension(r"/NopeCHA/NopeCha Extension.crx")

driver = webdriver.Chrome(chrome_options=ext)


url = "https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php"
driver.get(url)

time.sleep(10)

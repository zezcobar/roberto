from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="c:\webdrivers\chromedriver.exe")
driver.get("https://pt.aliexpress.com/af/redmi.html?d=y&origin=n&SearchText=redmi&catId=0&spm=a2g0o.best.1000002.0&initiative_id=SB_20220923070709")

navegador.get('https://pt.aliexpress.com/')
navegador.find_element(By.ID, 'search-key').send_keys('Redmi')
navegador.find_element(By.CLASS_NAME,'search-button').submit()
navegador.find_element(By.TAG_NAME,'a')
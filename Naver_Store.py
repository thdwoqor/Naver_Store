import selenium
import chromedriver_autoinstaller
import time
import subprocess

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  #크롬드라이버 버전 확인
global driver
try:
    subprocess.Popen(f"C:\Program Files\Google\Chrome\Application\chrome.exe https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com --new-window --remote-debugging-port=9222 --user-data-dir=C:\\Temp")
except:
    subprocess.Popen(f"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com --new-window --remote-debugging-port=9222 --user-data-dir=C:\\Temp")
time.sleep(5)

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe',options=chrome_options)   
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe',options=chrome_options)

# driver.implicitly_wait(time_to_wait=5)

# URL = 'https://smartstore.naver.com/darkr8m/products/6043162971'
URL = 'https://smartstore.naver.com/pangppp/products/4923264887?'
driver.get(url=URL)

while True:
    try:
        driver.find_element_by_class_name("_2-uvQuRWK5")
        break
    except:
        driver.get(url=URL)
        time.sleep(0.1)
        print("NoSuchElement")

driver.find_element_by_class_name("_2-uvQuRWK5").click()

driver.implicitly_wait(time_to_wait=5)

driver.find_element_by_class_name("btn_payment").click()

#https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/
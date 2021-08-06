import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import os

option = Options()
option.headless = True

#driver = webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver.exe",options=option)
driver = webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")

#driver = webdriver.Chrome()

url = "https://contratos.comprasnet.gov.br/transparencia/terceirizados"

driver.get(url)

time.sleep(2)

tabela = driver.find_element_by_xpath("//div[@class='overflow-hidden']")
html_content = tabela.get_attribute('outerHTML')
print(html_content)

driver.quit()







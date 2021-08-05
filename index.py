#PIP: 
# pip install requests2
# pip install pandas
# pip install lxml
# pip install beautifulsoup4
# pip install selenium 

#Dependecias do projeto 
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

# Grab content from URL (Pegar conteúdo HTML a partir da URL)
url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"

option = Options()
option.headless = True
#driver = webdriver.Firefox(options=option)
driver = webdriver.Firefox()

driver.get("https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1")
driver.quit()


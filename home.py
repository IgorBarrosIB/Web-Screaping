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

dados = driver.find_element_by_xpath("//div[@id='crudTable_wrapper']//div[@class='col-sm-12']")
html_content = dados.get_attribute('outerHTML')


# Parsear o conteúdo HTML - BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
informacao = soup.findAll('span')


# 3. Estruturar conteúdo em um Data Frame - Pandas
df_full = pd.read_html(str(informacao))[0].head
df = df_full[['Órgão', 'CPF', 'Nome', 'Função', 'Salário']]
df.columns = ['Órgão','CPF', 'Nome', 'Função', 'Salário']
print(df_full)


driver.quit()




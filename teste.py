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

# Pegando os nomes das colunas da tabela
colunas = {i: col.getText() for i, col in enumerate(soup.find('table', {'id': 'crudTable'}).find('thead').findAll('th'))}
colunas_names = [col.getText() for col in soup.find('table', {'id': 'crudTable'}).find('tbody').findAll('td')]

# Criando um DataFrame com os nomes das colunas
dados = pd.DataFrame(columns=colunas_names)

print(dados)

# Pegando os dados da tabela por linha
for i in range(len(soup.find('table', {'id': 'crudTable'}).find('thead').findAll('th'))):
    linha = soup.find('table', {'id': 'crudTable'}).find('tbody').findAll('td')[i].getText().split('\n')[1:]
    inserir_linha = pd.DataFrame(linha).T.rename(columns=colunas)
    #dados = pd.concat([dados, inserir_linha], ignore_index=True)

# É tetra!




driver.quit()




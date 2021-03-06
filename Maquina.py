import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

import json
import os

option = Options()
option.headless = True

driver = webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver.exe",options=option)
#driver = webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.set_window_size(2500,900)

#url = "https://contratos.comprasnet.gov.br/transparencia/terceirizados"
url = "https://contratos.comprasnet.gov.br/transparencia/terceirizados?orgao=%5B%2244207%22%5D"

driver.get(url)

#selecionar os valores filtro

#select_xpath = "//div[@id='bs-example-navbar-collapse-1']//ul//li[@filter-name='orgao']"
#select_element = driver.find_element_by_xpath(select_xpath).click()

#select_valor = "//ul[@class='select2-results']//li//div[@id='select2-result-label-4']"
#valor_element = driver.find_element_by_xpath(select_valor).click()

#time.sleep(2)

# Selecionar todos os valores 
span_xpath = "//select[@name='crudTable_length']//option[@value='-1']"
span_element = driver.find_element_by_xpath(span_xpath).click()

time.sleep(20)

#Selecionando a tabela
dados = driver.find_element_by_xpath("//div[@id='crudTable_wrapper']//div[@class='col-sm-12']")
html_content = dados.get_attribute('outerHTML')


# Parsear o conteúdo HTML - BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(id='crudTable')

# Data Structure Conversion (Estruturar conteúdo em um Data Frame) - Pandas
df_full = pd.read_html(str(table))[0]
df = df_full[['Órgão', 'Unidade Gestora', 'Número Contrato', 'CPF', 'Nome', 'Função', 'Jornada', 'Salário', 'Data Início', 'Situação']]
df.columns = ['Órgão', 'Unidade Gestora', 'Número Contrato', 'CPF', 'Nome', 'Função', 'Jornada', 'Salário', 'Data Início', 'Situação']
driver.quit()

print(df)

# Transforma os dados em um Dicionario de dados próprio
#consulta = {}
#consulta['informacao'] = df.to_dict('records')
#print(consulta)

# Converter e salvar em um arquivo JSON
#js = json.dumps(consulta)
#fp = open('consulta.json', 'w')
#fp.write(js)
#fp.close()
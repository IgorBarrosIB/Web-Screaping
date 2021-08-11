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

driver = webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver.exe",options=option)
driver.set_window_size(2500,900)

url = "https://contratos.comprasnet.gov.br/transparencia/terceirizados"

driver.get(url)

time.sleep(2)

# Selecionar todos os valores 
span_xpath = "//select[@name='crudTable_length']//option[@value='-1']"
span_element = driver.find_element_by_xpath(span_xpath).click()

time.sleep(400)

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
#consulta = df.query('Órgão=="44207 - INST.CHICO MENDES DE CONSER.DA BIODIVERSID "')

# Transforma os dados em um Dicionario de dados próprio
consulta = {}
consulta['informacao'] = df.to_dict('records')
driver.quit()

# Converter e salvar em um arquivo JSON
js = json.dumps(consulta)
fp = open('consulta.json', 'w')
fp.write(js)
fp.close()








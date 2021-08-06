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

# enter keyword to search
keyword = "geeksforgeeks"
  
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
  
# get element 
element = driver.find_element_by_link_text("Courses")
  
# get href attribute
print(element.get_attribute('href'))
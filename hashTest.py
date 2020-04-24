from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import FirefoxProfile
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from backports import configparser
import json

# some JSON:
x =  '{ "name":" ", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
y["name"] = "allan"
test = []
print(y)
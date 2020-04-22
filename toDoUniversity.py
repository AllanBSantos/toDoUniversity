from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import FirefoxProfile
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from backports import configparser
import os
import json
#test
def accessPortal():
    global browser
    link = "https://www.psxportalacademico.com.br/facp/index.php"
    firefoxOptions = Options() 
    browser = webdriver.Firefox(options=firefoxOptions) # abre o browser com as informações inseridas
    time.sleep(3)   
    browser.get(link)  #Aguarda alguns segundos pra dar tempo de abrir o browser 
    time.sleep(3)
    browser.maximize_window() # maximiza a tela pra não ser necessário o scroll
    time.sleep(3)
def loadElements():
    global userBox, passwordBox, loginButton
    wait = WebDriverWait(browser, 40)
    #wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "_3j8Pd")))
    userBox = browser.find_elements_by_class_name("box_login")[0] #browser.find_element_by_xpath("//span[@data-icon='clip']")
    passwordBox = browser.find_elements_by_class_name("box_login")[1]
    loginButton = browser.find_elements_by_class_name("btn_login")[1]
    #print(userBox,passwordBox)

def loadLoginData():
    global userName, password
    config = configparser.ConfigParser()
    path = os.getcwd()
    configPath = path +r"\\config.ini"
    print(configPath)
    config.read(configPath)
    section = "login"
    userName = config.get(section, 'userName')
    password = config.get(section,'password')
    print(password,userName)

def insertLoginData():
    userBox.send_keys(userName)
    time.sleep(1)
    passwordBox.send_keys(password)
    time.sleep(1)
    loginButton.click()

def accessTasks():
    time.sleep(3)
    taskMenu = browser.find_elements_by_xpath("//*[contains(text(), 'Atividades')]")[0]
    time.sleep(1)
    taskMenu.click()

def loadAllTasks():
    parentElement = browser.find_element_by_class_name("lovelyrow1")
    elementList = parentElement.find_elements_by_tag_name("td")
    taskModel = '{ "description":" ", "professor":"", "className":"", "status":"","deadline":""}'
    task = []#json.loads(taskModel)
    for x in range(len(elementList)): 
        #task[x] = json.loads(taskModel)
        #task[x]["description"] = elementList[x].text
        print(elementList[x].text)
        #até aqui estou pegando os dados de 1 unica task tenho que organizar ela agora e replicar para as demais. 


#access the web portal
accessPortal()
loadElements()
loadLoginData()
insertLoginData()
accessTasks()
loadAllTasks()
#donwloadDocumentsOfTasks()
#separateTasks()
#
##send data to whatsapp
#accesWhatsapp()
#loginOnWhatsapp()
#insertAttachment()
#enterMessage()
#sendMessage()


#WorkFlow

#if __name__ == "__main__":
#
#    while resp != 1:
#        
#        time.sleep(50)





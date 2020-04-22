from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import FirefoxProfile
import time

def accessPortal():
    link = "https://www.psxportalacademico.com.br/facp/index.php"
    firefoxOptions = Options() 
    browser = webdriver.Firefox(options=firefoxOptions) # abre o browser com as informações inseridas
    time.sleep(3)   
    browser.get(link)  #Aguarda alguns segundos pra dar tempo de abrir o browser 
    time.sleep(3)
    browser.maximize_window() # maximiza a tela pra não ser necessário o scroll
 


#access the web portal
accessPortal()
S
#loadLoginData()
#insertLoginData()
#accessTasks()
#loadAllTasks()
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





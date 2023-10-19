from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
import os


diretorio = os.getcwd()
chrome_options = Options()
chrome_options.add_argument(r"user-data-dir="+diretorio+"profile/zap")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://web.whatsapp.com/")
sleep(30)
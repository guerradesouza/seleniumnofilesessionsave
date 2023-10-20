from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

from time import sleep
import os


diretorio = os.getcwd()
chrome_options = Options()
chrome_options.add_argument(r"user-data-dir="+diretorio+"/profile/zap")
print(diretorio+"profile/zap")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
driver.get("https://web.whatsapp.com/")


#input("Depois de ler o QRCode clique aqui e dê ENTER")


#API edita codigo bcBiFKbdkQR8c73dNQAlfG0SOZYqmosB
chave = "bcBiFKbdkQR8c73dNQAlfG0SOZYqmosB"
api = requests.get("https://editacodigo.com.br/index/api-whatsapp/"+chave, headers=agent )
sleep(1)
print("api -->", api.text)
api = api.text
api = api.split(".n.")
bolinha_notificacao = api[3].strip()
contato_cliente = api[4].strip()
caixa_msg = api[5].strip()
msg_cliente = api[6].strip()

def bot():

    try:
        #CAPTURAR A BOLINHA
        bolinha = driver.find_element(By.CLASS_NAME, bolinha_notificacao)
        bolinha = driver.find_elements(By.CLASS_NAME, bolinha_notificacao)
        clica_bolinha = bolinha[-1]
        acao_bolinha = webdriver.common.action_chains.ActionChains(driver)
        acao_bolinha.move_to_element_with_offset(clica_bolinha, 0, -20)
        acao_bolinha.click()
        acao_bolinha.perform()
        acao_bolinha.click()
        acao_bolinha.perform()
        sleep(1)

        #PEGAR TELEFONE
        telefone_cliente = driver.find_element(By.XPATH, contato_cliente)
        telefone_final = telefone_cliente.text
        print('telefone_final --> ', telefone_final)
        sleep(1)

        #PEGAR A MENSAGEM DO CLIENTE
        todas_as_msgs = driver.find_elements(By.CLASS_NAME, msg_cliente)
        todas_as_msgs_texto = [e.text for e in todas_as_msgs]
        msg = todas_as_msgs_texto[-1]
        print("mensagem --> ", msg)
        sleep(1)

        #RESPONDENDO CLIENTE
        campo_de_texto = driver.find_element(By.XPATH, caixa_msg)
        campo_de_texto.click()
        sleep(1)
        campo_de_texto.send_keys("Olá, eu também sou um bot em desenvolvimento", Keys.ENTER)

        #FECHAR CONTATO
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform

    except:
        print("Aguardando novas mensagens...")

while True:
    bot()

input("Aperte o ENTER para sair")
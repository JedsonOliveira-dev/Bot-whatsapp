from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

janela = webdriver.Chrome()
janela.get('https://web.whatsapp.com/')
pyautogui.sleep(35)

lista = ['Grupo 01', 'Grupo 02', 'Grupo 03', 'Grupo 04', 'Grupo 05']

janela.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys('Grupo 01')
pyautogui.sleep(1)
pyautogui.press('enter')

for grupo in range(10):

    janela.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys('>>>>>>>>>>>>>>>, essa é uma mensagem automatica <<<<<<<<<<<<<<.')
    pyautogui.press('enter')

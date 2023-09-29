import time
import difflib

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=r"C:\Users\Tavi\PycharmProjects\pythonProject2\chromedriver.exe")
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=service, options=options)
browser.get("https://automationintesting.online/")
# time.sleep(1)

hack_button_xpath = '//button[text()="Let me hack!"]'
hack_button = browser.find_element(By.XPATH, hack_button_xpath)
hack_button.click()
# time.sleep(1)

paragraf_hotel_xpath = '//div[@class="col-sm-10"]/p'
paragraf_hotel = browser.find_element(By.XPATH, paragraf_hotel_xpath)
print(paragraf_hotel.text)
text_asteptat = "Welcome t Shady Meadows, a delightful Bed & Breakfast nestled in the hills on Newingtonfordburyshire. A place so beautiful you will never want to leave. All our rooms have comfortable beds and we provide breakfast from the locally sourced supermarket. It is a delightful place."
# Crearea unui obiect Differ
differ = difflib.Differ()
# Calcularea diferențelor între text1 și text2

lista_text_ast = text_asteptat.split(" ")
list_web = paragraf_hotel.text.split(" ")
print(f"Lista astepta {lista_text_ast}\nLista web {list_web}")
differences = set(list_web) ^ set(lista_text_ast)
print("Differences:", list(differences))
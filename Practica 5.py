from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import time

#iniciamos web driver y entramos a la pagina que escogimos
driver = webdriver.Chrome(r"C:\Users\ianve\Documents\Universidad\7 Semestre\Calidad de Software\chromedriver.exe")

driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com/")

#creamos una cuenta
def crearCuenta():
    driver.find_element(By.LINK_TEXT, "Create an Account").click()
    driver.find_element(By.ID, "firstname").click()
    driver.find_element(By.CSS_SELECTOR, ".field-name-firstname").click()
    driver.find_element(By.ID, "firstname").send_keys("prueba")
    driver.find_element(By.ID, "lastname").click()
    driver.find_element(By.ID, "lastname").send_keys("1")
    driver.find_element(By.ID, "is_subscribed").click()
    driver.find_element(By.ID, "email_address").click()
    driver.find_element(By.ID, "email_address").send_keys("email.prueba@prueba.com")
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys("Prueba123")
    driver.find_element(By.ID, "password-confirmation").click()
    driver.find_element(By.ID, "password-confirmation").send_keys("Prueba123")
    driver.find_element(By.CSS_SELECTOR, ".submit > span").cld
    driver.find_element(By.CSS_SELECTOR, "#ui-id-11 > span").click()

def inicioSesion():
    driver.find_element(By.LINK_TEXT, "Sign In").click()
    driver.find_element(By.ID, "email").click()
    driver.find_element(By.ID, "email").send_keys("email.prueba@prueba.com")
    driver.find_element(By.CSS_SELECTOR, ".primary:nth-child(1) > #send2 ")
    driver.find_element(By.ID, "pass").send_keys("Prueba123")
    driver.find_element(By.ID, "pass").send_keys(Keys.ENTER)
    print("Se inicio sesion")
    time.sleep(3)

def agregarCarrito():
    print("entro")
    time.sleep(2)
    driver.find_element(By.ID, "ui-id-4").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Jackets").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(1) > .filter-options-title").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".allow .item:nth-child(1) > a").click()
    time.sleep(2)
    driver.find_element(By.ID, "mode-list").click()
    time.sleep(2)
    driver.find_element(By.ID, "option-label-size-143-item-167").click()
    time.sleep(2)
    driver.find_element(By.ID, "option-label-color-93-item-53").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) .actions-primary span").click()
    print("Se añadio")
    time.sleep(2)
    
def comprarCarrito():
    print('Comprar carrito')
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "logo").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "minicart-wrapper").click()
    time.sleep(2)
    driver.find_element(By.ID, "top-cart-btn-checkout").click()

    
    #driver.close()

#crearCuenta()

#inicioSesion()

agregarCarrito()
comprarCarrito()


print()
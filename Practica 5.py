from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

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
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="customer-email"]').send_keys("Tests@gmail.com")
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[1]/div/input').send_keys("test")
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[2]/div/input').send_keys("test")
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[3]/div/input').send_keys("test")
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/fieldset/div/div[1]/div/input').send_keys("test")
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[4]/div/input').send_keys("test")
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[7]/div/input').send_keys("12345")
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[9]/div/input').send_keys("test")
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[2]/div/div[3]/form/div[1]/table/tbody/tr[1]/td[1]/input').click()
    Select(driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[5]/div/select')).select_by_index(3)
    Select(driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[8]/div/select')).select_by_index(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[2]/div/div[3]/form/div[3]/div/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[3]/main/div[2]/div/div[2]/div[4]/ol/li[2]/div/div[3]/form/div[3]/div/button').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="checkout-payment-method-load"]/div/div/div[2]/div[2]/div[4]/div/button').click()

    
#driver.close()

#crearCuenta()

#inicioSesion()

agregarCarrito()
comprarCarrito()


print()
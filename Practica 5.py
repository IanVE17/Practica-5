import os
import time
from dotenv import load_dotenv
import randominfo # ? Used to generate random data: https://pypi.org/project/randominfo/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys 

class Person:
    def __init__(self) -> None:
        self.first_name = randominfo.get_first_name()
        self.last_name = randominfo.get_last_name()
        self.birthdate = randominfo.get_birthdate()

# Loading the environment variables from the .env file.
load_dotenv()

PERSON = Person()

# Getting the path to the webdriver from the .env file.
WEBDRIVER_PATH = os.getenv('WEBDRIVER_PATH')
EMAIL = randominfo.get_email(PERSON)
PASSWORD = randominfo.random_password()
ADDRESS = "3782 Mount Street"

# Checking if the word 'chrome' is in the WEBDRIVER_PATH variable. If it is, it will use the Chrome
# webdriver. If not, it will use the Edge webdriver.
driver = (webdriver.Chrome if 'chrome' in WEBDRIVER_PATH else webdriver.Edge)(WEBDRIVER_PATH)

driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com/")

# Creating an account.
def createAccount():
    os.system('cls')

    # Clicking on the "Create an Account" link.
    driver.find_element(By.LINK_TEXT, "Create an Account").click()

    # Finding the element for firstname field and sending the keys of PERSON.first_name to it.
    driver.find_element(By.ID, "firstname").send_keys(PERSON.first_name)

    # Finding the element for lastname and sending the keys of PERSON.last_name to it.
    driver.find_element(By.ID, "lastname").send_keys(PERSON.last_name)

    # Clicking on the checkbox that says "Sign Up for Newsletter".
    driver.find_element(By.ID, "is_subscribed").click()

    # Finding the element for email_address and sending the keys of EMAIL to it.
    driver.find_element(By.ID, "email_address").send_keys(EMAIL)

    # Finding the element for password and sending the keys of PASSWORD to it.
    driver.find_element(By.ID, "password").send_keys(PASSWORD)

    # Finding the element for password-confirmation and sending the keys of PASSWORD to it.
    driver.find_element(By.ID, "password-confirmation").send_keys(PASSWORD)

    driver.find_element(By.CSS_SELECTOR, ".submit > span").click()
    time.sleep(3)

# Logging in to the website.
def login():
    os.system('cls')
    driver.find_element(By.LINK_TEXT, "Sign In").click()
    driver.find_element(By.ID, "email").click()
    driver.find_element(By.ID, "email").send_keys(EMAIL)
    driver.find_element(By.CSS_SELECTOR, ".primary:nth-child(1) > #send2 ")
    driver.find_element(By.ID, "pass").send_keys(PASSWORD)
    driver.find_element(By.ID, "pass").send_keys(Keys.ENTER)
    print("Login Successfull")
    time.sleep(3)

# Adding a product to the shopping cart.
def addToShoppingCar():
    os.system('cls')
    print("Adding to shopping cart")
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
    print("Added!")
    time.sleep(2)

# Buying the product that was added to the shopping cart.
def buyShoppingCar():
    print('Buying')

    # Clicking on the logo, then clicking on the minicart-wrapper, then clicking on the
    # top-cart-btn-checkout.
    driver.find_element(By.CLASS_NAME, "logo").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "minicart-wrapper").click()
    time.sleep(2)
    driver.find_element(By.ID, "top-cart-btn-checkout").click()
    time.sleep(10)

    # Finding the element for company and sending the keys to it.
    driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[3]/div/input").send_keys(PERSON.last_name + " Company")

    # Finding the elements for street and sending the keys to it.
    for path in [
        "/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/fieldset/div/div[1]/div/input",
        "/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/fieldset/div/div[2]/div/input",
        "/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/fieldset/div/div[3]/div/input",
    ]:
        driver.find_element(By.XPATH, path).send_keys(ADDRESS)

    time.sleep(1)

    # Finding the element for city and sending the keys to it.
    driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[4]/div/input").send_keys(ADDRESS)

    # Finding the element for state and choosing the state.
    driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[5]/div/select").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[5]/div/select/option[2]").click()

    # Finding the element for zip and sending the keys to it.
    driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[7]/div/input").send_keys(ADDRESS)

    # Finding the element for phone_number and sending keys to it.
    driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[9]/div/input").send_keys(randominfo.get_phone_number())

    # Finding the element for shipping_method and choosing the shipping method.
    driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[2]/div/div[3]/form/div[1]/table/tbody/tr[1]/td[1]/input").click()

    # Finding the next button and clicking it.
    driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[2]/div/div[3]/form/div[3]/div/button").click()

    time.sleep(5)

    # Finding the element for final checkout and clicking it.
    driver.find_element(By.XPATH, "/html/body/div[3]/main/div[2]/div/div[2]/div[4]/ol/li[3]/div/form/fieldset/div[1]/div/div/div[2]/div[2]/div[4]/div/button").click()

    time.sleep(5)

    # Finding the element for going back to the shopping.
    driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/div[2]/div/div/a").click()

    time.sleep(5)

if __name__ == "__main__":
    createAccount()
    # login()
    addToShoppingCar()
    buyShoppingCar()
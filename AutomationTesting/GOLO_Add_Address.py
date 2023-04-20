import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from AutomationTesting.helpers import user_email, user_pass


class myGOLO(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/Juli Diva/Downloads/chromedriver_mac64/chromedriver")
        self.driver.maximize_window()


    def test_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.golo.com/")

        driver.find_element(By.XPATH, "//span[contains(text(),'Already a Customer? Login')]").click()

        email = driver.find_element(By.ID, "email")
        email.send_keys(user_email)

        password = driver.find_element(By.ID, "password")
        password.send_keys(user_pass)

        login = driver.find_element(By.XPATH, "//button[@id='btn-login']")
        login.click()
        time.sleep(3)

        my_profile = driver.find_element(By.XPATH, "//span[@class='nav-item__icon--user']")
        my_profile.click()
        time.sleep(3)

        addresses = driver.find_element(By.XPATH, "//li[@class='unstyled-li']//*[contains(text(),'Addresses')]")
        addresses.click()
        time.sleep(3)

        new_address = driver.find_element(By.XPATH, "//*[@class='add-address']")
        new_address.click()
        time.sleep(3)

        input_first_name = driver.find_element(By.XPATH, "//input[@id ='AddressFirstName_new']")
        input_first_name.send_keys("Fake")
        time.sleep(3)

        input_last_name = driver.find_element(By.XPATH, "//input[@id = 'AddressLastName_new']")
        input_last_name.send_keys("Faker")
        time.sleep(3)


        input_company = driver.find_element(By.XPATH, "//input[@id ='AddressCompany_new']")
        input_company.send_keys( "Golo")
        time.sleep(3)

        input_address = driver.find_element(By.XPATH, "//input[@id='AddressAddress1_new']")
        input_address.send_keys("123Fake street")
        time.sleep(3)

        input_city = driver.find_element(By.XPATH, "//input[@id= 'AddressCity_new']")
        input_city.send_keys("Newark")
        time.sleep(3)

        input_state = driver.find_element(By.XPATH, "//*[@id='AddressProvince_new']/option[12]")
        input_state.click()
        time.sleep(3)

        input_country = driver.find_element(By.XPATH, "//*[@id='AddressCountry_new']/option[1]")
        input_country.click()
        time.sleep(3)

        input_zipCode = driver.find_element(By.XPATH, "//input[@id='AddressZip_new']")
        input_zipCode.send_keys("19702")
        time.sleep(3)

        input_phonenumber = driver.find_element(By.XPATH, "//input[@id='AddressPhone_new']")
        input_phonenumber.send_keys("00000000000")
        time.sleep(3)

        add_address_btn = driver.find_element(By.XPATH, "//input[@value='Add Address']")
        add_address_btn.click()
        time.sleep(3)

        if "Your Addresses" in driver.title:
            raise Exception("Addresses page has the right Title!")

    def tearDown(self):
        self.driver.quit()


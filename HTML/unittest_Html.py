from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from faker import Faker
import time
import HtmlTestRunner
faker_class = Faker()


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/Juli Diva/Downloads/chromedriver_mac64/chromedriver")
        self.driver.maximize_window()

    def test_chrome_1120x550(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.golo.com/")

        driver.find_element(By.XPATH, "//span[contains(text(),'Already a Customer? Login')]").click()

        email = driver.find_element(By.ID, "email")
        email.send_keys(faker_class.email())

        password = driver.find_element(By.ID, "password")
        password.send_keys(faker_class.password())

        login = driver.find_element(By.XPATH, "//button[@id='btn-login']")
        login.click()
        time.sleep(3)

        if "Welcome to myGOLO!" in driver.title:
         raise Exception("Addresses page has the right Title!")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./Html_reports'))
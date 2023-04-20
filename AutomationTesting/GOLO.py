import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GOLO(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/Juli Diva/Downloads/chromedriver_mac64/chromedriver")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.golo.com/")
        wait = WebDriverWait(driver, 3)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(text(),"1-888-530-GOLO (4656)")]')))

        more_information_link = driver.find_element(By.ID, "navlink-item-more-information")
        more_information_link.click()

        faq_container = driver.find_element(By.XPATH, "//h2[contains(text(),'FAQs')]")
        faq_container.click()

        question1_expand = driver.find_element(By.XPATH, "//h3[contains(text(),'Why is GOLO unique?')]")
        question1_expand.click()
        # click again to collapse the question
        question1_expand.click()

        question2_expand = driver.find_element(By.XPATH, "//h3[contains(text(),'What is the GOLO For Life Plan?')]")
        question2_expand.click()
        # click again to collapse the question
        question2_expand.click()

        question3_expand = driver.find_element(By.XPATH, "//h3[contains(text(),'What is Release?')]")
        question3_expand.click()
        # click again to collapse the question
        question3_expand.click()

        question4_expand = driver.find_element(By.XPATH, "//h3[contains(text(),'Is Release Safe?')]")
        question4_expand.click()
        # click again to collapse the question
        question4_expand.click()

        question5_expand = driver.find_element(By.XPATH, "//h3[contains(text(),'How Long Do I Take Release?')]")
        question5_expand.click()
        # click again to collapse the question
        question5_expand.click()

        back_to_page = driver.find_element(By.XPATH, "//a[@href='/pages/more-information']"
                                                     "[contains(text(), ' Back to More Information')]")
        back_to_page.click()

    def tearDown(self):
            self.driver.quit()

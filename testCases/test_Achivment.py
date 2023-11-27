import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pageObjects.DashboardPage import Dashboard  # Import your DashboardPage class
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGenerator

class Test_Achivment:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    achievement_xpath = "/html/body/div[1]/div/div[1]/div/div/div/ul/li[3]/a/div/div[2]/span"  # XPath for the Achievement section
    right_element_xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]"  # XPath for the right side element
    See_Certification_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div[1]/div/img"
    Download_Certificate_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div[1]/div/div/img"
    logger = LogGenerator.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Achievement_Section_001(self, setup):
        self.logger.info("******************** test_Achievement_Section_001 Section Test start **************************")
        self.logger.info("******************** Verifying Achievement Section Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 20)
        time.sleep(2)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(2)
        self.logger.info("********************* Clicked on the Achievement option. *********************")
        achievement_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.achievement_xpath)))
        achievement_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, self.right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        # Verify if the page title is "Alpha Capital"
        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Achievement Page Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info("Achievement Section Test Passed: Page title is as expected.")
            assert True
        else:
            self.logger.error("Achievement Section Test Failed: Page title is not as expected.")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Achievement_Section.png")
            assert False

        self.driver.close()
        self.logger.info("****************** Achievement Section Test is completed ************************")

        self.logger.info(" ************************** test_Achievement_Section_001 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_See_Certificate_Achievement_Section_002(self, setup):
        self.logger.info("******************** Verifying Achievement Section Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 20)
        time.sleep(2)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(2)
        self.logger.info("********************* Clicked on the Achievement option. *********************")
        achievement_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.achievement_xpath)))
        achievement_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, self.right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("***************** Only see certificate (User Validation) *******************")
        wait = WebDriverWait(self.driver, 20)

        See_Certification_Xpath_N = wait.until(EC.element_to_be_clickable((By.XPATH, self.See_Certification_Xpath)))
        See_Certification_Xpath_N.click()

        time.sleep(2)

        self.driver.close()
        self.logger.info("****************** test_See_Certificate_Achievement_Section_002  Test is completed ************************")

        self.logger.info(" ************************** test_See_Certificate_Achievement_Section_002 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Achievement_Section_Download_Certificate_003(self, setup):
        self.logger.info("******************** Verifying Achievement Section Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 20)
        time.sleep(2)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(2)
        self.logger.info("********************* Clicked on the Achievement option. *********************")
        achievement_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.achievement_xpath)))
        achievement_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, self.right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("********************* Download Certificate to click on Download Button ************************")
        wait = WebDriverWait(self.driver, 20)

        Download_Certificate_Button_Xpath = wait.until(EC.element_to_be_clickable((By.XPATH, self.Download_Certificate_Xpath)))
        Download_Certificate_Button_Xpath.click()

        time.sleep(2)

        self.driver.close()
        self.logger.info("c****************** Achievement Section Test is completed ************************")

        self.logger.info(" ************************** test_Achievement_Section_Download_Certificate_003 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Achievement_Section_Search_Certificate_004(self, setup):
        self.logger.info("******************** Verifying Achievement Section Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 20)
        time.sleep(2)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(2)
        self.logger.info("********************* Clicked on the Achievement option. *********************")
        achievement_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.achievement_xpath)))
        achievement_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, self.right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("********************* Search Certificate to click on Download Button ************************")

        Search_textbox_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/header/div/div/div[2]/div/div/div/input")
        Search_textbox_Xpath.send_keys("Ruturaj")

        time.sleep(2)

        self.logger.info("********************* Download Certificate to click on Download Button ************************")
        wait = WebDriverWait(self.driver, 20)

        time.sleep(2)

        wait.until(EC.element_to_be_clickable((By.XPATH, self.Download_Certificate_Xpath)))

        self.driver.close()
        self.logger.info("c****************** Achievement Section Test is completed ************************")

        self.logger.info(" ************************** test_Achievement_Section_Search_Certificate_004 passed ************************")

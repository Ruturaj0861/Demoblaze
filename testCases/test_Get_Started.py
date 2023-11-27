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

class Test_GetStarted:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    achievement_xpath = "/html/body/div[1]/div/div[1]/div/div/div/ul/li[3]/a/div/div[2]/span"  # XPath for the Achievement section
    right_element_xpath = "/html/body/div[1]/div/div/1/div/main/div[2]"  # XPath for the right side element
    get_started_xpath = "/html/body/div[1]/div/div[1]/div/div/div/ul/li[4]/a/div"  # XPath for the Get Started section
    get_started_right_element_xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]"  # XPath for the Get Started right side element
    logger = LogGenerator.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_GetStarted_Section(self, setup):
        self.logger.info("******************** Verifying Get Started Section Test **************************")
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
        self.logger.info("********************* Clicked on the Get Started option. *********************")
        get_started_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.get_started_xpath)))
        get_started_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Get Started section
        self.logger.info("***************** Moved cursor to the right side for Get Started *******************")
        get_started_right_element = self.driver.find_element(By.XPATH, self.get_started_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(get_started_right_element)
        action.perform()

        time.sleep(2)

        # Verify if the page title is "Alpha Capital"
        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Get Started Page Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info("Get Started Section Test Passed: Page title is as expected.")
        else:
            self.logger.error("Get Started Section Test Failed: Page title is not as expected.")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_GetStarted_Section.png")
            assert False

        self.driver.close()
        self.logger.info("****************** Get Started Section Test is completed ************************")

        self.logger.info(" ************************** test_GetStarted_Section passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_GetStarted_Section_See_Video_MT5_Login_Overview_002(self, setup):
        self.logger.info("******************** test_GetStarted_Section_See_Video_MT5_Login_Overview_002 Test Started **************************")
        self.logger.info("******************** Verifying Get Started Section Test **************************")
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
        self.logger.info("********************* Clicked on the Get Started option. *********************")
        get_started_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.get_started_xpath)))
        get_started_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Get Started section
        self.logger.info("***************** Moved cursor to the right side for Get Started *******************")
        get_started_right_element = self.driver.find_element(By.XPATH, self.get_started_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(get_started_right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("******************* Click on play video Video MT5 Login Overview *************************")

        See_Video_MT5_Login_Overview_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[1]")
        See_Video_MT5_Login_Overview_Xpath.click()

        self.logger.info("******************* played video Video MT5 Login Overview *************************")

        self.logger.info("******************* Video Play Box visible or Not *************************")

        time.sleep(1)

        Video_play_Box = "/html/body/div[1]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, CHALLENGES_Xpath)))
            self.logger.info(f"'{Video_play_Box}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Video_play_Box}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "GetStarted_Section_See_Video_MT5_Login_Overview.png")

        self.logger.info("******************* Video Play Box visible *************************")

        self.driver.close()
        self.logger.info("****************** test_GetStarted_Section_See_Video_MT5_Login_Overview_002 Test is completed ************************")

        self.logger.info(" ************************** test_GetStarted_Section_See_Video_MT5_Login_Overview_002 passed ************************")
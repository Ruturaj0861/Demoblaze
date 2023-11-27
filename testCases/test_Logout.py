import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pageObjects.DashboardPage import Dashboard
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGenerator

class Test_Logout:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    logout_xpath = "/html/body/div[1]/div/div[1]/div/div/div/ul/li[12]/div/div[2]/span"
    logger = LogGenerator.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Logout_001(self, setup):
        self.logger.info("******************** Test test_Logout_001 **************************")
        self.logger.info("******************** Verifying Logout Test **************************")
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

        # Use JavaScript to scroll to the Logout element
        self.logger.info("***************** Scrolling to view the Logout element *******************")
        logout_element = self.driver.find_element(By.XPATH, self.logout_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", logout_element)

        time.sleep(2)

        # Click on the Logout element
        self.logger.info("***************** Clicking on the Logout option *******************")
        logout_element.click()

        # Verify if the page title is as expected (this can be the login page title)
        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Page Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info("Logout Test Passed: Page title is as expected.")
            assert True
        else:
            self.logger.error("Logout Test Failed: Page title is not as expected.")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Logout.png")
            assert False

        self.driver.close()
        self.logger.info("****************** Logout Test is completed ************************")

        self.logger.info(" ************************** test_Logout passed ************************")

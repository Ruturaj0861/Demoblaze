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

class Test_TradingPlatform:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    trading_platform_xpath = "/html/body/div[1]/div/div[1]/div/div/div/ul/li[10]/a/div/div[2]/span"
    logger = LogGenerator.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_TradingPlatform_001(self, setup):
        self.logger.info("******************** test_TradingPlatform_001 Test start **************************")
        self.logger.info("******************** Verifying Trading Platform Test **************************")
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

        # Use JavaScript to scroll to the Trading Platform element
        self.logger.info("***************** Scrolling to view the Trading Platform element *******************")
        trading_platform_element = self.driver.find_element(By.XPATH, self.trading_platform_xpath)  # Use the correct XPath expression
        self.driver.execute_script("arguments[0].scrollIntoView(true);", trading_platform_element)

        time.sleep(2)

        # Click on the Trading Platform element
        self.logger.info("***************** Clicking on the Trading Platform option *******************")
        trading_platform_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/header/div/div/div[2]")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        # Verify if the page title is as expected
        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Trading Platform Page Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info("Trading Platform Test Passed: Page title is as expected.")
            assert True
        else:
            self.logger.error("Trading Platform Test Failed: Page title is not as expected.")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_TradingPlatform.png")
            assert False

        self.driver.close()
        self.logger.info("****************** Trading Platform Test is completed ************************")

        self.logger.info(" ************************** test_TradingPlatform passed ************************")

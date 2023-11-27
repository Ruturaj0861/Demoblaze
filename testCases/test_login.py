import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGenerator
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_AC_L_1:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    invalid_password = Readconfig.getinvalid_password()
    logger = LogGenerator.loggen()  # Configure logging in the test class

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle_001(self, setup):
        self.logger.info("************************** test_homePageTitle_001 *******************************")
        self.logger.info("******************** Verifying Home Page Title ***********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Alpha Capital":
            assert True
            self.driver.close()
            self.logger.info("************** Test Home Page Title is Passed ********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************** Test Home Page Title is Failed ********************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_002(self, setup):
        self.logger.info("******************** test_login_002 Test start **************************")
        self.logger.info("******************** Verifying Login Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Alpha Capital":
            assert True
            self.driver.close()
            self.logger.info("****************** Login Test is Passed ************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("****************** Login Test is Failed ************************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_invalid_credentials_003(self, setup):
        self.logger.info("******************** test_login_invalid_credentials_003 test start **************************")
        self.logger.info("******************** Verifying Login Test with Invalid Credentials **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.invalid_password)
        self.lp.clickLogin()

        try:
            # Check if an error message element is displayed
            error_message = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[1]/div")

            if error_message.is_displayed():
                self.logger.info("*************** Error message is displayed. ***********************")
                action = ActionChains(self.driver)
                action.click()  # Click anywhere on the page to make the error message disappear
                action.perform()
            else:
                self.logger.error("***************** Error message is not displayed. ********************")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_login_failed.png")
                assert False  # If the error message is not displayed, fail the test

        except Exception as e:
            self.logger.error(f"Exception: {str(e)}")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_failed.png")
            assert False  # If an exception occurs, fail the test

        self.logger.info("****************** test_login_invalid_credentials_002 completed ************************")

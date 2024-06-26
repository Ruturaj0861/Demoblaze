import pytest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from pageObjects.LoginPage import Login
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGenerator
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_002:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    invalid_password = Readconfig.getinvalid_password()
    logger = LogGenerator.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_with_valid_credentials(self, setup):
        self.logger.info("******************** test_login_with_valid_credentials test start **************************")
        self.logger.info("******************** Verifying Login Test with Valid Credentials **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.clickLoginMenu()
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()  # Corrected method name

        try:
            WebDriverWait(self.driver, 10).until(
                EC.title_is("STORE")
            )
            act_title = self.driver.title
            if act_title == "STORE":
                assert True
                self.logger.info("****************** Login Test with Valid Credentials is Passed ************************")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_login_valid_credentials.png")
                self.logger.error("****************** Login Test with Valid Credentials is Failed ************************")
                assert False
        finally:
            self.driver.quit()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_with_invalid_credentials(self, setup):
        self.logger.info("******************** test_login_with_invalid_credentials test start **************************")
        self.logger.info("******************** Verifying Login Test with Invalid Credentials **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.clickLoginMenu()
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.invalid_password)
        self.lp.clickLoginButton()  # Corrected method name

        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()

            act_title = self.driver.title
            if act_title == "STORE":  # Adjusted expected title as per your description
                assert True
                self.logger.info("****************** Login Test with Invalid Credentials is Passed ************************")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_login_with_invalid_credentials_failed.png")
                self.logger.error("****************** Login Test with Invalid Credentials is Failed ************************")
                assert False

        except NoAlertPresentException:
            self.logger.error("No alert present when expected during login with invalid credentials")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_with_invalid_credentials_failed.png")
            assert False

        except Exception as e:
            self.logger.error(f"Exception: {str(e)}")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_with_invalid_credentials_failed.png")
            assert False

        finally:
            self.driver.close()
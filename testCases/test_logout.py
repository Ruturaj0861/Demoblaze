import pytest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from pageObjects.LoginPage import Login
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGenerator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_003:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    invalid_password = Readconfig.getinvalid_password()
    logger = LogGenerator.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_logout(self, setup):
        self.logger.info(
            "******************** test_logout test start **************************")
        self.logger.info("******************** Verifying Login Test with Valid Credentials **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.clickLoginMenu()
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.title_is("STORE")
            )
            act_title = self.driver.title
            if act_title == "STORE":
                self.logger.info(
                    "****************** Login Test with Valid Credentials is Passed ************************")
                self.logger.info("******************** Verifying Logout Process **************************")
                logout_button = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "/html/body/nav/div[1]/ul/li[6]/a"))
                )
                logout_button.click()

                WebDriverWait(self.driver, 10).until(
                    EC.title_is("STORE")
                )
                assert self.driver.title == "STORE"
                self.logger.info("****************** Logout Test is Passed ************************")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_login_valid_credentials.png")
                self.logger.error(
                    "****************** Login Test with Valid Credentials is Failed ************************")
                assert False
        except Exception as e:
            self.logger.error(f"Exception: {str(e)}")
            self.driver.save_screenshot(".\\Screenshots\\logout_error.png")
            assert False, f"Exception occurred: {str(e)}"
        finally:
            self.driver.quit()

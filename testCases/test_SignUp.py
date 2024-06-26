import pytest
from selenium import webdriver
from pageObjects.Sign_up import Sign_up
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGenerator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Test_1:
    baseURL = Readconfig.getApplicationURL()
    logger = LogGenerator.loggen()

    baseURL = Readconfig.getApplicationURL()
    existing_username = Readconfig.getuseremail()  # Correct method to get the existing username
    existing_password = Readconfig.getpassword()  # Correct method to get the existing password
    logger = LogGenerator.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_signUpNewUser_001(self, setup):
        self.logger.info("************************** test_signUpNewUser_001 *******************************")
        self.logger.info("******************** Verifying Sign Up with New User ***********************")
        self.driver = setup
        self.driver.get(self.baseURL)

        sign_up = Sign_up(self.driver)

        timestamp = str(int(time.time()))
        unique_username = "user" + timestamp
        unique_password = "pass" + timestamp

        try:
            self.logger.info("Waiting for Sign Up button to be clickable")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(sign_up.button_sign_up_xpath)
            ).click()
            self.logger.info("Clicked on Sign Up button")

            self.logger.info("Waiting for Username textbox to be visible")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(sign_up.textbox_Username_xpath)
            ).send_keys(unique_username)
            self.logger.info(f"Entered username: {unique_username}")

            self.logger.info("Waiting for Password textbox to be visible")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(sign_up.textbox_password_xpath)
            ).send_keys(unique_password)
            self.logger.info(f"Entered password")

            self.logger.info("Waiting for Register button to be clickable")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(sign_up.button_Sign_Register_xpath)
            ).click()
            self.logger.info("Clicked on Register button")

            try:
                self.logger.info("Checking for alert presence")
                WebDriverWait(self.driver, 5).until(EC.alert_is_present())
                alert = self.driver.switch_to.alert
                alert_text = alert.text
                self.logger.info(f"Alert text: {alert_text}")
                alert.accept()
                self.logger.info("Accepted the alert")
            except Exception as e:
                self.logger.info("No alert present")

            self.driver.save_screenshot(".\\Screenshots\\" + "after_alert.png")

            self.logger.info("Validating the page title")
            assert self.driver.title == "STORE", f"Expected page title to be 'STORE' but got '{self.driver.title}'"
            self.logger.info("Page title validated successfully")

            self.logger.info("************** Test Sign Up with New User is Passed ********************")

        except Exception as e:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_signUpNewUser.png")
            self.logger.error("************** Test Sign Up with New User is Failed ********************")
            self.logger.error(f"Exception: {e}")
            assert False
        finally:
            self.driver.quit()



    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle_001(self, setup):
        self.logger.info("************************** test_homePageTitle_001 *******************************")
        self.logger.info("******************** Verifying Home Page Title ***********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "STORE":
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
    def test_signUpWithExistingUser_002(self, setup):
        self.logger.info("************************** test_signUpWithExistingUser_002 *******************************")
        self.logger.info("******************** Verifying Sign Up with Existing User ***********************")
        self.driver = setup
        self.driver.get(self.baseURL)

        sign_up = Sign_up(self.driver)

        try:
            self.logger.info("Waiting for Sign Up button to be clickable")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(sign_up.button_sign_up_xpath)
            ).click()
            self.logger.info("Clicked on Sign Up button")

            self.logger.info("Waiting for Username textbox to be visible")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(sign_up.textbox_Username_xpath)
            ).send_keys(self.existing_username)
            self.logger.info(f"Entered username: {self.existing_username}")

            self.logger.info("Waiting for Password textbox to be visible")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(sign_up.textbox_password_xpath)
            ).send_keys(self.existing_password)
            self.logger.info(f"Entered password")

            self.logger.info("Waiting for Register button to be clickable")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(sign_up.button_Sign_Register_xpath)
            ).click()
            self.logger.info("Clicked on Register button")

            try:
                self.logger.info("Checking for alert presence")
                WebDriverWait(self.driver, 5).until(EC.alert_is_present())
                alert = self.driver.switch_to.alert
                alert_text = alert.text
                self.logger.info(f"Alert text: {alert_text}")
                alert.accept()
                self.logger.info("Accepted the alert")
            except Exception as e:
                self.logger.info("No alert present")

            self.driver.save_screenshot(".\\Screenshots\\" + "after_alert.png")

            self.logger.info("Validating the page title")
            assert self.driver.title == "STORE", f"Expected page title to be 'STORE' but got '{self.driver.title}'"
            self.logger.info("Page title validated successfully")

            self.logger.info("************** Test Sign Up with Existing User is Passed ********************")

        except Exception as e:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_signUpWithExistingUser.png")
            self.logger.error("************** Test Sign Up with Existing User is Failed ********************")
            self.logger.error(f"Exception: {e}")
            assert False
        finally:
            self.driver.quit()


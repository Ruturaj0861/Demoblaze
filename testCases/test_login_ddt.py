import pytest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGenerator
from utilities.excel_helper import ExcelHelper


class TestLoginDDT:
    baseURL = Readconfig.getApplicationURL()
    logger = LogGenerator.loggen()

    @pytest.fixture()
    def setup(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    @pytest.mark.parametrize("username, password, expected_result",
                             ExcelHelper("R:/Demoblaze_E-commerce/TestData/testdata.xlsx").read_data("Sheet1"))
    def test_login_with_data(self, setup, username, password, expected_result):
        self.logger.info("******************** test_login_with_data test start **************************")
        self.logger.info(f"Username: {username}, Password: {password}, Expected Result: {expected_result}")

        driver = setup
        driver.get(self.baseURL)
        lp = Login(driver)
        lp.clickLoginMenu()
        lp.setUsername(username)
        lp.setPassword(password)
        lp.clickLoginButton()

        try:
            try:
                alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
                alert.accept()
                self.logger.info("Alert accepted for invalid login attempt.")
                if expected_result == "Fail":
                    self.logger.info("****************** Login Test Failed as Expected ************************")
                else:
                    self.logger.error("Expected success but login failed with alert.")
                    driver.save_screenshot(".\\Screenshots\\" + f"test_login_with_data_{username}_{password}.png")
            except TimeoutException:
                if expected_result == "Pass":
                    WebDriverWait(driver, 10).until(EC.title_is("STORE"))
                    act_title = driver.title
                    if act_title == "STORE":
                        self.logger.info("****************** Login Test Passed ************************")
                    else:
                        self.logger.error("Login was not successful. Title mismatch!")
                        driver.save_screenshot(".\\Screenshots\\" + f"test_login_with_data_{username}_{password}.png")
                else:
                    self.logger.error("Expected failure but no alert was found.")
                    driver.save_screenshot(".\\Screenshots\\" + f"test_login_with_data_{username}_{password}.png")

        except NoSuchElementException as e:
            self.logger.error(f"Element not found: {str(e)}")
            driver.save_screenshot(".\\Screenshots\\" + f"test_login_with_data_{username}_{password}.png")

        except Exception as ex:
            self.logger.error(f"Exception: {str(ex)}")
            driver.save_screenshot(".\\Screenshots\\" + f"test_login_with_data_{username}_{password}.png")

        finally:
            driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, InvalidSelectorException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from utilities import XLutils
from pageObjects.LoginPage import Login
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGenerator

class Test_Login_DDT:
    Url = Readconfig.getApplicationURL()
    log = LogGenerator.loggen()
    path = "C:\\Users\\rutur\\PycharmProjects\\ALPHA_CAPITAL\\TestData\\LoginData.xlsx"

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_ddt_001(self, setup):
        self.logger.info("******************** test_login_ddt_001 Test Start **************************")
        self.driver = setup
        self.log.info("test_login_ddt is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this URL --> " + self.Url)
        self.lp = Login(self.driver)
        self.rows = XLutils.getrowCount(self.path, 'Sheet1')
        self.log.info("Number of rows are ---> " + str(self.rows))
        login_statuses = []

        for r in range(2, self.rows + 1):
            self.username = XLutils.readData(self.path, 'Sheet1', r, 2)
            self.password = XLutils.readData(self.path, 'Sheet1', r, 3)
            self.Exp_Status = XLutils.readData(self.path, 'Sheet1', r, 4)

            self.lp.setEmail(self.username)
            self.log.info("Entering username --> " + self.username)
            self.lp.setPassword(self.password)
            self.log.info("Entering password --> " + self.password)

            try:
                login_button = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/form/div[4]/button'))
                )
                self.driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
                login_button.click()
                self.log.info("Click on login button")

                if self.lp.Login_status() == True:
                    if self.Exp_Status == "Pass":
                        self.driver.save_screenshot(
                            "C:\\Users\\rutur\\PycharmProjects\\ALPHA_CAPITAL\\Screenshots" + self.username + self.password + "test_login_ddt-pass.png")
                        self.lp.clickLogout()
                        self.log.info("Click on logout button")
                        login_statuses.append("Pass")
                        XLutils.writeData(self.path, 'Sheet1', r, 5, "Pass")
                    else:
                        self.driver.save_screenshot(
                            "C:\\Users\\rutur\\PycharmProjects\\ALPHA_CAPITAL\\Screenshots" + self.username + self.password + "test_login_ddt-fail.png")
                        self.lp.clickLogout()
                        self.log.info("Click on logout button")
                        login_statuses.append("Fail")
                        XLutils.writeData(self.path, 'Sheet1', r, 5, "Fail")
                else:
                    if self.Exp_Status == "Fail":
                        login_statuses.append("Pass")
                        XLutils.writeData(self.path, 'Sheet1', r, 5, "Pass")
                        self.driver.save_screenshot(
                            "C:\\Users\\rutur\\PycharmProjects\\ALPHA_CAPITAL\\Screenshots" + self.username + self.password + "test_login_ddt_fail.png")
                    else:
                        login_statuses.append("Fail")
                        XLutils.writeData(self.path, 'Sheet1', r, 5, "Fail")
                        self.driver.save_screenshot(
                            "C:\\Users\\rutur\\PycharmProjects\\ALPHA_CAPITAL\\Screenshots" + self.username + self.password + "test_login_ddt_006-fail.png")
            except TimeoutException:
                self.log.error("Timeout waiting for the login button to be clickable")
            except ElementClickInterceptedException:
                self.log.error("ElementClickInterceptedException: Element click intercepted")
                # Handle the ElementClickInterceptedException here, e.g., scroll the page or take appropriate action

            # Additional code for interactions
            # Create an ActionChains object and move the cursor to the right
            action = ActionChains(self.driver)
            action.move_by_offset(10, 0)  # Adjust the offset as needed
            action.perform()

            try:
                # Find the widget element and scroll into view
                widget = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")))
                self.driver.execute_script("arguments[0].scrollIntoView();", widget)

                # Find the logout button and click it
                logout_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/ul/li[12]/div/div[2]/span")))
                logout_button.click()
            except TimeoutException:
                self.log.error("Timeout waiting for the widget or the logout button to be clickable")

        print(login_statuses)

        if "Fail" not in login_statuses:
            self.log.info("test_login_ddt is Passed")
            assert True
        else:
            self.log.info("test_login_ddt is Failed")
            assert False

        self.driver.close()
        self.log.info("test_login_ddt is Completed")

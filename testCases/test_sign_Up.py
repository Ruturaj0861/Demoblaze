import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains  # Import ActionChains
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGenerator
from selenium.webdriver.common.keys import Keys
import time

class Test_SignUp:
    baseURL = Readconfig.getApplicationURL()
    sign_up_xpath = "/html/body/div[1]/div/div[1]/div/div[1]/div/div[1]/div/div[5]/div/span/div/h6"
    sign_up_title = "Alpha Capital"
    logger = LogGenerator.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_signup_page_title_001(self, setup):
        self.logger.info("******************** Verifying Sign-Up Page Title Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)

        sign_up_button = self.driver.find_element(By.XPATH, self.sign_up_xpath)

        action = ActionChains(self.driver)
        action.move_to_element(sign_up_button).click().perform()
        time.sleep(2)

        if self.sign_up_title in self.driver.title:
            assert True
            self.logger.info("****************** Sign-Up Page Title Test is Passed ************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_signup_page_title.png")
            self.driver.close()
            self.logger.error("****************** Sign-Up Page Title Test is Failed ************************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_signup_and_scroll_002(self, setup):
        self.logger.info("******************** Verifying Sign-Up and Scroll Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)

        # Click the sign-up button using the given XPath
        sign_up_button = self.driver.find_element(By.XPATH, self.sign_up_xpath)

        # Scroll to the bottom of the page
        while True:
            # Perform a series of scroll actions, scrolling down
            self.driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
            time.sleep(2)

            # Check if you've reached the bottom of the page
            if self.driver.execute_script(
                    "return (window.innerHeight + window.scrollY) >= document.body.scrollHeight;"):
                self.logger.info("Reached the bottom of the page.")
                break  # If we've reached the bottom, break the loop

        action = ActionChains(self.driver)
        action.move_to_element(sign_up_button).click().perform()
        self.logger.info("Sign-Up button clicked.")

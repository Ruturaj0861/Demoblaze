import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from pageObjects.DashboardPage import Dashboard
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGenerator
from selenium.webdriver.common.keys import Keys

class Test_PaymentFundingEvaluation:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    payment_funding_evaluation_Xpath = """//span[contains(@class, 'MuiTypography-root') and contains(text(), 'Funding Evaluation')]"""
    payment_funding_evaluation_right_element_xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/div[6]/span"  # XPath for the right side element
    payment_history_xpath = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'Payment History')]"
    payment_history_right_element_xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]"  # XPath for the right side element
    faq_xpath = "//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-body1') and contains(@class, 'MuiListItemText-primary') and contains(@class, 'css-yb@lig') and text()='FAQ']"
    logger = LogGenerator.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_PaymentFundingEvaluation_Section_001(self, setup):
        self.logger.info("******************** test_PaymentFundingEvaluation_Section_001 Test case start **************************")
        self.logger.info("******************** Verifying Payment Funding Evaluation Section Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 20)  # Increased timeout to 20 seconds
        time.sleep(5)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(5)
        self.logger.info("********************* Clicked on the Payment Funding Evaluation option. *********************")

        try:
            # Wait for the Payment Funding Evaluation element to be clickable and visible
            payment_funding_evaluation_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.payment_funding_evaluation_Xpath)))
            payment_funding_evaluation_option.click()
        except Exception as e:
            self.logger.error("Error while clicking on Payment Funding Evaluation option: " + str(e))
            self.driver.save_screenshot(".\\Screenshots\\" + "payment_funding_evaluation_error.png")
            assert False

        time.sleep(10)

        # Add your code to move the cursor to the right side for the Payment Funding Evaluation section
        self.logger.info("***************** Moved cursor to the right side for Payment Funding Evaluation *******************")
        payment_funding_evaluation_right_element = self.driver.find_element(By.XPATH, self.payment_funding_evaluation_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(payment_funding_evaluation_right_element)
        action.perform()

        time.sleep(10)

        # Verify if the page title is "Alpha Capital"
        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Payment Funding Evaluation Page Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info("Payment Funding Evaluation Section Test Passed: Page title is as expected.")
        else:
            self.logger.error("Payment Funding Evaluation Section Test Failed: Page title is not as expected.")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_PaymentFundingEvaluation_Section.png")
            assert False

        self.driver.close()
        self.logger.info("****************** Payment Funding Evaluation Section Test is completed ************************")

        self.logger.info("************************** test_PaymentFundingEvaluation_Section_001 passed ************************")

        @pytest.mark.sanity
        @pytest.mark.regression
        def test_PaymentFundingEvaluation_Section_Alpha_Pro_002(self, setup):
            self.logger.info(
                "******************** test_PaymentFundingEvaluation_Section_Alpha_Pro_002 test case start **************************")
            self.logger.info(
                "******************** Verifying Payment Funding Evaluation Section Test **************************")
            self.driver = setup
            self.driver.get(self.baseURL)
            self.lp = Dashboard(self.driver)
            self.lp.setEmail(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            wait = WebDriverWait(self.driver, 20)  # Increased timeout to 20 seconds
            time.sleep(5)

            self.logger.info("***************** Moved cursor to the left side *******************")
            left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
            action = ActionChains(self.driver)
            action.move_to_element(left_element)
            action.perform()

            time.sleep(5)
            self.logger.info(
                "********************* Clicked on the Payment Funding Evaluation option. *********************")

            try:
                # Wait for the Payment Funding Evaluation element to be clickable and visible
                payment_funding_evaluation_option = wait.until(
                    EC.element_to_be_clickable((By.XPATH, self.payment_funding_evaluation_Xpath)))
                payment_funding_evaluation_option.click()
            except Exception as e:
                self.logger.error("Error while clicking on Payment Funding Evaluation option: " + str(e))
                self.driver.save_screenshot(".\\Screenshots\\" + "payment_funding_evaluation_error.png")
                assert False

            time.sleep(10)

            # Add your code to move the cursor to the right side for the Payment Funding Evaluation section
            self.logger.info(
                "***************** Moved cursor to the right side for Payment Funding Evaluation *******************")
            payment_funding_evaluation_right_element = self.driver.find_element(By.XPATH,
                                                                                self.payment_funding_evaluation_right_element_xpath)
            action = ActionChains(self.driver)
            action.move_to_element(payment_funding_evaluation_right_element)
            action.perform()

            time.sleep(2)

            time.sleep(1)
            self.logger.info("********************* Clicked on the Alpha button *********************")
            alpha_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div/div/div/button[1]")))
            alpha_button.click()

            time.sleep(1)
            self.logger.info("********************* Scrolling down to make an element visible *********************")
            alpha_pro_10K_button = self.driver.find_element(By.XPATH,
                                                            "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/button")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", alpha_pro_10K_button)
            time.sleep(1)

            time.sleep(1)
            self.logger.info("********************* Clicked on the alpha_pro_10K button *********************")
            alpha_pro_10K_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                          "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/button")))
            alpha_pro_10K_button.click()

            time.sleep(1)
            self.logger.info("********************* Clear and Send Keys to First_Name *********************")
            first_name_input = self.driver.find_element(By.XPATH,
                                                        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div/input")
            first_name_input.clear()
            first_name_input.send_keys("Testuser")

            time.sleep(1)
            self.logger.info("********************* Clear and Send Keys to Last_Name *********************")
            last_name = self.driver.find_element(By.XPATH,
                                                 "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/input")
            last_name.clear()
            last_name.send_keys("1234")

            time.sleep(1)
            self.logger.info("********************* Clear and Send Keys to Email_Id *********************")
            email_input = self.driver.find_element(By.XPATH,
                                                   "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/input")
            email_input.clear()
            email_input.send_keys("kobox34324@about27.com")

            time.sleep(1)
            self.logger.info(
                "********************* Scrolling down to make an element visible country dropdown Scroll *********************")
            country_dropdown_Scroll = self.driver.find_element(By.XPATH,
                                                               "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/div/div/input")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", country_dropdown_Scroll)

            time.sleep(1)
            self.logger.info("********************* Clicked on the Country dropdown *********************")
            country_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                      "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/div/div/input")))
            country_dropdown.click()

            time.sleep(1)
            self.logger.info(
                "********************* Selected 'India' from the dropdown and pressed ENTER *********************")
            country_dropdown.send_keys(Keys.RETURN)

            time.sleep(1)
            self.logger.info("********************* Clicked on the coin base checkbox *********************")
            coin_base_checkbox = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[1]/div/div[4]/div[2]/label")))
            coin_base_checkbox.click()

            time.sleep(1)
            self.logger.info("********************* check out the check out button *********************")
            check_out_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[1]/div/div[4]/div[1]")))
            check_out_button.click()

            time.sleep(1)
            self.logger.info("********************* check Funding Evaluation *********************")

            dropdown_element = self.driver.find_element(By.XPATH,
                                                        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[1]/div/div[5]/div[1]/div[2]/div")
            dropdown_element.click()

            option_index_2 = self.driver.find_element(By.XPATH, "(//li[contains(@class, 'MuiMenuItem-root')])[2]")
            option_index_2.click()

            time.sleep(1)
            self.logger.info("********************* check on the Account Balance *********************")

            dropdown_element = self.driver.find_element(By.XPATH,
                                                        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[1]/div/div[5]/div[2]/div[2]/div")
            dropdown_element.click()

            option_index_4 = self.driver.find_element(By.XPATH, "//li[@data-value='200000']")
            option_index_4.click()

            time.sleep(1)
            self.logger.info("********************* Selected 'Expert Advisor' checkbox *********************")
            expert_advisor_checkbox = self.driver.find_element(By.XPATH,
                                                               "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[1]/div/div[6]/div/span")
            expert_advisor_checkbox.click()

            self.logger.info(
                "************* All actions completed test_PaymentFundingEvaluation_Section_Alpha_Pro_002 passed *********************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_PaymentHistory_Section_003(self, setup):
        self.logger.info("******************** Verifying Payment History Section Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 20)  # Increased timeout to 20 seconds
        time.sleep(2)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(2)
        self.logger.info("********************* Clicked on the Payment History option. *********************")

        try:
            # Wait for the Payment History element to be clickable and visible
            payment_history_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.payment_history_xpath)))
            payment_history_option.click()
        except Exception as e:
            self.logger.error("Error while clicking on Payment History option: " + str(e))
            self.driver.save_screenshot(".\\Screenshots\\" + "payment_history_error.png")
            assert False

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Payment History section
        self.logger.info("***************** Moved cursor to the right side for Payment History *******************")
        payment_history_right_element = self.driver.find_element(By.XPATH, self.payment_history_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(payment_history_right_element)
        action.perform()

        time.sleep(2)

        # Verify if the page title is "Alpha Capital"
        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Payment History Page Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info("Payment History Section Test Passed: Page title is as expected.")
        else:
            self.logger.error("Payment History Section Test Failed: Page title is not as expected.")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_PaymentHistory_Section.png")
            assert False

        self.driver.close()
        self.logger.info("****************** test_PaymentHistory_Section_003 Test is completed ************************")

        self.logger.info("************************** test_PaymentHistory_Section_003 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_FAQ_Section_004(self, setup):
        self.logger.info("******************** Verifying FAQ Section Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 20)
        time.sleep(10)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(10)
        self.logger.info("********************* Clicked on the FAQ option. *********************")

        faq_xpath = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'FAQ')]"
        try:
            faq_option = wait.until(EC.element_to_be_clickable((By.XPATH, faq_xpath)))
            faq_option.click()
        except Exception as e:
            self.logger.error("Error while clicking on FAQ option: " + str(e))
            self.driver.save_screenshot(".\\Screenshots\\" + "faq_error.png")
            assert False

        # Switch to the new tab (assuming FAQ opens in a new tab)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        time.sleep(10)

        # Add your code to verify the FAQ page title on the new tab
        expected_title = "Alpha Capital Help Center"
        actual_title = self.driver.title
        self.logger.info(f"Actual FAQ Page Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info("FAQ Section Test Passed: Page title is as expected.")
        else:
            self.logger.error("FAQ Section Test Failed: Page title is not as expected.")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_FAQ_Section.png")
            assert False

        # Close the new tab
        self.driver.close()

        # Switch back to the main tab
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.logger.info("****************** FAQ Section Test is completed ************************")

        self.logger.info("************************** test_FAQ_Section_004 passed ************************")
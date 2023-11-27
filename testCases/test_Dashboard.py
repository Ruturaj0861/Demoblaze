import pytest
import selenium.webdriver.safari.service
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select
import time

from pageObjects.DashboardPage import Dashboard
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGenerator

class Test_Dashboard:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    logger = LogGenerator.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Dashboard_Title_001(self, setup):
        self.logger.info("******************** Verifying Login Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 20)
        time.sleep(5)
        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(1)
        self.logger.info("********************* Clicked on the Dashboard option. *********************")
        dashboard_option = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/ul/li[1]/a/div")))
        dashboard_option.click()

        time.sleep(1)
        self.logger.info("******************* Moved cursor to the right side *************************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/header/div/div/div[2]")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(1)
        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Dashboard Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info(" ************************* Dashboard Title is as expected. ******************************")
            assert True
            self.driver.close()
            self.logger.info("****************** Login and Dashboard Test is Passed ************************")
        else:
            self.logger.error("Dashboard Title is not as expected. Taking a screenshot.")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("****************** Login and Dashboard Test is Failed ************************")
            assert False

        self.logger.info(" ************************** test_Dashboard_Title_1 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Filter_002(self, setup):
        self.logger.info("******************** Verifying Login Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 20)

        time.sleep(1)
        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(1)
        self.logger.info("********************* Clicked on the Dashboard option. *********************")
        dashboard_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/ul/li[1]/a/div")))
        dashboard_option.click()

        time.sleep(1)
        self.logger.info("******************* Moved cursor to the right side *************************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/header/div/div/div[2]")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(1)
        self.logger.info("********************* Clicked on the Filter button 1st time *********************")

        filter_button = self.driver.find_element(By.XPATH,
                                                 "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/div/button")
        filter_button.click()

        self.logger.info("********************* Select Active Filter *********************")
        active_element = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[1]")
        action = ActionChains(self.driver)
        action.move_to_element(active_element)
        action.click().perform()
        Active_Blue_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/label/span[2]/span"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Active_Blue_Xpath)))
            self.logger.info(f"'{Active_Blue_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Active_Blue_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Active Filter.png")

        self.logger.info("********************* Active Filter Selected *********************")

        self.logger.info("********************* Clicked on the Filter button 2nd time *********************")

        filter_button = self.driver.find_element(By.XPATH,
                                                 "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/div/button")
        filter_button.click()

        self.logger.info("********************* Select Inactive Filter *********************")
        Inactive_element = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[2]")
        action = ActionChains(self.driver)
        action.move_to_element(Inactive_element)
        action.click().perform()
        Inactive_Red_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/label/span[2]/span"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Inactive_Red_Xpath)))
            self.logger.info(f"'{Inactive_Red_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Inactive_Red_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Inactive Filter.png")

        self.logger.info("********************* All Filter Selected *********************")

        self.logger.info("********************* Clicked on the Filter button 3rd time *********************")

        filter_button = self.driver.find_element(By.XPATH,
                                                 "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/div/button")
        filter_button.click()

        self.logger.info("********************* Select All Filter *********************")
        All_element = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[3]")
        action = ActionChains(self.driver)
        action.move_to_element(All_element)
        action.click().perform()

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Active_Blue_Xpath)))
            self.logger.info(f"'{Active_Blue_Xpath}' is visible for All filter.")
        except Exception as e:
            self.logger.error(f"'{Active_Blue_Xpath}' is not visible for All Filter. Screenshot added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Active_Blue_Filter_for_All_Filter.png")
            self.logger.info("Screenshot saved as 'Active_Blue_Filter_for_All_Filter.png'.")

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Inactive_Red_Xpath)))
            self.logger.info(f"'{Inactive_Red_Xpath}' is visible for ALl filter.")
        except Exception as e:
            self.logger.error(f"'{Inactive_Red_Xpath}' is not visible for All filter. Screenshot added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Inactive_For_All_Filter.png")
            self.logger.info("Screenshot saved as 'Inactive_For_All_Filter.png'.")

        self.logger.info("********************* All Filter Selected *********************")

        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Filter Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info(
                " ************************* Filter Title is as expected. ******************************")
            assert True
            self.driver.close()
            self.logger.info("****************** Filter Test is Passed ************************")
        else:
            self.logger.error("Add Account Title is not as expected. Taking a screenshot.")
            self.driver.save_screenshot(".\\Screenshots\\" + "Filter.png")
            self.driver.close()
            self.logger.error("****************** Filter Test is Failed ************************")
            assert False

        self.logger.info("************* All actions completed test_Filter_002 passed *********************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Add_Account_003(self, setup):
        self.logger.info("******************** Verifying Add Account Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)

        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 20)

        time.sleep(1)
        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(1)
        self.logger.info("********************* Clicked on the Dashboard option. *********************")
        dashboard_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/ul/li[1]/a/div")))
        dashboard_option.click()

        time.sleep(1)
        self.logger.info("******************* Moved cursor to the right side *************************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/header/div/div/div[2]")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(1)
        self.logger.info("********************* Clicked on the Add_Account button *********************")
        add_account_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/button")))
        add_account_button.click()

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

        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Add Account Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info(
                " ************************* Add Account Title is as expected. ******************************")
            assert True
            self.driver.close()
            self.logger.info("****************** Add Account Test is Passed ************************")
        else:
            self.logger.error("Add Account Title is not as expected. Taking a screenshot.")
            self.driver.save_screenshot(".\\Screenshots\\" + "add Account.png")
            self.driver.close()
            self.logger.error("****************** Add Account Test is Failed ************************")
            assert False

        self.logger.info("************* All actions completed test_Add_Account_003 passed *********************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Exit_Add_Account_004(self, setup):
        self.logger.info("******************** Verifying Login Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 20)
        time.sleep(1)
        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(1)
        self.logger.info("********************* Clicked on the Dashboard option. *********************")
        dashboard_option = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/ul/li[1]/a/div")))
        dashboard_option.click()

        time.sleep(1)
        self.logger.info("******************* Moved cursor to the right side *************************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/header/div/div/div[2]")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        self.logger.info("******************* Click to Add Account *************************")

        Add_Account = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/button")
        Add_Account.click()

        self.logger.info("******************* Click to Alpha Pro *************************")

        alpha_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div/div/div/button[1]")))
        alpha_button.click()

        time.sleep(1)
        self.logger.info("********************* Scrolling down to make an element visible *********************")
        alpha_pro_10K_button = self.driver.find_element(By.XPATH,
                                                        "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/button")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", alpha_pro_10K_button)
        time.sleep(1)

        self.logger.info("********************* Clicked on the alpha_pro_10K button *********************")
        alpha_pro_10K_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                      "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/button")))
        alpha_pro_10K_button.click()

        self.logger.info("******************* Click to Exit Alpha Pro *************************")

        Exit_Button_Xpath_Alpha_Pro = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                      "/html/body/div[1]/div/div[1]/div/div[1]/div/a")))
        Exit_Button_Xpath_Alpha_Pro.click()

        self.logger.info("******************* Click Free Trial *************************")

        Free_Trial = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                      "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div/div/div/button[2]")))
        Free_Trial.click()

        time.sleep(1)
        self.logger.info("********************* Scrolling down to make an element visible Try Now *********************")
        Free_tral_50K = self.driver.find_element(By.XPATH,
                                                        "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[3]/div[2]/div[1]/div[2]/div[1]/div/button")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Free_tral_50K)
        time.sleep(1)

        self.logger.info("********************* Clicked on the Free_tral_200K_Try_Now button *********************")
        Free_tral_200K_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                      "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[3]/div[2]/div[1]/div[2]/div[1]/div/button")))
        Free_tral_200K_button.click()

        self.logger.info("******************* Click to Exit Free Tral *************************")

        Exit_Button_Xpath_Free_Tral = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                      "/html/body/div[1]/div/div[1]/div/div[1]/div/a")))
        Exit_Button_Xpath_Free_Tral.click()

        self.logger.info("************* All actions completed test_Exit_Add_Account_007 passed *********************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_start_now_for_free_trail_005(self, setup):
        self.logger.info(
            "******************** test_start_now_for_free_trail_008 started **************************")
        self.logger.info("******************** Verifying Login Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 20)
        time.sleep(5)
        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(1)
        self.logger.info("********************* Clicked on the Dashboard option. *********************")
        dashboard_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/ul/li[1]/a/div")))
        dashboard_option.click()

        time.sleep(1)
        self.logger.info("******************* Moved cursor to the right side *************************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/header/div/div/div[2]")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(1)
        self.logger.info("********************* scrolling down to start now for free trail *********************")
        start_now_for_free_trail = self.driver.find_element(By.XPATH,
                                                                "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/button")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", start_now_for_free_trail)
        time.sleep(1)

        self.logger.info("********************* Click to start now for free trail *********************")

        start_now_2 = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                 "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/button")))
        start_now_2.click()

        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Add Account Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info(
                " ************************* start now for free trail Title is as expected. ******************************")
            assert True
            self.driver.close()
            self.logger.info("****************** start now for free trail Test is Passed ************************")
        else:
            self.logger.error("start now for free trail Title is not as expected. Taking a screenshot.")
            self.driver.save_screenshot(".\\Screenshots\\" + "start now for free trail.png")
            self.driver.close()
            self.logger.error("****************** start now for free trail Test is Failed ************************")
            assert False

        self.logger.info("************* start_now_for_free_trail_008 Test Passed *********************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_start_now_for_Alpha_Pro_006(self, setup):
        self.logger.info(
                "******************** test_start_now_for_Alpha_Pro_006 started **************************")
        self.logger.info("******************** Verifying Login Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 20)
        time.sleep(5)
        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(1)
        self.logger.info("********************* Clicked on the Dashboard option. *********************")
        dashboard_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/ul/li[1]/a/div")))
        dashboard_option.click()

        time.sleep(1)
        self.logger.info("******************* Moved cursor to the right side *************************")
        right_element = self.driver.find_element(By.XPATH,
                                                         "/html/body/div[1]/div/div[1]/div/header/div/div/div[2]")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(1)
        self.logger.info(
            "********************* scrolling down to start now for free trail *********************")
        start_now_for_free_trail = self.driver.find_element(By.XPATH,
                                                                 "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/div[1]/div/div[2]/button")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", start_now_for_free_trail)
        time.sleep(1)

        self.logger.info("********************* Click to start now for Alpha Pro *********************")

        start_now_2 = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                     "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/div[1]/div/div[2]/button")))
        start_now_2.click()

        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Add Account Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info(
                    " ************************* start now for Alpha Pro Title is as expected. ******************************")
            assert True
            self.driver.close()
            self.logger.info(
                        "****************** start now for Alpha Pro Test is Passed ************************")
        else:
            self.logger.error("start now for Alpha Pro Title is not as expected. Taking a screenshot.")
            self.driver.save_screenshot(".\\Screenshots\\" + "start now for Alpha Pro.png")
            self.driver.close()
            self.logger.error(
                        "****************** start now for Alpha Pro Test is Failed ************************")
            assert False

        self.logger.info("************* test_start_now_for_Alpha_Pro_006 Test Passed *********************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Check_all_Boxes_Avalable_007(self, setup):
        self.logger.info("*************** test_Check_all_Boxes_Avalable_007 test case started *********************")
        self.logger.info("******************** Verifying Login Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 20)

        time.sleep(1)
        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(1)
        self.logger.info("********************* Clicked on the Dashboard option. *********************")
        dashboard_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/ul/li[1]/a/div")))
        dashboard_option.click()

        time.sleep(1)
        self.logger.info("******************* Moved cursor to the right side *************************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/header/div/div/div[2]")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(1)
        self.logger.info("******************* check Trader Badge Box visible or Not *************************")

        Trader_Badge_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div[2]/div/div/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Trader_Badge_Xpath)))
            self.logger.info(f"'{Trader_Badge_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Trader_Badge_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Trader Badge.png")

        self.logger.info("******************* Trader Badge Box visible *************************")

        self.logger.info("******************* Check ACTIVE ACCOUNTS Box visible or Not *************************")

        time.sleep(1)

        ACTIVE_ACCOUNTS_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div[1]/div/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, ACTIVE_ACCOUNTS_Xpath)))
            self.logger.info(f"'{ACTIVE_ACCOUNTS_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{ACTIVE_ACCOUNTS_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "ACTIVE ACCOUNTS.png")

        self.logger.info("******************* ACTIVE ACCOUNTS Box visible *************************")

        self.logger.info("******************* DISCORD ANNOUNCEMENTS Box visible or Not *************************")

        time.sleep(1)

        DISCORD_ANNOUNCEMENTS_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div[1]/div[1]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, DISCORD_ANNOUNCEMENTS_Xpath)))
            self.logger.info(f"'{DISCORD_ANNOUNCEMENTS_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{DISCORD_ANNOUNCEMENTS_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "DISCORD ANNOUNCEMENTS.png")

        self.logger.info("******************* DISCORD ANNOUNCEMENTS Box visible *************************")

        self.logger.info("******************* TWITTER UPDATES Box visible or Not *************************")

        time.sleep(1)

        TWITTER_UPDATES_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div[1]/div[1]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, TWITTER_UPDATES_Xpath)))
            self.logger.info(f"'{TWITTER_UPDATES_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{TWITTER_UPDATES_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "TWITTER UPDATES.png")

        self.logger.info("******************* TWITTER UPDATES Box visible *************************")

        self.logger.info("******************* CHALLENGES Box visible or Not *************************")

        time.sleep(1)

        CHALLENGES_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div[3]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, CHALLENGES_Xpath)))
            self.logger.info(f"'{CHALLENGES_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{CHALLENGES_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "CHALLENGES.png")

        self.logger.info("******************* CHALLENGES Box visible *************************")

        self.logger.info("******************* test_Check_all_Boxes_Avalable_007 test case Pass *************************")
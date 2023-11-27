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

class Test_Competition:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    competition_list_xpath = "//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiListItemText-primary') and contains(., 'Competition List')]"  # Correct XPath for the Competition List option
    leaderboard_list_xpath = "//span[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiListItemText-primary') and contains(., 'Leaderboard List')]"  # New XPath for Leaderboard List
    logger = LogGenerator.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Competition_List(self, setup):
        self.logger.info("******************** Verifying Competition List Test **************************")
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

        # Use JavaScript to scroll to the competition element
        self.logger.info("***************** Scrolling to view the competition element *******************")
        competition_element = self.driver.find_element(By.XPATH, self.competition_list_xpath)  # Use the correct XPath expression
        self.driver.execute_script("arguments[0].scrollIntoView(true);", competition_element)

        time.sleep(2)

        # Click on the competition element
        self.logger.info("***************** Clicking on the Competition List option *******************")
        competition_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        # Verify if the page title is as expected
        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Competition List Page Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info("Competition List Test Passed: Page title is as expected.")
            assert True
        else:
            self.logger.error("Competition List Test Failed: Page title is not as expected.")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Competition_List.png")
            assert False

        self.driver.close()
        self.logger.info("****************** Competition List Test is completed ************************")

        self.logger.info(" ************************** test_Competition_List passed ************************")


        @pytest.mark.sanity
        @pytest.mark.regression
        def test_Competition_List_In_Upcoming_Check_Alpha_and_Community_003(self, setup):
            self.logger.info(
                "******************** test_Competition_List_In_Upcoming_Check_Alpha_and_Community_003 test case start  **************************")
            self.logger.info("******************** Verifying Competition List Test **************************")
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

            # Use JavaScript to scroll to the competition element
            self.logger.info("***************** Scrolling to view the competition element *******************")
            competition_element = self.driver.find_element(By.XPATH,
                                                           self.competition_list_xpath)  # Use the correct XPath expression
            self.driver.execute_script("arguments[0].scrollIntoView(true);", competition_element)

            time.sleep(2)

            # Click on the competition element
            self.logger.info("***************** Clicking on the Competition List option *******************")
            competition_element.click()

            # Add your code to move the cursor to the right side here
            self.logger.info("***************** Moved cursor to the right side *******************")
            right_element = self.driver.find_element(By.XPATH,
                                                     "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
            action = ActionChains(self.driver)
            action.move_to_element(right_element)
            action.perform()

            time.sleep(2)

            self.logger.info("***************** Click Community *******************")

            Click_Community = self.driver.find_element(By.XPATH,
                                                       "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div/button[2]")
            Click_Community.click()

            # Verify if the page title is as expected
            expected_title = "Alpha Capital"
            actual_title = self.driver.title
            self.logger.info(f"Actual Competition List Page Title: {actual_title}")

            if actual_title == expected_title:
                self.logger.info("Competition List Test Passed: Page title is as expected.")
                assert True
            else:
                self.logger.error("Competition List Test Failed: Page title is not as expected.")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_Competition_List.png")
                assert False

            self.driver.close()
            self.logger.info(
                " ************************** test_Competition_List_In_Upcoming_Check_Alpha_and_Community_003 passed ************************")

        @pytest.mark.sanity
        @pytest.mark.regression
        def test_Competition_List_In_Ongoing_Check_Alpha_and_Community_004(self, setup):
            self.logger.info(
                "******************** test_Competition_List_In_Ongoing_Check_Alpha_and_Community_004 test case start  **************************")
            self.logger.info("******************** Verifying Competition List Test **************************")
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

            # Use JavaScript to scroll to the competition element
            self.logger.info("***************** Scrolling to view the competition element *******************")
            competition_element = self.driver.find_element(By.XPATH,
                                                           self.competition_list_xpath)  # Use the correct XPath expression
            self.driver.execute_script("arguments[0].scrollIntoView(true);", competition_element)

            time.sleep(2)

            # Click on the competition element
            self.logger.info("***************** Clicking on the Competition List option *******************")
            competition_element.click()

            # Add your code to move the cursor to the right side here
            self.logger.info("***************** Moved cursor to the right side *******************")
            right_element = self.driver.find_element(By.XPATH,
                                                     "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
            action = ActionChains(self.driver)
            action.move_to_element(right_element)
            action.perform()

            time.sleep(2)

            self.logger.info("***************** Click Ongoing *******************")

            Click_Ongoing = self.driver.find_element(By.XPATH,
                                                     "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[2]")
            Click_Ongoing.click()

            self.logger.info("***************** Click Community *******************")

            Click_Community = self.driver.find_element(By.XPATH,
                                                       "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div/button[2]")
            Click_Community.click()

            # Verify if the page title is as expected
            expected_title = "Alpha Capital"
            actual_title = self.driver.title
            self.logger.info(f"Actual Competition List Page Title: {actual_title}")

            if actual_title == expected_title:
                self.logger.info("Competition List Test Passed: Page title is as expected.")
                assert True
            else:
                self.logger.error("Competition List Test Failed: Page title is not as expected.")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_Competition_List.png")
                assert False

            self.driver.close()
            self.logger.info(
                " ************************** test_Competition_List_In_Ongoing_Check_Alpha_and_Community_004 passed ************************")

        @pytest.mark.sanity
        @pytest.mark.regression
        def test_Competition_List_In_Ongoing_Check_Leadership_005(self, setup):
            self.logger.info(
                "******************** test_Competition_List_In_Ongoing_Check_Leadership_005 test case start  **************************")
            self.logger.info("******************** Verifying Competition List Test **************************")
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

            # Use JavaScript to scroll to the competition element
            self.logger.info("***************** Scrolling to view the competition element *******************")
            competition_element = self.driver.find_element(By.XPATH,
                                                           self.competition_list_xpath)  # Use the correct XPath expression
            self.driver.execute_script("arguments[0].scrollIntoView(true);", competition_element)

            time.sleep(2)

            # Click on the competition element
            self.logger.info("***************** Clicking on the Competition List option *******************")
            competition_element.click()

            # Add your code to move the cursor to the right side here
            self.logger.info("***************** Moved cursor to the right side *******************")
            right_element = self.driver.find_element(By.XPATH,
                                                     "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
            action = ActionChains(self.driver)
            action.move_to_element(right_element)
            action.perform()

            time.sleep(2)

            self.logger.info("***************** Click Ongoing *******************")

            Click_Ongoing = self.driver.find_element(By.XPATH,
                                                     "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[2]")
            Click_Ongoing.click()

            self.logger.info("***************** Click See Leadership *******************")

            Leadership_Xpath = self.driver.find_element(By.XPATH,
                                                        "/html/body/div[1]/div/div[1]/div/main/div[2]/div[3]/div[1]/div/div/div[6]/button")
            Leadership_Xpath.click()

            self.driver.close()
            self.logger.info(
                " ************************** test_Competition_List_In_Ongoing_Check_Leadership_005 passed ************************")

        @pytest.mark.sanity
        @pytest.mark.regression
        def test_Competition_List_In_Ongoing_Check_Leadership_Search_user_006(self, setup):
            self.logger.info(
                "******************** test_Competition_List_In_Ongoing_Check_Leadership_Search_user_006 test case start  **************************")
            self.logger.info("******************** Verifying Competition List Test **************************")
            self.driver = setup
            self.driver.get(self.baseURL)
            self.lp = Dashboard(self.driver)
            self.lp.setEmail(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            wait = WebDriverWait(self.driver, 120)
            time.sleep(2)

            self.logger.info("***************** Moved cursor to the left side *******************")
            left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
            action = ActionChains(self.driver)
            action.move_to_element(left_element)
            action.perform()

            time.sleep(2)

            # Use JavaScript to scroll to the competition element
            self.logger.info("***************** Scrolling to view the competition element *******************")
            competition_element = self.driver.find_element(By.XPATH,
                                                           self.competition_list_xpath)  # Use the correct XPath expression
            self.driver.execute_script("arguments[0].scrollIntoView(true);", competition_element)

            time.sleep(2)

            # Click on the competition element
            self.logger.info("***************** Clicking on the Competition List option *******************")
            competition_element.click()

            # Add your code to move the cursor to the right side here
            self.logger.info("***************** Moved cursor to the right side *******************")
            right_element = self.driver.find_element(By.XPATH,
                                                     "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
            action = ActionChains(self.driver)
            action.move_to_element(right_element)
            action.perform()

            time.sleep(2)

            self.logger.info("***************** Click Ongoing *******************")

            Click_Ongoing = self.driver.find_element(By.XPATH,
                                                     "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[2]")
            Click_Ongoing.click()

            self.logger.info("***************** Click See Leadership *******************")

            Leadership_Xpath = self.driver.find_element(By.XPATH,
                                                        "/html/body/div[1]/div/div[1]/div/main/div[2]/div[3]/div[1]/div/div/div[6]/button")
            Leadership_Xpath.click()

            self.logger.info("***************** Wait visible of element locate *******************")

            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div[1]/div")))

            self.logger.info("***************** Scroll visible of element *******************")

            search_Box_Xpath = self.driver.find_element(By.XPATH,
                                                        "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/input")

            self.driver.execute_script("arguments[0].scrollIntoView(true);", search_Box_Xpath)

            self.logger.info("***************** Send user name User *******************")
            Search_N_Textbox_New = self.driver.find_element(By.XPATH,
                                                            "//input[@placeholder='Search by name' and @type='text' and @aria-label='search' and @class='MuiInputBase-input css-1jhxu0']")
            Search_N_Textbox_New.send_keys("Kanhu")

            self.logger.info("***************** Search User *******************")
            Search_button_Xpath = self.driver.find_element(By.XPATH,
                                                           "//button[contains(@class, 'MuiButton-outlined') and contains(@class, 'css-9h0458') and @tabindex='0' and @type='button']")
            Search_button_Xpath.click()

            self.driver.close()
            self.logger.info(
                " ************************** test_Competition_List_In_Ongoing_Check_Leadership_Search_user_006 passed ************************")

        @pytest.mark.sanity
        @pytest.mark.regression
        def test_Competition_List_End_007(self, setup):
            self.logger.info(
                "******************** test_Competition_List_End_007 Test case start **************************")
            self.logger.info("******************** Verifying Competition List Test **************************")
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

            # Use JavaScript to scroll to the competition element
            self.logger.info("***************** Scrolling to view the competition element *******************")
            competition_element = self.driver.find_element(By.XPATH,
                                                           self.competition_list_xpath)  # Use the correct XPath expression
            self.driver.execute_script("arguments[0].scrollIntoView(true);", competition_element)

            time.sleep(2)

            # Click on the competition element
            self.logger.info("***************** Clicking on the Competition List option *******************")
            competition_element.click()

            # Add your code to move the cursor to the right side here
            self.logger.info("***************** Moved cursor to the right side *******************")
            right_element = self.driver.find_element(By.XPATH,
                                                     "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
            action = ActionChains(self.driver)
            action.move_to_element(right_element)
            action.perform()

            time.sleep(2)

            self.logger.info("***************** Click End *******************")

            End_Xpath = self.driver.find_element(By.XPATH,
                                                 "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[3]")
            End_Xpath.click()

            # Verify if the page title is as expected
            expected_title = "Alpha Capital"
            actual_title = self.driver.title
            self.logger.info(f"Actual Competition List Page Title: {actual_title}")

            if actual_title == expected_title:
                self.logger.info("Competition List Test Passed: Page title is as expected.")
                assert True
            else:
                self.logger.error("Competition List Test Failed: Page title is not as expected.")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_Competition_List.png")
                assert False

            self.driver.close()

            self.logger.info(
                " ************************** test_Competition_List_End_007 passed ************************")

        @pytest.mark.sanity
        @pytest.mark.regression
        def test_Competition_List_End_Alpha_Community_008(self, setup):
            self.logger.info(
                "******************** test_Competition_List_End_Alpha_Community_008 Test case start **************************")
            self.logger.info("******************** Verifying Competition List Test **************************")
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

            # Use JavaScript to scroll to the competition element
            self.logger.info("***************** Scrolling to view the competition element *******************")
            competition_element = self.driver.find_element(By.XPATH,
                                                           self.competition_list_xpath)  # Use the correct XPath expression
            self.driver.execute_script("arguments[0].scrollIntoView(true);", competition_element)

            time.sleep(2)

            # Click on the competition element
            self.logger.info("***************** Clicking on the Competition List option *******************")
            competition_element.click()

            # Add your code to move the cursor to the right side here
            self.logger.info("***************** Moved cursor to the right side *******************")
            right_element = self.driver.find_element(By.XPATH,
                                                     "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
            action = ActionChains(self.driver)
            action.move_to_element(right_element)
            action.perform()

            time.sleep(2)

            self.logger.info("***************** Click End *******************")

            End_Xpath = self.driver.find_element(By.XPATH,
                                                 "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[3]")
            End_Xpath.click()

            self.logger.info("***************** Click Community *******************")

            Community_Xpath = self.driver.find_element(By.XPATH,
                                                       "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div/button[2]")
            Community_Xpath.click()

            # Verify if the page title is as expected
            expected_title = "Alpha Capital"
            actual_title = self.driver.title
            self.logger.info(f"Actual Competition List Page Title: {actual_title}")

            if actual_title == expected_title:
                self.logger.info("Competition List Test Passed: Page title is as expected.")
                assert True
            else:
                self.logger.error("Competition List Test Failed: Page title is not as expected.")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_Competition_List.png")
                assert False

            self.driver.close()

            self.logger.info(
                " ************************** test_Competition_List_End_Alpha_Community_008 passed ************************")

        @pytest.mark.sanity
        @pytest.mark.regression
        def test_Competition_List_Participed_Alpha_Community_008(self, setup):
            self.logger.info(
                "******************** test_Competition_List_Participed_Alpha_Community_008 Test case start **************************")
            self.logger.info("******************** Verifying Competition List Test **************************")
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

            # Use JavaScript to scroll to the competition element
            self.logger.info("***************** Scrolling to view the competition element *******************")
            competition_element = self.driver.find_element(By.XPATH,
                                                           self.competition_list_xpath)  # Use the correct XPath expression
            self.driver.execute_script("arguments[0].scrollIntoView(true);", competition_element)

            time.sleep(2)

            # Click on the competition element
            self.logger.info("***************** Clicking on the Competition List option *******************")
            competition_element.click()

            # Add your code to move the cursor to the right side here
            self.logger.info("***************** Moved cursor to the right side *******************")
            right_element = self.driver.find_element(By.XPATH,
                                                     "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
            action = ActionChains(self.driver)
            action.move_to_element(right_element)
            action.perform()

            time.sleep(2)

            self.logger.info("***************** Click Participed *******************")

            Participed_Xpath = self.driver.find_element(By.XPATH,
                                                        "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[3]")
            Participed_Xpath.click()

            self.logger.info("***************** Click Community *******************")

            Community_Xpath = self.driver.find_element(By.XPATH,
                                                       "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div/button[2]")
            Community_Xpath.click()

            # Verify if the page title is as expected
            expected_title = "Alpha Capital"
            actual_title = self.driver.title
            self.logger.info(f"Actual Competition List Page Title: {actual_title}")

            if actual_title == expected_title:
                self.logger.info("Competition List Test Passed: Page title is as expected.")
                assert True
            else:
                self.logger.error("Competition List Test Failed: Page title is not as expected.")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_Competition_List.png")
                assert False

            self.driver.close()

            self.logger.info(
                " ************************** test_Competition_List_Participed_Alpha_Community_008 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Leaderboard_List_009(self, setup):
        self.logger.info("******************** test_Leaderboard_List_009 Test Start **************************")
        self.logger.info("******************** Verifying Leaderboard List Test **************************")
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

        # Use JavaScript to scroll to the Leaderboard List element
        self.logger.info("***************** Scrolling to view the Leaderboard List element *******************")
        leaderboard_element = self.driver.find_element(By.XPATH, self.leaderboard_list_xpath)  # Use the correct XPath expression
        self.driver.execute_script("arguments[0].scrollIntoView(true);", leaderboard_element)

        time.sleep(2)

        # Click on the Leaderboard List element
        self.logger.info("***************** Clicking on the Leaderboard List option *******************")
        leaderboard_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        # Verify if the page title is as expected
        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Leaderboard List Page Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info("Leaderboard List Test Passed: Page title is as expected.")
            assert True
        else:
            self.logger.error("Leaderboard List Test Failed: Page title is not as expected.")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Leaderboard_List.png")
            assert False

        self.driver.close()
        self.logger.info("****************** Leaderboard List Test is completed ************************")

        self.logger.info(" ************************** test_Leaderboard_List_009 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Leaderboard_List_End_010(self, setup):
        self.logger.info("******************** test_Leaderboard_List_End_010 Test Start **************************")
        self.logger.info("******************** Verifying Leaderboard List Test **************************")
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

        # Use JavaScript to scroll to the Leaderboard List element
        self.logger.info("***************** Scrolling to view the Leaderboard List element *******************")
        leaderboard_element = self.driver.find_element(By.XPATH,
                                                       self.leaderboard_list_xpath)  # Use the correct XPath expression
        self.driver.execute_script("arguments[0].scrollIntoView(true);", leaderboard_element)

        time.sleep(2)

        # Click on the Leaderboard List element
        self.logger.info("***************** Clicking on the Leaderboard List option *******************")
        leaderboard_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH,
                                                 "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("***************** Click on Community *******************")

        Community_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div/button[2]")
        Community_Xpath.click()

        # Verify if the page title is as expected
        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Leaderboard List Page Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info("Leaderboard List Test Passed: Page title is as expected.")
            assert True
        else:
            self.logger.error("Leaderboard List Test Failed: Page title is not as expected.")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Leaderboard_List.png")
            assert False

        self.driver.close()
        self.logger.info("****************** test_Leaderboard_List_End_010 Test is completed ************************")

        self.logger.info(" ************************** test_Leaderboard_List_End_010 passed ************************")


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Leaderboard_List_End_011(self, setup):
        self.logger.info("******************** test_Leaderboard_List_End_011 Test Start **************************")
        self.logger.info("******************** Verifying Leaderboard List Test **************************")
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

        # Use JavaScript to scroll to the Leaderboard List element
        self.logger.info("***************** Scrolling to view the Leaderboard List element *******************")
        leaderboard_element = self.driver.find_element(By.XPATH,
                                                       self.leaderboard_list_xpath)  # Use the correct XPath expression
        self.driver.execute_script("arguments[0].scrollIntoView(true);", leaderboard_element)

        time.sleep(2)

        # Click on the Leaderboard List element
        self.logger.info("***************** Clicking on the Leaderboard List option *******************")
        leaderboard_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH,
                                                 "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("***************** Click on Participed *******************")

        Participed_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[2]")
        Participed_Xpath.click()

        self.logger.info("***************** Click on Community *******************")

        Community_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div/button[2]")
        Community_Xpath.click()

        # Verify if the page title is as expected
        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Leaderboard List Page Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info("Leaderboard List Test Passed: Page title is as expected.")
            assert True
        else:
            self.logger.error("Leaderboard List Test Failed: Page title is not as expected.")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Leaderboard_List.png")
            assert False

        self.driver.close()
        self.logger.info("****************** test_Leaderboard_List_End_011 Test is completed ************************")

        self.logger.info(" ************************** test_Leaderboard_List_End_011 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Competition_List_End_Alpha_See_Leadership_012(self, setup):
        self.logger.info("******************** Verifying Competition List Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 120)
        time.sleep(2)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(2)

        # Use JavaScript to scroll to the competition element
        self.logger.info("***************** Scrolling to view the competition element *******************")
        competition_element = self.driver.find_element(By.XPATH, self.competition_list_xpath)  # Use the correct XPath expression
        self.driver.execute_script("arguments[0].scrollIntoView(true);", competition_element)

        time.sleep(2)

        # Click on the competition element
        self.logger.info("***************** Clicking on the Competition List option *******************")
        competition_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("***************** Click on End *******************")

        Click_End_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[3]")
        Click_End_Xpath.click()

        self.logger.info("***************** Click See Leadership *******************")

        Leadership_Xpath = self.driver.find_element(By.XPATH,
                                                    "/html/body/div[1]/div/div[1]/div/main/div[2]/div[3]/div[1]/div/div/div[6]/button")
        Leadership_Xpath.click()

        self.logger.info("***************** Wait visible of element locate *******************")

        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div[1]/div")))

        self.logger.info("***************** Scroll visible of element *******************")

        search_Box_Xpath = self.driver.find_element(By.XPATH,
                                                    "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/input")

        self.driver.execute_script("arguments[0].scrollIntoView(true);", search_Box_Xpath)

        self.logger.info("***************** Send user name User *******************")
        Search_N_Textbox_New = self.driver.find_element(By.XPATH,
                                                        "//input[@placeholder='Search by name' and @type='text' and @aria-label='search' and @class='MuiInputBase-input css-1jhxu0']")
        Search_N_Textbox_New.send_keys("Kanhu")

        self.logger.info("***************** Search User *******************")
        Search_button_Xpath = self.driver.find_element(By.XPATH,
                                                       "//button[contains(@class, 'MuiButton-outlined') and contains(@class, 'css-9h0458') and @tabindex='0' and @type='button']")
        Search_button_Xpath.click()

        self.driver.close()
        self.logger.info(
            " ************************** test_Competition_List_End_Alpha_See_Leadership_012 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Competition_List_End_Alpha_See_Leadership_For_Community_013(self, setup):
        self.logger.info("******************** Verifying Competition List Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 120)
        time.sleep(2)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(2)

        # Use JavaScript to scroll to the competition element
        self.logger.info("***************** Scrolling to view the competition element *******************")
        competition_element = self.driver.find_element(By.XPATH, self.competition_list_xpath)  # Use the correct XPath expression
        self.driver.execute_script("arguments[0].scrollIntoView(true);", competition_element)

        time.sleep(2)

        # Click on the competition element
        self.logger.info("***************** Clicking on the Competition List option *******************")
        competition_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("***************** Click on End *******************")

        Click_End_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[3]")
        Click_End_Xpath.click()

        self.logger.info("***************** Click on Community *******************")

        Community_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div/button[2]")
        Community_Xpath.click()

        self.logger.info("***************** Click See Leadership *******************")

        Leadership_Xpath = self.driver.find_element(By.XPATH,
                                                    "/html/body/div[1]/div/div[1]/div/main/div[2]/div[3]/div[1]/div/div/div[6]/button")
        Leadership_Xpath.click()

        self.logger.info("***************** Wait visible of element locate *******************")

        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div[1]/div")))

        self.logger.info("***************** Scroll visible of element *******************")

        search_Box_Xpath = self.driver.find_element(By.XPATH,
                                                    "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/input")

        self.driver.execute_script("arguments[0].scrollIntoView(true);", search_Box_Xpath)

        self.logger.info("***************** Send user name User *******************")
        Search_N_Textbox_New = self.driver.find_element(By.XPATH,
                                                        "//input[@placeholder='Search by name' and @type='text' and @aria-label='search' and @class='MuiInputBase-input css-1jhxu0']")
        Search_N_Textbox_New.send_keys("Kanhu")

        self.logger.info("***************** Search User *******************")
        Search_button_Xpath = self.driver.find_element(By.XPATH,
                                                       "//button[contains(@class, 'MuiButton-outlined') and contains(@class, 'css-9h0458') and @tabindex='0' and @type='button']")
        Search_button_Xpath.click()

        self.driver.close()
        self.logger.info(
            " ************************** test_Competition_List_End_Alpha_See_Leadership_For_Community_013 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Competition_List_Participeted_Alpha_See_Leadership_For_Alpha_014(self, setup):
        self.logger.info("******************** Verifying Competition List Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 120)
        time.sleep(2)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(2)

        # Use JavaScript to scroll to the competition element
        self.logger.info("***************** Scrolling to view the competition element *******************")
        competition_element = self.driver.find_element(By.XPATH, self.competition_list_xpath)  # Use the correct XPath expression
        self.driver.execute_script("arguments[0].scrollIntoView(true);", competition_element)

        time.sleep(2)

        # Click on the competition element
        self.logger.info("***************** Clicking on the Competition List option *******************")
        competition_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("***************** Click on Participed *******************")

        Click_Participed_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[4]")
        Click_Participed_Xpath.click()

        self.logger.info("***************** Click See Leadership *******************")

        Leadership_Xpath = self.driver.find_element(By.XPATH,
                                                    "/html/body/div[1]/div/div[1]/div/main/div[2]/div[3]/div[1]/div/div/div[6]/button")
        Leadership_Xpath.click()

        self.logger.info("***************** Wait visible of element locate *******************")

        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div[1]/div")))

        self.logger.info("***************** Scroll visible of element *******************")

        search_Box_Xpath = self.driver.find_element(By.XPATH,
                                                    "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/input")

        self.driver.execute_script("arguments[0].scrollIntoView(true);", search_Box_Xpath)

        self.logger.info("***************** Send user name User *******************")
        Search_N_Textbox_New = self.driver.find_element(By.XPATH,
                                                        "//input[@placeholder='Search by name' and @type='text' and @aria-label='search' and @class='MuiInputBase-input css-1jhxu0']")
        Search_N_Textbox_New.send_keys("Kanhu")

        self.logger.info("***************** Search User *******************")
        Search_button_Xpath = self.driver.find_element(By.XPATH,
                                                       "//button[contains(@class, 'MuiButton-outlined') and contains(@class, 'css-9h0458') and @tabindex='0' and @type='button']")
        Search_button_Xpath.click()

        self.driver.close()
        self.logger.info(
            " ************************** test_Competition_List_Participeted_Alpha_See_Leadership_For_Alpha_014 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Competition_List_Participeted_Alpha_See_Leadership_For_Community_015(self, setup):
        self.logger.info("******************** Verifying Competition List Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 120)
        time.sleep(2)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(2)

        # Use JavaScript to scroll to the competition element
        self.logger.info("***************** Scrolling to view the competition element *******************")
        competition_element = self.driver.find_element(By.XPATH, self.competition_list_xpath)  # Use the correct XPath expression
        self.driver.execute_script("arguments[0].scrollIntoView(true);", competition_element)

        time.sleep(2)

        # Click on the competition element
        self.logger.info("***************** Clicking on the Competition List option *******************")
        competition_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("***************** Click on Participed *******************")

        Click_Participed_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[4]")
        Click_Participed_Xpath.click()

        self.logger.info("***************** Click on Community *******************")

        Community_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div/button[2]")
        Community_Xpath.click()

        self.logger.info("***************** Click See Leadership *******************")

        Leadership_Xpath = self.driver.find_element(By.XPATH,
                                                    "/html/body/div[1]/div/div[1]/div/main/div[2]/div[3]/div[1]/div/div/div[6]/button")
        Leadership_Xpath.click()

        self.logger.info("***************** Wait visible of element locate *******************")

        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div[1]/div")))

        self.logger.info("***************** Scroll visible of element *******************")

        search_Box_Xpath = self.driver.find_element(By.XPATH,
                                                    "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/input")

        self.driver.execute_script("arguments[0].scrollIntoView(true);", search_Box_Xpath)

        self.logger.info("***************** Send user name User *******************")
        Search_N_Textbox_New = self.driver.find_element(By.XPATH,
                                                        "//input[@placeholder='Search by name' and @type='text' and @aria-label='search' and @class='MuiInputBase-input css-1jhxu0']")
        Search_N_Textbox_New.send_keys("Kanhu")

        self.logger.info("***************** Search User *******************")
        Search_button_Xpath = self.driver.find_element(By.XPATH,
                                                       "//button[contains(@class, 'MuiButton-outlined') and contains(@class, 'css-9h0458') and @tabindex='0' and @type='button']")
        Search_button_Xpath.click()

        self.driver.close()
        self.logger.info(
            " ************************** test_Competition_List_Participeted_Alpha_See_Leadership_For_Community_015 passed ************************")

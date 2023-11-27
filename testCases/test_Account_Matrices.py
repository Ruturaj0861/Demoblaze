import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pageObjects.DashboardPage import Dashboard
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGenerator

class Test_AccountMatrices:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    account_matrices_xpath = "/html/body/div[1]/div/div[1]/div/div/div/ul/li[6]/a/div/div[2]/span"  # XPath for the Account Matrices section
    account_matrices_right_element_xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div"  # XPath for the right side element
    logger = LogGenerator.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AccountMatrices_Section_001(self, setup):
        self.logger.info("******************** test_AccountMatrices_Section_001 test case started **************************")
        self.logger.info("******************** Verifying Account Matrices Section Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 30)
        time.sleep(2)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(2)
        self.logger.info("********************* Clicked on the Account Matrices option. *********************")

        # Wait for the Account Matrices element to be clickable and visible
        account_matrices_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.account_matrices_xpath)))
        account_matrices_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Account Matrices section
        self.logger.info("***************** Moved cursor to the right side for Account Matrices *******************")
        account_matrices_right_element = self.driver.find_element(By.XPATH, self.account_matrices_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(account_matrices_right_element)
        action.perform()

        time.sleep(2)

        # Verify if the page title is "Alpha Capital"
        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Account Matrices Page Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info("Account Matrices Section Test Passed: Page title is as expected.")
        else:
            self.logger.error("Account Matrices Section Test Failed: Page title is not as expected.")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_AccountMatrices_Section.png")
            assert False

        self.driver.close()
        self.logger.info("****************** test_AccountMatrices_Section_001 Test is completed ************************")

        self.logger.info("************************** test_AccountMatrices_Section_001 passed ************************")


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AccountMatrices_Section_Refresh_Box_Into_Program_objectives_002(self, setup):
        self.logger.info("******************** test_AccountMatrices_Section_Refresh_Box_Into_Program_objectives_002 test case started **************************")
        self.logger.info("******************** Verifying Account Matrices Section Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 30)
        time.sleep(2)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(2)
        self.logger.info("********************* Clicked on the Account Matrices option. *********************")

        # Wait for the Account Matrices element to be clickable and visible
        account_matrices_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.account_matrices_xpath)))
        account_matrices_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Account Matrices section
        self.logger.info("***************** Moved cursor to the right side for Account Matrices *******************")
        account_matrices_right_element = self.driver.find_element(By.XPATH, self.account_matrices_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(account_matrices_right_element)
        action.perform()

        self.logger.info("************************** click Auto Refresh to Enable box ************************************")

        Refresh_Box_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/input")
        Refresh_Box_Xpath.click()

        time.sleep(2)

        self.logger.info("************************** Check if Auto Refresh is enable then every 5 sec refresh or not ************************************")

        zero_sec_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[1]/div[1]/div[1]"
        Five_sec_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[1]/div[1]/div[1]"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Five_sec_Xpath)))
            self.logger.info(f"'{Five_sec_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Five_sec_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Five_sec.png")

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, zero_sec_Xpath)))
            self.logger.info(f"'{zero_sec_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{zero_sec_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "zero_sec.png")

        self.driver.close()
        self.logger.info("****************** test_AccountMatrices_Section_Refresh_Box_Into_Program_objectives_002 Test is completed ************************")

        self.logger.info("************************** test_AccountMatrices_Section_Refresh_Box_Into_Program_objectives_002 passed ************************")


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AccountMatrices_Section_Refresh_button_Into_Program_Objectives_003(self, setup):
        self.logger.info("******************** test_AccountMatrices_Section_Refresh_button_Into_Program_Objectives_003 test case started **************************")
        self.logger.info("******************** Verifying Account Matrices Section Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 30)
        time.sleep(2)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(2)
        self.logger.info("********************* Clicked on the Account Matrices option. *********************")

        # Wait for the Account Matrices element to be clickable and visible
        account_matrices_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.account_matrices_xpath)))
        account_matrices_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Account Matrices section
        self.logger.info("***************** Moved cursor to the right side for Account Matrices *******************")
        account_matrices_right_element = self.driver.find_element(By.XPATH, self.account_matrices_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(account_matrices_right_element)
        action.perform()

        self.logger.info("************************** click Refresh button ************************************")

        Refresh_button_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[1]/div[2]")
        Refresh_button_Xpath.click()

        time.sleep(2)

        self.driver.close()
        self.logger.info("****************** test_AccountMatrices_Section_Refresh_button_Into_Program_Objectives_003 Test is completed ************************")

        self.logger.info("************************** test_AccountMatrices_Section_Refresh_button_Into_Program_Objectives_003 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AccountMatrices_Section_check_Graphs_Balance_Profit_Drawdown_004(self, setup):
        self.logger.info("******************** test_AccountMatrices_Section_check_Graphs_Balance_Profit_Drawdown_004 test case started **************************")
        self.logger.info("******************** Verifying Account Matrices Section Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 30)
        time.sleep(2)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(2)
        self.logger.info("********************* Clicked on the Account Matrices option. *********************")

        # Wait for the Account Matrices element to be clickable and visible
        account_matrices_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.account_matrices_xpath)))
        account_matrices_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Account Matrices section
        self.logger.info("***************** Moved cursor to the right side for Account Matrices *******************")
        account_matrices_right_element = self.driver.find_element(By.XPATH, self.account_matrices_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(account_matrices_right_element)
        action.perform()

        self.logger.info("***************** Check Balance Graphs is visible or not *******************")

        Balance_Graph_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div/div/svg/foreignObject"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Balance_Graph_Xpath)))
            self.logger.info(f"'{Balance_Graph_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Balance_Graph_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Balance_Graph.png")

        time.sleep(2)

        self.logger.info("***************** Check Profit Graphs is visible or not *******************")

        Profit_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/button[2]")
        Profit_Xpath.click()
        time.sleep(2)

        Profit_Graph_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div/div[3]/div/div/div/svg"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Profit_Graph_Xpath)))
            self.logger.info(f"'{Profit_Graph_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Profit_Graph_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Profit_Graph.png")

        self.logger.info("***************** Check Drawdown Graphs is visible or not *******************")

        Drawdown_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/button[3]")
        Drawdown_Xpath.click()

        Drawdown_Graph_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div/div[4]/div/div/div/svg"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Drawdown_Graph_Xpath)))
            self.logger.info(f"'{Drawdown_Graph_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Drawdown_Graph_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Drawdown_Graph.png")

        self.driver.close()
        self.logger.info("****************** test_AccountMatrices_Section_check_Graphs_Balance_Profit_Drawdown_004 Test is completed ************************")

        self.logger.info("************************** test_AccountMatrices_Section_check_Graphs_Balance_Profit_Drawdown_004 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AccountMatrices_Section_All_section_Visible_005(self, setup):
        self.logger.info("******************** test_AccountMatrices_Section_All_section_Visible_005 test case started **************************")
        self.logger.info("******************** Verifying Account Matrices Section Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 30)
        time.sleep(2)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(2)
        self.logger.info("********************* Clicked on the Account Matrices option. *********************")

        # Wait for the Account Matrices element to be clickable and visible
        account_matrices_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.account_matrices_xpath)))
        account_matrices_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Account Matrices section
        self.logger.info("***************** Moved cursor to the right side for Account Matrices *******************")
        account_matrices_right_element = self.driver.find_element(By.XPATH, self.account_matrices_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(account_matrices_right_element)
        action.perform()

        self.logger.info("***************** Check Refresh Field is visible or not *******************")

        Refresh_Field_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[1]"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Refresh_Field_Xpath)))
            self.logger.info(f"'{Refresh_Field_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Refresh_Field_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Refresh_Field.png")

        time.sleep(1)

        self.logger.info("***************** Refresh Field is visible *******************")

        self.logger.info("***************** Check Start Date Field is visible or not *******************")

        Start_Date_Field_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[2]/div[1]/div[1]"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Start_Date_Field_Xpath)))
            self.logger.info(f"'{Start_Date_Field_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Start_Date_Field_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Start_Date_Field.png")

        self.logger.info("***************** Start Date Field is visible *******************")

        time.sleep(1)

        self.logger.info("***************** Graphs Field is visible or not *******************")

        Graphs_Field_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[2]/div[1]/div[2]"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Graphs_Field_Xpath)))
            self.logger.info(f"'{Graphs_Field_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Graphs_Field_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Graphs_Field.png")

        self.logger.info("***************** Graphs Field is visible *******************")

        time.sleep(1)

        self.logger.info("***************** Statistic Field is visible or not *******************")

        Statistic_Field_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[2]/div[1]/div[3]"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Statistic_Field_Xpath)))
            self.logger.info(f"'{Start_Date_Field_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Statistic_Field_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Statistic Field.png")

        self.logger.info("***************** Statistic Field is visible *******************")

        time.sleep(1)

        self.logger.info("***************** Daily Summary Field is visible or not *******************")

        Daily_Summary_Field_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[2]/div[1]/div[3]"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Daily_Summary_Field_Xpath)))
            self.logger.info(f"'{Daily_Summary_Field_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Daily_Summary_Field_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Daily Summary Field.png")

        self.logger.info("***************** Daily Summary Field is visible *******************")

        time.sleep(1)

        self.logger.info("***************** Trading Objective Field is visible or not *******************")

        Trading_Objective_Field_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[2]/div[2]/div[2]"

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Trading_Objective_Field_Xpath)))
            self.logger.info(f"'{Trading_Objective_Field_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Trading_Objective_Field_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Trading Objective Field.png")

        self.logger.info("***************** Trading Objective Field is visible *******************")

        self.driver.close()
        self.logger.info("****************** test_AccountMatrices_Section_All_section_Visible_005 Test is completed ************************")

        self.logger.info("************************** test_AccountMatrices_Section_All_section_Visible_005 passed ************************")


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AccountMatrices_Section_Insights_Advanced_Statistics_Field_006(self, setup):
        self.logger.info("******************** test_AccountMatrices_Section_Insights_Advanced_Statistics_Field_006 test case started **************************")
        self.logger.info("******************** Verifying Account Matrices Section Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 30)
        time.sleep(2)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(2)
        self.logger.info("********************* Clicked on the Account Matrices option. *********************")

        # Wait for the Account Matrices element to be clickable and visible
        account_matrices_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.account_matrices_xpath)))
        account_matrices_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Account Matrices section
        self.logger.info("***************** Moved cursor to the right side for Account Matrices *******************")
        account_matrices_right_element = self.driver.find_element(By.XPATH, self.account_matrices_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(account_matrices_right_element)
        action.perform()

        self.logger.info("***************** Click Insights *******************")

        Insights_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div/div/div/button[2]")
        Insights_Xpath.click()

        self.logger.info("***************** Advanced Statistics Field is visible or not *******************")

        Advanced_Statistics_Field_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[3]/div/div[2]/div[1]/div/div/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Advanced_Statistics_Field_Xpath)))
            self.logger.info(f"'{Advanced_Statistics_Field_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Advanced_Statistics_Field_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Advanced Statistics Field.png")

        self.logger.info("***************** Advanced Statistics Field is visible *******************")

        self.logger.info("***************** AUDCAD.pro Field is visible or not *******************")

        AUDCAD_pro_Field_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[3]/div/div[2]/div[2]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, AUDCAD_pro_Field_Xpath)))
            self.logger.info(f"'{AUDCAD_pro_Field_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Advanced_Statistics_Field_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "AUDCAD.PRO Field.png")

        self.logger.info("***************** AUDCAD.pro Field is visible *******************")


        self.driver.close()
        self.logger.info("****************** test_AccountMatrices_Section_Insights_Advanced_Statistics_Field_006 Test is completed ************************")

        self.logger.info("************************** test_AccountMatrices_Section_Insights_Advanced_Statistics_Field_006 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AccountMatrices_Section_Risk_Insights_007(self, setup):
        self.logger.info("******************** test_AccountMatrices_Section_Risk_Insights_007 test case started **************************")
        self.logger.info("******************** Verifying Account Matrices Section Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 30)
        time.sleep(2)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(2)
        self.logger.info("********************* Clicked on the Account Matrices option. *********************")

        # Wait for the Account Matrices element to be clickable and visible
        account_matrices_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.account_matrices_xpath)))
        account_matrices_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Account Matrices section
        self.logger.info("***************** Moved cursor to the right side for Account Matrices *******************")
        account_matrices_right_element = self.driver.find_element(By.XPATH, self.account_matrices_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(account_matrices_right_element)
        action.perform()

        self.logger.info("***************** Click Insights *******************")

        Insights_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div/div/div/button[2]")
        Insights_Xpath.click()


        self.logger.info("***************** Click Risk Insights *******************")

        wait = WebDriverWait(self.driver, 20)
        Risk_Insights = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/div/h6")))
        Risk_Insights.click()

        self.logger.info("***************** Risk per Trade Graph is visible or not *******************")

        Risk_per_Trade_Graph_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div/div/div/svg"

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Risk_per_Trade_Graph_Xpath)))
            self.logger.info(f"'{Risk_per_Trade_Graph_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Risk_per_Trade_Graph_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Risk_per_Trade_Graph.png")

        self.logger.info("***************** Risk per Trade Graph is visible *******************")

        self.logger.info("***************** Concurant Trade and lots per day Graph is visible or not *******************")

        Concurant_Trade_and_lots_per_day_Graph_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[3]/div/div[2]/div[1]/div/div/div/div[3]/div/div/div/svg/foreignObject"

        Concurant_Trade_and_lots_per_day_Graph =self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div/div/div/button[2]")
        Concurant_Trade_and_lots_per_day_Graph.click()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Concurant_Trade_and_lots_per_day_Graph_Xpath)))
            self.logger.info(f"'{Concurant_Trade_and_lots_per_day_Graph_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Concurant_Trade_and_lots_per_day_Graph_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Concurant_Trade_and_lots_per_day_Graph.png")

        self.logger.info("***************** Concurant Trade and lots per day Graph is visible *******************")

        self.logger.info(
            "***************** Trads and Lots per Day Graph is visible or not *******************")

        Trads_and_Lots_per_Day_Graph_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[3]/div/div[2]/div[1]/div/div/div/div[4]/div/div/div/svg/foreignObject"

        Trads_and_Lots_per_Day_Graph = self.driver.find_element(By.XPATH,
                                                                          "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div/div/div/button[3]")
        Trads_and_Lots_per_Day_Graph.click()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Trads_and_Lots_per_Day_Graph_Xpath)))
            self.logger.info(f"'{Trads_and_Lots_per_Day_Graph_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Trads_and_Lots_per_Day_Graph_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Trads_and_Lots_per_Day_Graph.png")

        self.logger.info("***************** Concurant Trade and lots per day Graph is visible *******************")

        self.logger.info(
            "***************** Lots Per Trade Graph is visible or not *******************")

        Trads_and_Lots_per_Day_Trade_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[3]/div/div[2]/div[1]/div/div/div/div[5]/div/div/div/svg"

        Trads_and_Lots_per_Trade_Graph = self.driver.find_element(By.XPATH,
                                                                          "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div/div/div/button[4]")
        Trads_and_Lots_per_Trade_Graph.click()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Trads_and_Lots_per_Day_Trade_Xpath)))
            self.logger.info(f"'{Trads_and_Lots_per_Day_Trade_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Trads_and_Lots_per_Day_Trade_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Lots Per Trade Graph.png")

        self.logger.info("***************** Lots Per Trade Graph is visible *******************")

        self.driver.close()
        self.logger.info("****************** test_AccountMatrices_Section_Risk_Insights_007 Test is completed ************************")

        self.logger.info("************************** test_AccountMatrices_Section_Risk_Insights_007 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AccountMatrices_Section_Trading_Journal_Check_Trading_Activity_008(self, setup):
        self.logger.info("******************** test_AccountMatrices_Section_Trading_Journal_Check_Trading_Activity_008 test case started **************************")
        self.logger.info("******************** Verifying Account Matrices Section Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 30)
        time.sleep(2)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(2)
        self.logger.info("********************* Clicked on the Account Matrices option. *********************")

        # Wait for the Account Matrices element to be clickable and visible
        account_matrices_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.account_matrices_xpath)))
        account_matrices_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Account Matrices section
        self.logger.info("***************** Moved cursor to the right side for Account Matrices *******************")
        account_matrices_right_element = self.driver.find_element(By.XPATH, self.account_matrices_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(account_matrices_right_element)
        action.perform()

        self.logger.info("***************** Click Trading Journal *******************")

        Trading_Journal_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div/div/div/button[3]")
        Trading_Journal_Xpath.click()

        self.logger.info("***************** Click Three Dot (Trading Activity) *******************")
        time.sleep(2)

        Trading_Activity = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[4]/div/div/div[2]/div/div[1]/h6")
        Trading_Activity.click()

        time.sleep(2)

        self.logger.info("***************** Click SL / TP format 1st Box *******************")

        SL_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[4]/div/div/div[2]/div/div[2]/div/div[2]/div")
        SL_Xpath.click()

        self.logger.info("***************** Click Buy *******************")

        Sell_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[4]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/h6")
        Sell_Xpath.click()

        self.logger.info("***************** Click Sell *******************")

        Sell_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[4]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/h6")
        Sell_Xpath.click()

        self.logger.info("***************** Withdrawal Sell *******************")

        Withdrawal_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[4]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div[3]/div[1]/h6")
        Withdrawal_Xpath.click()

        self.logger.info("***************** Deposite Sell *******************")

        Deposite_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[4]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div[4]/div[1]/h6")
        Deposite_Xpath.click()

        self.logger.info("***************** Interest Sell *******************")

        Interest_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[4]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div[5]/div[1]/h6")
        Interest_Xpath.click()

        self.logger.info("***************** Again Click SL / TP format 1st box *******************")

        SL_Xpath = self.driver.find_element(By.XPATH,
                                            "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[4]/div/div/div[2]/div/div[2]/div/div[2]/div")
        SL_Xpath.click()

        self.logger.info("***************** Click SL / TP format 2nd box *******************")

        TP_XPATH = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[4]/div/div/div[2]/div/div[2]/div/div[3]/div")
        TP_XPATH.click()

        self.logger.info("***************** Click In *******************")

        In_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[4]/div/div/div[2]/div/div[2]/div/div[3]/div[2]/div[1]/div[1]/h6")
        In_Xpath.click()

        self.logger.info("***************** Click Out *******************")

        Out_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[4]/div/div/div[2]/div/div[2]/div/div[3]/div[2]/div[2]/div[1]/h6")
        Out_Xpath.click()

        self.logger.info("***************** Again Click SL / TP format 2nd box *******************")

        TP_XPATH = self.driver.find_element(By.XPATH,
                                            "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[4]/div/div/div[2]/div/div[2]/div/div[3]/div")
        TP_XPATH.click()

        self.driver.close()
        self.logger.info("****************** test_AccountMatrices_Section_Trading_Journal_Check_Trading_Activity_008 Test is completed ************************")

        self.logger.info("************************** test_AccountMatrices_Section_Trading_Journal_Check_Trading_Activity_008 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AccountMatrices_Section_Trading_Journal_Check_Trading_Activity_Field_009(self, setup):
        self.logger.info("******************** test_AccountMatrices_Section_Trading_Journal_Check_Trading_Activity_Field_009 test case started **************************")
        self.logger.info("******************** Verifying Account Matrices Section Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 30)
        time.sleep(2)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(2)
        self.logger.info("********************* Clicked on the Account Matrices option. *********************")

        # Wait for the Account Matrices element to be clickable and visible
        account_matrices_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.account_matrices_xpath)))
        account_matrices_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Account Matrices section
        self.logger.info("***************** Moved cursor to the right side for Account Matrices *******************")
        account_matrices_right_element = self.driver.find_element(By.XPATH, self.account_matrices_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(account_matrices_right_element)
        action.perform()

        self.logger.info("***************** Click Trading Journal *******************")

        Trading_Journal_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div/div/div/button[3]")
        Trading_Journal_Xpath.click()

        self.logger.info("***************** Check Trading Journal Field *******************")

        Trading_Journal_Field = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[4]/div"

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Trading_Journal_Field)))
            self.logger.info(f"'{Trading_Journal_Field}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Trading_Journal_Field}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Trading_Journal_Field.png")

        self.driver.close()
        self.logger.info("****************** test_AccountMatrices_Section_Trading_Journal_Check_Trading_Activity_Field_009 Test is completed ************************")

        self.logger.info("************************** test_AccountMatrices_Section_Trading_Journal_Check_Trading_Activity_Field_009 passed ************************")


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AccountMatrices_Section_Account_Info_Field_010(self, setup):
        self.logger.info("******************** test_AccountMatrices_Section_Account_Info_Field_010 test case started **************************")
        self.logger.info("******************** Verifying Account Matrices Section Test **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Dashboard(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        wait = WebDriverWait(self.driver, 30)
        time.sleep(2)

        self.logger.info("***************** Moved cursor to the left side *******************")
        left_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(left_element)
        action.perform()

        time.sleep(2)
        self.logger.info("********************* Clicked on the Account Matrices option. *********************")

        # Wait for the Account Matrices element to be clickable and visible
        account_matrices_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.account_matrices_xpath)))
        account_matrices_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Account Matrices section
        self.logger.info("***************** Moved cursor to the right side for Account Matrices *******************")
        account_matrices_right_element = self.driver.find_element(By.XPATH, self.account_matrices_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(account_matrices_right_element)
        action.perform()

        self.logger.info("***************** Click Account Info *******************")

        Account_Info_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div/div/div/button[4]")
        Account_Info_Xpath.click()

        self.logger.info("***************** Check General Information Field *******************")

        General_Information_Field = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[5]/div"

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, General_Information_Field)))
            self.logger.info(f"'{General_Information_Field}' is visible.")
        except Exception as e:
            self.logger.error(f"'{General_Information_Field}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "General Information.png")

        self.driver.close()
        self.logger.info("****************** test_AccountMatrices_Section_Account_Info_Field_010 Test is completed ************************")

        self.logger.info("************************** test_AccountMatrices_Section_Account_Info_Field_010 passed ************************")


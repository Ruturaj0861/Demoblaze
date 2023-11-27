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

class Test_AccountAnalysis:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    account_analysis_xpath = "/html/body/div[1]/div/div[1]/div/div/div/ul/li[5]/a/div"
    account_analysis_right_element_xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div"
    logger = LogGenerator.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AccountAnalysis_Section_001(self, setup):
        self.logger.info("******************** Verifying Account Analysis Section Test **************************")
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
        self.logger.info("********************* Clicked on the Account Analysis option. *********************")

        # Wait for the Account Analysis element to be clickable and visible
        account_analysis_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.account_analysis_xpath)))
        account_analysis_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Account Analysis section
        self.logger.info("***************** Moved cursor to the right side for Account Analysis *******************")
        account_analysis_right_element = self.driver.find_element(By.XPATH, self.account_analysis_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(account_analysis_right_element)
        action.perform()

        time.sleep(2)

        # Verify if the page title is "Alpha Capital"
        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Account Analysis Page Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info("Account Analysis Section Test Passed: Page title is as expected.")
        else:
            self.logger.error("Account Analysis Section Test Failed: Page title is not as expected.")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_AccountAnalysis_Section.png")
            assert False

        self.driver.close()
        self.logger.info("****************** Account Analysis Section Test is completed ************************")

        self.logger.info("************************** test_AccountAnalysis_Section_001 passed ************************")


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AccountAnalysis_Section_General_Statistics_Check_field_Avalible_002(self, setup):
        self.logger.info("******************** test_AccountAnalysis_Section_General_Statistics_Check_field_Avalible_002 Test Started **************************")
        self.logger.info("******************** Verifying Account Analysis Section Test **************************")
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
        self.logger.info("********************* Clicked on the Account Analysis option. *********************")

        # Wait for the Account Analysis element to be clickable and visible
        account_analysis_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.account_analysis_xpath)))
        account_analysis_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Account Analysis section
        self.logger.info("***************** Moved cursor to the right side for Account Analysis *******************")
        account_analysis_right_element = self.driver.find_element(By.XPATH, self.account_analysis_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(account_analysis_right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("******************* Check Basic Information Box visible or Not *************************")

        time.sleep(1)

        Basic_Information_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[1]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Basic_Information_Xpath)))
            self.logger.info(f"'{Basic_Information_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Basic_Information_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Basic Information.png")

        self.logger.info("******************* Basic Information Box visible *************************")

        self.logger.info("******************* Check General Statistics Box visible or Not *************************")

        time.sleep(1)

        General_Statistics_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[1]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, General_Statistics_Xpath)))
            self.logger.info(f"'{General_Statistics_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{General_Statistics_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "General Statistics.png")

        self.logger.info("******************* General Statistics Box visible *************************")

        self.logger.info("******************* Check Balance Curve Box visible or Not *************************")

        time.sleep(1)

        Balance_Curve_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[1]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Balance_Curve_Xpath)))
            self.logger.info(f"'{Balance_Curve_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Basic_Information_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Balance Curve.png")

        self.logger.info("******************* Balance Curve Box visible *************************")

        self.logger.info("******************* Check Average profit / Average loss Box visible or Not *************************")

        time.sleep(1)

        Average_profit_Average_loss_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[4]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Average_profit_Average_loss_Xpath)))
            self.logger.info(f"'{Average_profit_Average_loss_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Average_profit_Average_loss_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Average profit / Average profit / Average loss.png")

        self.logger.info("******************* Average profit / Average loss Box visible *************************")

        self.logger.info(
            "******************* Check Final Evaluation Box visible or Not *************************")

        time.sleep(1)

        Final_Evaluation_Box_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[5]/div"

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Final_Evaluation_Box_Xpath)))
            self.logger.info(f"'{Final_Evaluation_Box_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Final_Evaluation_Box_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Final Evaluation Box.png")

        self.logger.info("******************* Final Evaluation Box Box visible *************************")

        self.logger.info("******************* test_AccountAnalysis_Section_General_Statistics_Check_field_Avalible_002 test case Complete *************************")
        self.logger.info("******************* test_AccountAnalysis_Section_General_Statistics_Check_field_Avalible_002 test case Pass *************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AccountAnalysis_Section_Account_Analysis_Check_field_Avalible_003(self, setup):
        self.logger.info("******************** test_AccountAnalysis_Section_Account_Analysis_Check_field_Avalible_003 Test Started **************************")
        self.logger.info("******************** Verifying Account Analysis Section Test **************************")
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
        self.logger.info("********************* Clicked on the Account Analysis option. *********************")

        # Wait for the Account Analysis element to be clickable and visible
        account_analysis_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.account_analysis_xpath)))
        account_analysis_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Account Analysis section
        self.logger.info("***************** Moved cursor to the right side for Account Analysis *******************")
        account_analysis_right_element = self.driver.find_element(By.XPATH, self.account_analysis_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(account_analysis_right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("******************* Click Account Analysis *************************")

        Account_Analysis_Xpath = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div.MainRouter > div > main > div:nth-child(2) > div > div.MuiGrid-root.MuiGrid-container.MuiGrid-item.MuiGrid-spacing-xs-3.MuiGrid-direction-xs-column.MuiGrid-grid-xs-2.MuiGrid-grid-sm-2.MuiGrid-grid-md-3.MuiGrid-grid-lg-3.MuiGrid-grid-xl-2.css-63u3g > div:nth-child(2) > div.d-flex.RadioStat.false > svg > circle")
        Account_Analysis_Xpath.click()


        self.logger.info("******************* Check Long/Short Comparison Box visible or Not *************************")

        time.sleep(1)

        Long_Short_Comparison_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[1]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Long_Short_Comparison_Xpath)))
            self.logger.info(f"'{Long_Short_Comparison_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Long_Short_Comparison_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Long/Short Comparison.png")

        self.logger.info("******************* Long/Short Comparison Box visible *************************")


        self.logger.info("******************* Check Long/Short Box visible or Not *************************")

        time.sleep(1)

        Long_Short_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[2]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Long_Short_Xpath)))
            self.logger.info(f"'{Long_Short_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Long_Short_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Long/Short.png")

        self.logger.info("******************* Long/Short Box visible *************************")

        self.logger.info("******************* Check Long Balance Box visible or Not *************************")

        time.sleep(1)

        Long_Short_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[3]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Long_Short_Xpath)))
            self.logger.info(f"'{Long_Short_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Long_Short_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Long Balance.png")

        self.logger.info("******************* Long Balance Box visible *************************")

        self.logger.info("******************* Check Short Balance Box visible or Not *************************")

        time.sleep(1)

        Short_Balance_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[4]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Short_Balance_Xpath)))
            self.logger.info(f"'{Short_Balance_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Short_Balance_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Short Balance.png")

        self.logger.info("******************* Short Balance Box visible *************************")

        self.logger.info("******************* test_AccountAnalysis_Section_Account_Analysis_Check_field_Avalible_003 test case Complete *************************")
        self.logger.info("******************* test_AccountAnalysis_Section_Account_Analysis_Check_field_Avalible_003 test case Pass *************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AccountAnalysis_Section_Results_by_days_Check_field_Avalible_004(self, setup):
        self.logger.info("******************** test_AccountAnalysis_Section_Results_by_days_Check_field_Avalible_004 Test Started **************************")
        self.logger.info("******************** Verifying Account Analysis Section Test **************************")
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
        self.logger.info("********************* Clicked on the Account Analysis option. *********************")

        # Wait for the Account Analysis element to be clickable and visible
        account_analysis_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.account_analysis_xpath)))
        account_analysis_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Account Analysis section
        self.logger.info("***************** Moved cursor to the right side for Account Analysis *******************")
        account_analysis_right_element = self.driver.find_element(By.XPATH, self.account_analysis_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(account_analysis_right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("******************* Click Results by days *************************")

        Results_by_days_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div[3]/div[2]/div[1]")
        Results_by_days_Xpath.click()


        self.logger.info("******************* Results by close Box visible or Not *************************")

        time.sleep(1)

        Results_by_close_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[1]/div[1]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Results_by_close_Xpath)))
            self.logger.info(f"'{Results_by_days_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Results_by_days_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Results by close.png")

        self.logger.info("******************* Results by close Box visible *************************")

        self.logger.info("******************* Results by Open Box visible or Not *************************")

        time.sleep(1)

        Results_by_Open_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[1]/div[2]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Results_by_Open_Xpath)))
            self.logger.info(f"'{Results_by_days_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Results_by_days_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Results by Open.png")

        self.logger.info("******************* Results by Open Box visible *************************")

        self.logger.info("******************* Results by Days Box visible or Not *************************")

        time.sleep(1)

        Results_by_Days_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[2]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Results_by_Days_Xpath)))
            self.logger.info(f"'{Results_by_days_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Results_by_days_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Results_by_days.png")

        self.logger.info("******************* Results_by_days Box visible *************************")

        self.logger.info("******************* test_AccountAnalysis_Section_Results_by_days_Check_field_Avalible_004 test case Complete *************************")
        self.logger.info("******************* test_AccountAnalysis_Section_Results_by_days_Check_field_Avalible_004 test case Pass *************************")


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Account_Analysis_Section_Long_Short_Comparison_Check_field_Avalible_005(self, setup):
        self.logger.info("******************** test_AccountAnalysis_Section_Long_Short_Comparison_Check_field_Avalible_005 Test Started **************************")
        self.logger.info("******************** Verifying Account Analysis Section Test **************************")
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
        self.logger.info("********************* Clicked on the Account Analysis option. *********************")

        # Wait for the Account Analysis element to be clickable and visible
        account_analysis_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.account_analysis_xpath)))
        account_analysis_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Account Analysis section
        self.logger.info("***************** Moved cursor to the right side for Account Analysis *******************")
        account_analysis_right_element = self.driver.find_element(By.XPATH, self.account_analysis_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(account_analysis_right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("******************* Click Long_Short_Comparison *************************")

        Long_Short_Comparison_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div[3]/div[3]/div[1]")
        Long_Short_Comparison_Xpath.click()


        self.logger.info("******************* Results by Instruments Box visible or Not *************************")

        time.sleep(1)

        Results_by_Instruments_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[1]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Results_by_Instruments_Xpath)))
            self.logger.info(f"'{Results_by_Instruments_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Results_by_Instruments_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Results by Instruments.png")

        self.logger.info("******************* Results by Instruments Box visible *************************")

        self.logger.info("******************* test_AccountAnalysis_Section_Long_Short_Comparison_Check_field_Avalible_005 test case Complete *************************")
        self.logger.info("******************* test_AccountAnalysis_Section_Long_Short_Comparison_Check_field_Avalible_005 test case Pass *************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Account_Analysis_Section_Trading_days_Analysis_Check_field_Avalible_006(self, setup):
        self.logger.info("******************** test_Account_Analysis_Section_Trading_days_Analysis_Check_field_Avalible_006 Test Started **************************")
        self.logger.info("******************** Verifying Account Analysis Section Test **************************")
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
        self.logger.info("********************* Clicked on the Account Analysis option. *********************")

        # Wait for the Account Analysis element to be clickable and visible
        account_analysis_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.account_analysis_xpath)))
        account_analysis_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Account Analysis section
        self.logger.info("***************** Moved cursor to the right side for Account Analysis *******************")
        account_analysis_right_element = self.driver.find_element(By.XPATH, self.account_analysis_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(account_analysis_right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("******************* Click Trading days Analysis *************************")

        Trading_days_Analysis_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div[3]/div[4]/div[1]")
        Trading_days_Analysis_Xpath.click()


        self.logger.info("******************* Average profit / Average loss Box visible or Not *************************")

        time.sleep(1)

        Average_profit_Average_loss = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[2]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Average_profit_Average_loss)))
            self.logger.info(f"'{Average_profit_Average_loss}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Average_profit_Average_loss}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Average_profit_Average_loss.png")

        self.logger.info("******************* Average_profit_Average_loss Box visible *************************")

        self.logger.info("******************* Trading days anaysis Box visible or Not *************************")

        time.sleep(1)

        Trading_days_anaysis = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[1]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Trading_days_anaysis)))
            self.logger.info(f"'{Trading_days_Analysis_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Trading_days_Analysis_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Trading_days_anaysis.png")

        self.logger.info("******************* Trading days anaysis Box visible *************************")

        self.logger.info("******************* test_Account_Analysis_Section_Trading_days_Analysis_Check_field_Avalible_006 test case Complete *************************")
        self.logger.info("******************* test_Account_Analysis_Section_Trading_days_Analysis_Check_field_Avalible_006 test case Pass *************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Account_Analysis_Section_Results_by_Position_size_Check_field_Avalible_007(self, setup):
        self.logger.info("******************** test_Account_Analysis_Section_Results_by_Position_size_Check_field_Avalible_007 Test Started **************************")
        self.logger.info("******************** Verifying Account Analysis Section Test **************************")
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
        self.logger.info("********************* Clicked on the Account Analysis option. *********************")

        # Wait for the Account Analysis element to be clickable and visible
        account_analysis_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.account_analysis_xpath)))
        account_analysis_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Account Analysis section
        self.logger.info("***************** Moved cursor to the right side for Account Analysis *******************")
        account_analysis_right_element = self.driver.find_element(By.XPATH, self.account_analysis_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(account_analysis_right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("******************* Results by Position size Analysis *************************")

        Results_by_Position_size_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div[3]/div[5]/div[1]")
        Results_by_Position_size_Xpath.click()


        self.logger.info("******************* Position profit / loss Box visible or Not *************************")

        time.sleep(1)

        Position_profit_loss_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[1]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Position_profit_loss_Xpath)))
            self.logger.info(f"'{Position_profit_loss_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Position_profit_loss_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Position_profit_loss.png")

        self.logger.info("******************* Position profit / loss Box visible *************************")


        self.logger.info("******************* test_Account_Analysis_Section_Results_by_Position_size_Check_field_Avalible_007 test case Complete *************************")
        self.logger.info("******************* test_Account_Analysis_Section_Results_by_Position_size_Check_field_Avalible_007 test case Pass *************************")


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Account_Analysis_Section_Results_by_Position_size_Check_field_Avalible_007(self, setup):
        self.logger.info("******************** test_Account_Analysis_Section_Results_by_Position_size_Check_field_Avalible_007 Test Started **************************")
        self.logger.info("******************** Verifying Account Analysis Section Test **************************")
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
        self.logger.info("********************* Clicked on the Account Analysis option. *********************")

        # Wait for the Account Analysis element to be clickable and visible
        account_analysis_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.account_analysis_xpath)))
        account_analysis_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Account Analysis section
        self.logger.info("***************** Moved cursor to the right side for Account Analysis *******************")
        account_analysis_right_element = self.driver.find_element(By.XPATH, self.account_analysis_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(account_analysis_right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("******************* Results by Position size Analysis *************************")

        Results_by_Position_size_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div[3]/div[5]/div[1]")
        Results_by_Position_size_Xpath.click()


        self.logger.info("******************* Profit in durations Box visible or Not *************************")

        time.sleep(1)

        Profit_in_durations_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[1]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Profit_in_durations_Xpath)))
            self.logger.info(f"'{Profit_in_durations_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Profit_in_durations_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Profit in durations.png")

        self.logger.info("******************* Profit in durations Box visible *************************")

        self.logger.info("******************* Results by Trade Duration Box visible or Not *************************")

        time.sleep(1)

        Results_by_Trade_Duration_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[2]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Results_by_Trade_Duration_Xpath)))
            self.logger.info(f"'{Results_by_Trade_Duration_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Results_by_Trade_Duration_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Results_by_Trade_Duration.png")

        self.logger.info("******************* Results_by_Trade_Duration Box visible *************************")

        self.logger.info("******************* test_Account_Analysis_Section_Results_by_Position_size_Check_field_Avalible_007 test case Complete *************************")
        self.logger.info("******************* test_Account_Analysis_Section_Results_by_Position_size_Check_field_Avalible_007 test case Pass *************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Account_Analysis_Section_Results_by_Open_Hour_Check_field_Avalible_008(self, setup):
        self.logger.info("******************** test_Account_Analysis_Section_Results_by_Open_Hour_Check_field_Avalible_008 Test Started **************************")
        self.logger.info("******************** Verifying Account Analysis Section Test **************************")
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
        self.logger.info("********************* Clicked on the Account Analysis option. *********************")

        # Wait for the Account Analysis element to be clickable and visible
        account_analysis_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.account_analysis_xpath)))
        account_analysis_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side for the Account Analysis section
        self.logger.info("***************** Moved cursor to the right side for Account Analysis *******************")
        account_analysis_right_element = self.driver.find_element(By.XPATH, self.account_analysis_right_element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(account_analysis_right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("******************* click Results by Open Hour *************************")

        Results_by_Open_Hour_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div[3]/div[7]/div[1]")
        Results_by_Open_Hour_Xpath.click()


        self.logger.info("******************* Profits by Open hour Box visible or Not *************************")

        time.sleep(1)

        Profits_by_Open_hour_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[1]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Profits_by_Open_hour_Xpath)))
            self.logger.info(f"'{Profits_by_Open_hour_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Profits_by_Open_hour_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Profits by Open hour.png")

        self.logger.info("******************* Profits by Open hour Box visible *************************")

        self.logger.info("******************* Results by Open Hour Box visible or Not *************************")

        time.sleep(1)

        Results_by_Open_Hour_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div/div[2]/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Results_by_Open_Hour_Xpath)))
            self.logger.info(f"'{Results_by_Open_Hour_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Results_by_Open_Hour_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Results by Open Hour.png")

        self.logger.info("******************* Results by Open Hour Box visible *************************")

        self.logger.info("******************* test_Account_Analysis_Section_Results_by_Open_Hour_Check_field_Avalible_008 test case Complete *************************")
        self.logger.info("******************* test_Account_Analysis_Section_Results_by_Open_Hour_Check_field_Avalible_008 test case Pass *************************")
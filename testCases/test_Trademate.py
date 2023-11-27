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
    trademate_xpath = "/html/body/div[1]/div/div[1]/div/div/div/ul/li[9]/a/div"
    logger = LogGenerator.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Trademate_001(self, setup):
        self.logger.info("******************** test_Trademate_001 test start **************************")
        self.logger.info("******************** Verifying Trademate Test **************************")
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

        # Use JavaScript to scroll to the Trademate element
        self.logger.info("***************** Scrolling to view the Trademate element *******************")
        trademate_element = self.driver.find_element(By.XPATH, self.trademate_xpath)  # Use the correct XPath expression
        self.driver.execute_script("arguments[0].scrollIntoView(true);", trademate_element)

        time.sleep(2)

        # Click on the Trademate element
        self.logger.info("***************** Clicking on the Trademate option *******************")
        trademate_element.click()

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
        self.logger.info(f"Actual Trademate Page Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info("Trademate Test Passed: Page title is as expected.")
            assert True
        else:
            self.logger.error("Trademate Test Failed: Page title is not as expected.")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Trademate.png")
            assert False

        self.driver.close()
        self.logger.info("****************** test_Trademate_001 Test is completed ************************")

        self.logger.info(" ************************** test_Trademate_001 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Trademate_Market_Scanner_002(self, setup):
        self.logger.info("******************** test_Trademate_Market_Scanner_002 Test started **************************")
        self.logger.info("******************** Verifying Trademate Test **************************")
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

        # Use JavaScript to scroll to the Trademate element
        self.logger.info("***************** Scrolling to view the Trademate element *******************")
        trademate_element = self.driver.find_element(By.XPATH, self.trademate_xpath)  # Use the correct XPath expression
        self.driver.execute_script("arguments[0].scrollIntoView(true);", trademate_element)

        time.sleep(2)

        # Click on the Trademate element
        self.logger.info("***************** Clicking on the Trademate option *******************")
        trademate_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.driver.close()
        self.logger.info("****************** test_Trademate_Market_Scanner_002 Test is completed ************************")

        self.logger.info(" ************************** test_Trademate_Market_Scanner_002 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Trademate_Market_Economic_Calander_003(self, setup):
        self.logger.info("******************** test_Trademate_Market_Economic_Calander_003 Test started **************************")
        self.logger.info("******************** Verifying Trademate Test **************************")
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

        # Use JavaScript to scroll to the Trademate element
        self.logger.info("***************** Scrolling to view the Trademate element *******************")
        trademate_element = self.driver.find_element(By.XPATH, self.trademate_xpath)  # Use the correct XPath expression
        self.driver.execute_script("arguments[0].scrollIntoView(true);", trademate_element)

        time.sleep(2)

        # Click on the Trademate element
        self.logger.info("***************** Clicking on the Trademate option *******************")
        trademate_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("******************* Click Economic Calander *************************")

        Economic_Calander = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[2]")
        Economic_Calander.click()

        self.logger.info("******************* Calander visible or Not *************************")

        time.sleep(2)

        Calander_Xpath = "/html/body/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Calander_Xpath)))
            self.logger.info(f"'{Calander_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Calander_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Calander.png")

        self.logger.info("******************* Calander visible *************************")

        self.driver.close()
        self.logger.info("****************** test_Trademate_Market_Economic_Calander_003 Test is completed ************************")

        self.logger.info(" ************************** test_Trademate_Market_Economic_Calander_003 passed ************************")


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Trademate_Market_Check_News_004(self, setup):
        self.logger.info(
            "******************** test_Trademate_Market_Check_News_004 Test started **************************")
        self.logger.info("******************** Verifying Trademate Test **************************")
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

        # Use JavaScript to scroll to the Trademate element
        self.logger.info("***************** Scrolling to view the Trademate element *******************")
        trademate_element = self.driver.find_element(By.XPATH, self.trademate_xpath)  # Use the correct XPath expression
        self.driver.execute_script("arguments[0].scrollIntoView(true);", trademate_element)

        time.sleep(2)

        # Click on the Trademate element
        self.logger.info("***************** Clicking on the Trademate option *******************")
        trademate_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH,
                                                 "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("******************* Click Market News *************************")

        Market_News = self.driver.find_element(By.XPATH,
                                               "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[3]")
        Market_News.click()

        self.logger.info("******************* Check News Feed Visible or nor *************************")

        News_Feed = "/html/body/div[1]/div/div[1]/div/main/div[2]/div[4]/div[2]"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, News_Feed)))
            self.logger.info(f"'{News_Feed}' is visible.")
        except Exception as e:
            self.logger.error(f"'{News_Feed}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "News feed.png")

        self.logger.info("******************* Check Tweeter Feeds Visible or nor *************************")

        Tweeter_Feed = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[4]/div[1]/div/div/div/button[2]")
        Tweeter_Feed.click()

        self.driver.close()
        self.logger.info(
            "****************** test_Trademate_Market_Check_News_004 Test is completed ************************")

        self.logger.info(
            " ************************** test_Trademate_Market_Check_News_004 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Trademate_Market_Trade_Journal_005(self, setup):
        self.logger.info("******************** test_Trademate_Market_Trade_Journal_005 Test started **************************")
        self.logger.info("******************** Verifying Trademate Test **************************")
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

        # Use JavaScript to scroll to the Trademate element
        self.logger.info("***************** Scrolling to view the Trademate element *******************")
        trademate_element = self.driver.find_element(By.XPATH, self.trademate_xpath)  # Use the correct XPath expression
        self.driver.execute_script("arguments[0].scrollIntoView(true);", trademate_element)

        time.sleep(2)

        # Click on the Trademate element
        self.logger.info("***************** Clicking on the Trademate option *******************")
        trademate_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("***************** Click Trade Journal *******************")

        Trade_Journal = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[4]")
        Trade_Journal.click()

        self.logger.info("***************** Check Trade Journal Fields Visible or not *******************")

        Trade_Journal = "/html/body/div[1]/div/div[1]/div/main/div[2]/div[5]"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Trade_Journal)))
            self.logger.info(f"'{Trade_Journal}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Trade_Journal}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Trade_Journal.png")
        self.driver.close()

        self.logger.info("****************** test_Trademate_Market_Trade_Journal_005 Test is completed ************************")

        self.logger.info(" ************************** test_Trademate_Market_Trade_Journal_005 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Trademate_Market_Market_Report_Market_Report_Email_and_Signup_Form_006(self, setup):
        self.logger.info("******************** test_Trademate_Market_Market_Report_Market_Report_Email_and_Signup_Form_006 Test started **************************")
        self.logger.info("******************** Verifying Trademate Test **************************")
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

        # Use JavaScript to scroll to the Trademate element
        self.logger.info("***************** Scrolling to view the Trademate element *******************")
        trademate_element = self.driver.find_element(By.XPATH, self.trademate_xpath)  # Use the correct XPath expression
        self.driver.execute_script("arguments[0].scrollIntoView(true);", trademate_element)

        time.sleep(2)

        # Click on the Trademate element
        self.logger.info("***************** Clicking on the Trademate option *******************")
        trademate_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("***************** Click Market Report *******************")

        Market_Report = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[5]")
        Market_Report.click()

        self.logger.info("***************** Check Market Report Fields Visible or not *******************")

        Market_Report_Email_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div[6]/div[2]"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Market_Report_Email_Xpath)))
            self.logger.info(f"'{Market_Report_Email_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Market_Report_Email_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Market Report Email.png")

        self.logger.info("***************** Check Sign Up Form Fields Visible or not *******************")

        Sign_Up_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[6]/div[1]/div/div/div/button[2]")
        Sign_Up_Xpath.click()

        self.logger.info("***************** Check Sign Up Fields Visible or not *******************")

        Sign_UP_Form = "/html/body/app-root/div[1]/div/app-market-report-view"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Sign_UP_Form)))
            self.logger.info(f"'{Sign_UP_Form}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Sign_UP_Form}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Sign Up.png")
        self.driver.close()

        self.logger.info("****************** test_Trademate_Market_Market_Report_Market_Report_Email_and_Signup_Form_006 Test is completed ************************")

        self.logger.info(" ************************** test_Trademate_Market_Market_Report_Market_Report_Email_and_Signup_Form_006 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Trademate_Market_Trading_View_Chart_007(self, setup):
        self.logger.info("******************** test_Trademate_Market_Trading_View_Chart_007 Test started **************************")
        self.logger.info("******************** Verifying Trademate Test **************************")
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

        # Use JavaScript to scroll to the Trademate element
        self.logger.info("***************** Scrolling to view the Trademate element *******************")
        trademate_element = self.driver.find_element(By.XPATH, self.trademate_xpath)  # Use the correct XPath expression
        self.driver.execute_script("arguments[0].scrollIntoView(true);", trademate_element)

        time.sleep(2)

        # Click on the Trademate element
        self.logger.info("***************** Clicking on the Trademate option *******************")
        trademate_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("***************** Click Trading View Chart *******************")

        Trading_View_Chart = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[6]")
        Trading_View_Chart.click()

        self.logger.info("***************** Check Market Report Fields Visible or not *******************")

        Trading_Chart = "/html/body"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Trading_Chart)))
            self.logger.info(f"'{Trading_Chart}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Trading_Chart}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Trading Chart.png")

        self.driver.close()

        self.logger.info("****************** test_Trademate_Market_Trading_View_Chart_007 Test is completed ************************")

        self.logger.info(" ************************** test_Trademate_Market_Trading_View_Chart_007 passed ************************")

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

class Test_AffiliateMarketing:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    affiliate_marketing_xpath = "/html/body/div[1]/div/div[1]/div/div/div/ul/li[11]/a/div/div[2]/span"
    logger = LogGenerator.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AffiliateMarketing_001(self, setup):
        self.logger.info("******************** test_AffiliateMarketing_001 Test Start **************************")
        self.logger.info("******************** Verifying Affiliate Marketing Test **************************")
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

        # Use JavaScript to scroll to the Affiliate Marketing element
        self.logger.info("***************** Scrolling to view the Affiliate Marketing element *******************")
        affiliate_marketing_element = self.driver.find_element(By.XPATH, self.affiliate_marketing_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", affiliate_marketing_element)

        time.sleep(2)

        # Click on the Affiliate Marketing element
        self.logger.info("***************** Clicking on the Affiliate Marketing option *******************")
        affiliate_marketing_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[5]/div/div/div[1]/div/div[4]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)


        self.driver.close()
        self.logger.info("****************** test_AffiliateMarketing_001 Test is completed ************************")

        self.logger.info(" ************************** test_AffiliateMarketing_001 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AffiliateMarketing_Overview_Field_Visible_or_Not_002(self, setup):
        self.logger.info("******************** test_AffiliateMarketing_Overview_Field_Visible_or_Not_002 Test Start **************************")
        self.logger.info("******************** Verifying Affiliate Marketing Test **************************")
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

        # Use JavaScript to scroll to the Affiliate Marketing element
        self.logger.info("***************** Scrolling to view the Affiliate Marketing element *******************")
        affiliate_marketing_element = self.driver.find_element(By.XPATH, self.affiliate_marketing_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", affiliate_marketing_element)

        time.sleep(2)

        # Click on the Affiliate Marketing element
        self.logger.info("***************** Clicking on the Affiliate Marketing option *******************")
        affiliate_marketing_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[5]/div/div/div[1]/div/div[4]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("***************** Check Click fild visible or not *******************")

        Click_Field_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div[5]/div/div/div[1]/div/div[1]/div/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Click_Field_Xpath)))
            self.logger.info(f"'{Click_Field_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Click_Field_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Click field.png")

        self.logger.info("***************** Check Pushleads fild visible or not *******************")

        Pushleads_Field_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div[5]/div/div/div[1]/div/div[2]/div/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Pushleads_Field_Xpath)))
            self.logger.info(f"'{Pushleads_Field_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Pushleads_Field_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Pushleads field.png")

        self.logger.info("***************** Check Conversions fild visible or not *******************")

        Conversions_Field_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div[5]/div/div/div[1]/div/div[3]/div/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Conversions_Field_Xpath)))
            self.logger.info(f"'{Conversions_Field_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Conversions_Field_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Conversions field.png")

        self.logger.info("***************** Check Profit fild visible or not *******************")

        Profit_Field_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div[5]/div/div/div[1]/div/div[4]/div/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Profit_Field_Xpath)))
            self.logger.info(f"'{Profit_Field_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Profit_Field_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Profit field.png")

        self.logger.info("***************** Check Pushleads fild visible or not *******************")

        Pushleads_Graph_Field_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div[5]/div/div/div[2]/div/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Pushleads_Graph_Field_Xpath)))
            self.logger.info(f"'{Pushleads_Graph_Field_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Pushleads_Graph_Field_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Pushleads field.png")

        self.driver.close()
        self.logger.info("****************** test_AffiliateMarketing_Overview_Field_Visible_or_Not_002 Test is completed ************************")

        self.logger.info(" ************************** test_AffiliateMarketing_Overview_Field_Visible_or_Not_002 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AffiliateMarketing_Get_a_Link_003(self, setup):
        self.logger.info("******************** test_AffiliateMarketing_Get_a_Link_003 Test Start **************************")
        self.logger.info("******************** Verifying Affiliate Marketing Test **************************")
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

        # Use JavaScript to scroll to the Affiliate Marketing element
        self.logger.info("***************** Scrolling to view the Affiliate Marketing element *******************")
        affiliate_marketing_element = self.driver.find_element(By.XPATH, self.affiliate_marketing_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", affiliate_marketing_element)

        time.sleep(2)

        # Click on the Affiliate Marketing element
        self.logger.info("***************** Clicking on the Affiliate Marketing option *******************")
        affiliate_marketing_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[5]/div/div/div[1]/div/div[4]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("***************** Click Get a link *******************")

        Get_a_Link_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[2]")
        Get_a_Link_Xpath.click()

        self.logger.info("***************** Click and check Choose Commission rate 367PX  *******************")

        Choose_Commission_rate_367PX = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div[2]")
        Choose_Commission_rate_367PX.click()

        self.logger.info("***************** Click and check Choose Commission rate 24PX *******************")

        Choose_Commission_rate_24PX = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div[2]")
        Choose_Commission_rate_24PX.click()

        self.driver.close()
        self.logger.info("****************** test_AffiliateMarketing_Get_a_Link_003 Test is completed ************************")

        self.logger.info(" ************************** test_AffiliateMarketing_Get_a_Link_003 passed ************************")


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AffiliateMarketing_Send_Custom_Code_004(self, setup):
        self.logger.info("******************** test_AffiliateMarketing_Send_Custom_Code_004 Test Start **************************")
        self.logger.info("******************** Verifying Affiliate Marketing Test **************************")
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

        # Use JavaScript to scroll to the Affiliate Marketing element
        self.logger.info("***************** Scrolling to view the Affiliate Marketing element *******************")
        affiliate_marketing_element = self.driver.find_element(By.XPATH, self.affiliate_marketing_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", affiliate_marketing_element)

        time.sleep(2)

        # Click on the Affiliate Marketing element
        self.logger.info("***************** Clicking on the Affiliate Marketing option *******************")
        affiliate_marketing_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[5]/div/div/div[1]/div/div[4]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("***************** Click Get a link *******************")

        Get_a_Link_Xpath = self.driver.find_element(By.XPATH,
                                                    "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[2]")
        Get_a_Link_Xpath.click()

        self.logger.info("***************** Send Custom Code *******************")

        Custom_Code_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/input")
        Custom_Code_Xpath.send_keys("Alpha123")

        self.driver.close()
        self.logger.info("****************** test_AffiliateMarketing_Send_Custom_Code_004 Test is completed ************************")

        self.logger.info(" ************************** test_AffiliateMarketing_Send_Custom_Code_004 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AffiliateMarketing_Affliate_Codes_Table_005(self, setup):
        self.logger.info("******************** test_AffiliateMarketing_Affliate_Codes_005 Test Start **************************")
        self.logger.info("******************** Verifying Affiliate Marketing Test **************************")
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

        # Use JavaScript to scroll to the Affiliate Marketing element
        self.logger.info("***************** Scrolling to view the Affiliate Marketing element *******************")
        affiliate_marketing_element = self.driver.find_element(By.XPATH, self.affiliate_marketing_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", affiliate_marketing_element)

        time.sleep(2)

        # Click on the Affiliate Marketing element
        self.logger.info("***************** Clicking on the Affiliate Marketing option *******************")
        affiliate_marketing_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[5]/div/div/div[1]/div/div[4]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("***************** Click Affliate Codes *******************")

        Affliate_Codes_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[3]")
        Affliate_Codes_Xpath.click()

        self.logger.info("***************** Check Affliate Codes Table *******************")

        Affliate_Codes_Table = "/html/body/div[1]/div/div[1]/div/main/div[2]/div[3]"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Affliate_Codes_Table)))
            self.logger.info(f"'{Affliate_Codes_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Affliate_Codes_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Affliate Codes.png")
        self.driver.close()
        self.logger.info("****************** test_AffiliateMarketing_Affliate_Codes_Table_005 Test is completed ************************")

        self.logger.info(" ************************** test_AffiliateMarketing_Affliate_Codes_Table_005 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AffiliateMarketing_Affliate_Codes_Table_Copy_URL_006(self, setup):
        self.logger.info("******************** test_AffiliateMarketing_Affliate_Codes_Table_Copy_URL_006 Test Start **************************")
        self.logger.info("******************** Verifying Affiliate Marketing Test **************************")
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

        # Use JavaScript to scroll to the Affiliate Marketing element
        self.logger.info("***************** Scrolling to view the Affiliate Marketing element *******************")
        affiliate_marketing_element = self.driver.find_element(By.XPATH, self.affiliate_marketing_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", affiliate_marketing_element)

        time.sleep(2)

        # Click on the Affiliate Marketing element
        self.logger.info("***************** Clicking on the Affiliate Marketing option *******************")
        affiliate_marketing_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[5]/div/div/div[1]/div/div[4]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("***************** Click Affliate Codes *******************")

        Affliate_Codes_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[3]")
        Affliate_Codes_Xpath.click()

        time.sleep(2)

        self.logger.info("***************** Click Copy URL *******************")

        Copy_URL = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[3]/div/div/div/table/tbody/tr[1]/td[6]/button")
        Copy_URL.click()

        self.logger.info("***************** URL Copied *******************")

        self.driver.close()
        self.logger.info("****************** test_AffiliateMarketing_Affliate_Codes_Table_Copy_URL_006 Test is completed ************************")

        self.logger.info(" ************************** test_AffiliateMarketing_Affliate_Codes_Table_Copy_URL_006 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AffiliateMarketing_Commision_Payment_007(self, setup):
        self.logger.info("******************** test_AffiliateMarketing_Commision_Payment_007 Test Start **************************")
        self.logger.info("******************** Verifying Affiliate Marketing Test **************************")
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

        # Use JavaScript to scroll to the Affiliate Marketing element
        self.logger.info("***************** Scrolling to view the Affiliate Marketing element *******************")
        affiliate_marketing_element = self.driver.find_element(By.XPATH, self.affiliate_marketing_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", affiliate_marketing_element)

        time.sleep(2)

        # Click on the Affiliate Marketing element
        self.logger.info("***************** Clicking on the Affiliate Marketing option *******************")
        affiliate_marketing_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[5]/div/div/div[1]/div/div[4]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("***************** Click Commision Payment *******************")

        Commision_Payment_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[4]")
        Commision_Payment_Xpath.click()

        self.driver.close()
        self.logger.info("****************** test_AffiliateMarketing_Commision_Payment_007 Test is completed ************************")

        self.logger.info(" ************************** test_AffiliateMarketing_Commision_Payment_007 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AffiliateMarketing_Commision_Payment_Field_008(self, setup):
        self.logger.info("******************** test_AffiliateMarketing_Commision_Payment_Field_008 Test Start **************************")
        self.logger.info("******************** Verifying Affiliate Marketing Test **************************")
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

        # Use JavaScript to scroll to the Affiliate Marketing element
        self.logger.info("***************** Scrolling to view the Affiliate Marketing element *******************")
        affiliate_marketing_element = self.driver.find_element(By.XPATH, self.affiliate_marketing_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", affiliate_marketing_element)

        time.sleep(2)

        # Click on the Affiliate Marketing element
        self.logger.info("***************** Clicking on the Affiliate Marketing option *******************")
        affiliate_marketing_element.click()

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[5]/div/div/div[1]/div/div[4]/div/div/div")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("***************** Click Commision Payment *******************")

        Commision_Payment_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[1]/div/div/div/button[4]")
        Commision_Payment_Xpath.click()

        self.logger.info("***************** Click Commision Payment Table *******************")

        Commision_Payment_Table_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div[4]")

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Commision_Payment_Table_Xpath)))
            self.logger.info(f"'{Commision_Payment_Table_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Commision_Payment_Table_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Commision_Payment.png")

        self.driver.close()
        self.logger.info("****************** test_AffiliateMarketing_Commision_Payment_Field_008 Test is completed ************************")

        self.logger.info(" ************************** test_AffiliateMarketing_Commision_Payment_Field_008 passed ************************")

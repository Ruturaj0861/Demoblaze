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

class Test_Profile:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    profile_xpath = "/html/body/div[1]/div/div[1]/div/div/div/ul/li[2]/a/div/div[2]/span"  # XPath for the profile section
    logger = LogGenerator.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Profile_Section_001(self, setup):
        self.logger.info("******************** test_Profile_Section_008 Test case Started **************************")
        self.logger.info("******************** Verifying Profile Section Test **************************")
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
        self.logger.info("********************* Clicked on the Profile option. *********************")
        profile_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.profile_xpath)))
        profile_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        # Verify if the page title is "Alpha Capital"
        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Profile Page Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info("Profile Section Test Passed: Page title is as expected.")
            assert True
        else:
            self.logger.error("Profile Section Test Failed: Page title is not as expected.")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Profile_Section.png")
            assert False

        self.driver.close()
        self.logger.info("****************** Profile Section Test is completed ************************")

        self.logger.info(" ************************** test_Profile_Section_008 passed ************************")


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_General_Information_002(self, setup):
        self.logger.info("******************** test_General_Information_009 Test case Started **************************")
        self.logger.info("******************** Verifying Profile Section Test **************************")
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
        self.logger.info("********************* Clicked on the Profile option. *********************")
        profile_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.profile_xpath)))
        profile_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        time.sleep(2)

        self.logger.info("***************** Check My profile Box *******************")
        self.logger.info("***************** Verify First Name sending or not *******************")

        First_Name = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div[1]/form/div[1]/div/input")

        self.logger.info("***************** Clear the First Name textbox *******************")

        First_Name.clear()

        self.logger.info("***************** Send First Name textbox *******************")

        First_Name.send_keys("Testuser")

        self.logger.info("***************** Verify Last Name sending or not *******************")

        Last_Name = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div[1]/form/div[2]/div/input")

        self.logger.info("***************** Clear the Last Name textbox *******************")

        Last_Name.clear()

        self.logger.info("***************** Send Last Name textbox *******************")

        Last_Name.send_keys("1234")

        self.logger.info("***************** clear Contact Number textbox *******************")

        Contact_No = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div[1]/form/div[3]/div/div/input")

        Contact_No.clear()

        self.logger.info("***************** send Contact Number textbox *******************")

        Contact_No.send_keys("1857839478")

        self.logger.info("***************** Clear City textbox *******************")

        city = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div[1]/form/div[6]/div/input")

        city.clear()

        self.logger.info("***************** Send City textbox *******************")

        city.send_keys("Bengaluru")

        time.sleep(2)

        self.logger.info("******************* check Country Dropdown visible *************************")

        Country_Dropdown_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div[1]/form/div[5]/div/div/div"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Country_Dropdown_Xpath)))
            self.logger.info(f"'{Country_Dropdown_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{Country_Dropdown_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Country dropdown.png")

        self.logger.info("******************* check Save Changes Button visible *************************")

        save_changes_Xpath = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div[1]/form/div[7]/button"

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, save_changes_Xpath)))
            self.logger.info(f"'{save_changes_Xpath}' is visible.")
        except Exception as e:
            self.logger.error(f"'{save_changes_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "Save changes.png")

        self.logger.info("***************** Check Password Box *******************")

        self.logger.info("***************** Verify current password send or not *******************")

        Current_Password_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div[2]/form/div[1]/div/div/input")
        Current_Password_Xpath.send_keys("Password@1234")

        self.logger.info("***************** Verify New password send or not *******************")

        New_password_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div/input")
        New_password_Xpath.send_keys("Password@1234")

        self.logger.info("***************** Verify Verify password send or not *******************")

        Verify_password = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/div/input")
        Verify_password.send_keys("Password@1234")

        self.logger.info("***************** Check Account Setting *******************")

        self.logger.info("******************* check Username textbox visible *************************")

        username_textbox_Clss = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div[3]/form/div[1]/div/input"

        try:
            WebDriverWait(self.driver, 10).until(EC.username_textbox_Xpath((By.CLASS_NAME, username_textbox_Clss)))
            self.logger.info(f"'{username_textbox_Clss}' is visible.")
        except Exception as e:
            self.logger.error(f"'{save_changes_Xpath}' is not visible. Screenshot Added")
            self.driver.save_screenshot(".\\Screenshots\\" + "username.png")

        self.logger.info("********************* Scroll Language *********************")

        Language_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div[3]/form/div[2]/div/div/div")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Language_button)

        self.logger.info("********************* Click Language *********************")

        time.sleep(2)

        Language_button.click()


        self.logger.info("********************* France Language Select *********************")

        Franch_Xpath = "#menu- > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation1.MuiPaper-root.MuiMenu-paper.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-zzhupx > ul > li.MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.Mui-selected.css-1bo1rz0"

        # Wait for the element to be clickable
        French_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Franch_Xpath))
        )

        French_element.click()

        self.logger.info("********************* Spanish Language Select *********************")

        Spanish_Xpath = "#menu- > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation1.MuiPaper-root.MuiMenu-paper.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-zzhupx > ul > li.MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.Mui-selected.css-1bo1rz0"

        Spanish_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Spanish_Xpath))
        )

        Spanish_element.click()

        self.logger.info("********************* Click Time Zone *********************")

        Time_Zone_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[2]/div[3]/form/div[3]/div/div/div")
        Time_Zone_Xpath.click()

        self.logger.info("********************* Select IST Time Zone *********************")

        IST_Xpath = "#menu- > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation1.MuiPaper-root.MuiMenu-paper.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-zzhupx > ul > li.MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.Mui-selected.css-1bo1rz0"

        IST_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, IST_Xpath))
        )

        IST_element.click()

        self.logger.info("********************* test_General_Information_009 test case passed........... *********************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Profile_Section_Verification_003(self, setup):
        self.logger.info("******************** test_Profile_Section_Verification_010 Test case Started **************************")
        self.logger.info("******************** Verifying Profile Section Test **************************")
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
        self.logger.info("********************* Clicked on the Profile option. *********************")
        profile_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.profile_xpath)))
        profile_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        self.logger.info("***************** Click on Verification *******************")


        Verification_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div/div/div/button[2]")
        Verification_Xpath.click()

        self.logger.info("***************** Clicked on Verification *******************")


        time.sleep(2)

        # Verify if the page title is "Alpha Capital"
        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Verification Page Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info("Profile Section Verification Test Passed: Page title is as expected.")
            assert True
        else:
            self.logger.error("Profile Section Verification Test Failed: Page title is not as expected.")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Profile_Section_Verification_003.png")
            assert False

        self.driver.close()
        self.logger.info("****************** test_Profile_Section_Verification_010 Test is completed ************************")

        self.logger.info(" ************************** test_Profile_Section_Verification_010 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Profile_Section_Payout_004(self, setup):
        self.logger.info("******************** test_Profile_Section_Payout_011 Test case Started **************************")
        self.logger.info("******************** Verifying Profile Section Test **************************")
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
        self.logger.info("********************* Clicked on the Profile option. *********************")
        profile_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.profile_xpath)))
        profile_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        self.logger.info("***************** Click on Payout *******************")


        Payout_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div/div/div/button[3]")
        Payout_Xpath.click()

        self.logger.info("***************** Clicked on Payout *******************")


        time.sleep(2)

        # Verify if the page title is "Alpha Capital"
        expected_title = "Alpha Capital"
        actual_title = self.driver.title
        self.logger.info(f"Actual Payout Page Title: {actual_title}")

        if actual_title == expected_title:
            self.logger.info("Profile Section Payout Test Passed: Page title is as expected.")
            assert True
        else:
            self.logger.error("Profile Section Payout Test Failed: Page title is not as expected.")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Profile_Section_Payout_004.png")
            assert False

        self.driver.close()
        self.logger.info("****************** test_Profile_Section_Payout_004 Test is completed ************************")

        self.logger.info(" ************************** test_Profile_Section_Payout_011 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Profile_payout_Section_Request_Payout_For_Trading_Account_005(self, setup):
        self.logger.info("******************** test_Profile_payout_Section_Request_Payout_For_Trading_Account_012 Test case Started **************************")
        self.logger.info("******************** Verifying Profile Section Test **************************")
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
        self.logger.info("********************* Clicked on the Profile option. *********************")
        profile_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.profile_xpath)))
        profile_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        self.logger.info("***************** Click to Payout *******************")

        payout_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div/div/div/button[3]")
        payout_Xpath.click()

        time.sleep(2)

        self.logger.info("***************** Click to Request Payout *******************")

        Request_Payout_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[5]/div[2]/div/div/div/div[2]/button")
        Request_Payout_Xpath.click()

        time.sleep(2)

        self.logger.info("***************** Send Withdraw Amount *******************")

        Withdraw_Amount_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[5]/div/div[3]/div/div/div/div/div[2]/div/div[5]/div/input")


        self.driver.execute_script("arguments[0].scrollIntoView(true);", Withdraw_Amount_Xpath)

        Withdraw_Amount_Xpath.send_keys("31232312")

        self.logger.info("***************** Send Reason *******************")

        Reason = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[5]/div/div[3]/div/div/div/div/div[2]/div/div[6]/div/div/div/textarea[1]")

        self.driver.execute_script("arguments[0].scrollIntoView(true);", Reason)

        Reason.send_keys("XYZ")

        time.sleep(2)

        self.driver.close()

        self.logger.info("****************** test_Profile_payout_Section_Request_Payout_For_Trading_Account_012 Test is completed ************************")

        self.logger.info(" ************************** test_Profile_payout_Section_Request_Payout_For_Trading_Account_012 passed ************************")


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Profile_payout_Section_Request_Payout_For_Afiliate_006(self, setup):
        self.logger.info("******************** test_Profile_payout_Section_Request_Payout_For_Afiliate_013 Test case Started **************************")
        self.logger.info("******************** Verifying Profile Section Test **************************")
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
        self.logger.info("********************* Clicked on the Profile option. *********************")
        profile_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.profile_xpath)))
        profile_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        self.logger.info("***************** Click to Payout *******************")

        payout_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div/div/div/button[3]")
        payout_Xpath.click()

        time.sleep(2)

        self.logger.info("***************** Click to Request Payout *******************")

        Request_Payout_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[5]/div[2]/div/div/div/div[2]/button")
        Request_Payout_Xpath.click()

        time.sleep(2)

        self.logger.info("***************** Click to Afiliate *******************")

        Afiliate = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[5]/div/div[3]/div/div/div/div/div[1]/div/div/div/button[2]")
        Afiliate.click()

        time.sleep(2)

        self.logger.info("***************** Send Withdraw Amount *******************")

        Withdraw_Amount_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[5]/div/div[3]/div/div/div/div/div[3]/div/div[1]/div/input")


        self.driver.execute_script("arguments[0].scrollIntoView(true);", Withdraw_Amount_Xpath)

        Withdraw_Amount_Xpath.send_keys("31232312")

        self.logger.info("***************** Send Reason *******************")

        Reason = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[5]/div/div[3]/div/div/div/div/div[3]/div/div[3]/div/div/div/textarea[1]")

        self.driver.execute_script("arguments[0].scrollIntoView(true);", Reason)

        Reason.send_keys("XYZ")

        time.sleep(2)

        self.driver.close()

        self.logger.info("****************** test_Profile_payout_Section_Request_Payout_For_Afiliate_013 Test is completed ************************")

        self.logger.info(" ************************** test_Profile_payout_Section_Request_Payout_For_Afiliate_013 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Profile_payout_Section_Back_Button_007(self, setup):
        self.logger.info("******************** test_Profile_payout_Section_Back_Button_014 Test case Started **************************")
        self.logger.info("******************** Verifying Profile Section Test **************************")
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
        self.logger.info("********************* Clicked on the Profile option. *********************")
        profile_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.profile_xpath)))
        profile_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        self.logger.info("***************** Click to Payout *******************")

        payout_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div/div/div/button[3]")
        payout_Xpath.click()

        time.sleep(2)

        self.logger.info("***************** Click to Request Payout *******************")

        Request_Payout_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[5]/div[2]/div/div/div/div[2]/button")
        Request_Payout_Xpath.click()

        time.sleep(2)

        self.logger.info("***************** Click to Back to Payout (for back button working or not) *******************")

        Back_button_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[5]/div/div[2]/p/img")
        Back_button_Xpath.click()


        self.driver.close()

        self.logger.info("****************** test_Profile_payout_Section_Back_Button_014 Test is completed ************************")

        self.logger.info(" ************************** test_Profile_payout_Section_Back_Button_014 passed ************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Profile_payout_Section_Download_Invoice_008(self, setup):
        self.logger.info("******************** test_Profile_payout_Section_Download_Invoice_008 Test case Started **************************")
        self.logger.info("******************** Verifying Profile Section Test **************************")
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
        self.logger.info("********************* Clicked on the Profile option. *********************")
        profile_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.profile_xpath)))
        profile_option.click()

        time.sleep(2)

        # Add your code to move the cursor to the right side here
        self.logger.info("***************** Moved cursor to the right side *******************")
        right_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]")
        action = ActionChains(self.driver)
        action.move_to_element(right_element)
        action.perform()

        self.logger.info("***************** Click to Payout *******************")

        payout_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[1]/div/div/div/button[3]")
        payout_Xpath.click()

        time.sleep(2)

        self.logger.info("***************** Download Invoice *******************")

        Download_Invoice_button_Xpath = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div[5]/div[3]/div/table/tbody/tr/td[7]/a/img")

        self.logger.info("***************** Scroll Download Invoice *******************")

        self.driver.execute_script("arguments[0].scrollIntoView(true);", Download_Invoice_button_Xpath)

        time.sleep(2)

        Download_Invoice_button_Xpath.click()

        time.sleep(2)

        self.driver.close()

        self.logger.info("****************** test_Profile_payout_Section_Download_Invoice_008 Test is completed ************************")

        self.logger.info(" ************************** test_Profile_payout_Section_Download_Invoice_008 passed ************************")

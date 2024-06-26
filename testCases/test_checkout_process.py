import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageObjects.checkout_page import CheckoutPage
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGenerator

class TestCheckoutProcess:
    baseURL = Readconfig.getApplicationURL()
    logger = LogGenerator.loggen()

    @pytest.fixture()
    def setup(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_checkout_positive_scenario(self, setup):
        self.logger.info("******************** Checkout Positive Scenario Test **************************")
        driver = setup
        driver.get(self.baseURL)
        checkout_page = CheckoutPage(driver)

        try:
            mobile_product = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a"))
            )
            mobile_product.click()

            add_to_cart_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div[2]/div[2]/div/a"))
            )
            add_to_cart_button.click()
            WebDriverWait(driver, 10).until(EC.alert_is_present()).accept()

            cart_icon = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/nav/div/div/ul/li[4]/a"))
            )
            cart_icon.click()

            place_order_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div[2]/button"))
            )
            place_order_button.click()

            checkout_page.fill_checkout_details("Test", "India", "Pune", "12345678910", "June", "2023")

            checkout_page.click_purchase_button()

        except Exception as e:
            self.logger.error(f"Exception: {str(e)}")
            driver.save_screenshot(".\\Screenshots\\checkout_positive_error.png")
            assert False, f"Exception occurred: {str(e)}"

        finally:
            driver.quit()


    def test_checkout_negative_scenario(self, setup):
        self.logger.info("******************** Checkout Negative Scenario Test **************************")
        driver = setup
        driver.get(self.baseURL)
        checkout_page = CheckoutPage(driver)

        try:
            cart_icon = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/nav/div[1]/ul/li[4]/a"))
            )
            cart_icon.click()

            place_order_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div[2]/button"))
            )
            place_order_button.click()

            assert WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div[2]/button"))
            )

            self.logger.info("****************** Checkout Negative Scenario Test Passed ************************")

        except Exception as e:
            self.logger.error(f"Exception: {str(e)}")
            driver.save_screenshot(".\\Screenshots\\checkout_negative_error.png")
            assert False, f"Exception occurred: {str(e)}"

        finally:
            driver.quit()
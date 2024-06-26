import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGenerator

class TestProductBrowsing:
    baseURL = Readconfig.getApplicationURL()
    logger = LogGenerator.loggen()

    @pytest.fixture()
    def setup(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    def test_verify_products_on_homepage(self, setup):
        self.logger.info("******************** Verify Products on Homepage Test **************************")
        driver = setup
        driver.get(self.baseURL)

        try:
            product_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a"))
            )
            assert product_element.text.strip() != "", "Product element not found or empty"
            self.logger.info("****************** Products on Homepage Test Passed ************************")

        except Exception as e:
            self.logger.error(f"Exception: {str(e)}")
            driver.save_screenshot(".\\Screenshots\\homepage_products_error.png")
            assert False

        finally:
            driver.quit()

    def test_navigate_product_categories(self, setup):
        self.logger.info("******************** Navigate Product Categories Test **************************")
        driver = setup
        driver.get(self.baseURL)

        try:
            mobile_category_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a"))
            )
            mobile_category_link.click()

            WebDriverWait(driver, 10).until(
                EC.title_is("STORE")
            )

            product_title_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/h2"))
            )

            assert "Samsung galaxy s6" in product_title_element.text, "Samsung galaxy s6 not found on product page"
            self.logger.info("****************** Product Categories Navigation Test Passed ************************")

        except Exception as e:
            self.logger.error(f"Exception: {str(e)}")
            driver.save_screenshot(".\\Screenshots\\product_categories_error.png")
            assert False, f"Exception occurred: {str(e)}"

        finally:
            driver.quit()

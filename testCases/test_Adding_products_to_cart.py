import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGenerator

class TestAddToCart:
    baseURL = Readconfig.getApplicationURL()
    logger = LogGenerator.loggen()

    @pytest.fixture()
    def setup(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    def test_add_product_to_cart(self, setup):
        self.logger.info("******************** Add Product to Cart Test **************************")
        driver = setup
        driver.get(self.baseURL)

        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div[2]/form/ul/li[2]/button"))
            )
            next_button.click()

            last_product = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[6]/div/div/h4/a"))
            )

            last_product.click()

            add_to_cart_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div[2]/div[2]/div/a"))
            )
            add_to_cart_button.click()

            self.logger.info("****************** Product Added to Cart Successfully ************************")

        except Exception as e:
            self.logger.error(f"Exception: {str(e)}")
            driver.save_screenshot(".\\Screenshots\\add_to_cart_error.png")
            assert False, f"Exception occurred: {str(e)}"

        finally:
            driver.quit()


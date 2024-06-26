from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_details(self, name, country, city, credit_card_no, month, year):
        name_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[1]/input"))
        )
        name_input.send_keys(name)

        country_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[2]/input"))
        )
        country_input.send_keys(country)

        city_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[3]/input"))
        )
        city_input.send_keys(city)

        credit_card_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[4]/input"))
        )
        credit_card_input.send_keys(credit_card_no)

        month_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[5]/input"))
        )
        month_input.send_keys(month)

        year_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[6]/input"))
        )
        year_input.send_keys(year)

    def click_purchase_button(self):
        purchase_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]"))
        )
        purchase_button.click()

    def get_purchase_confirmation_message(self):
        confirmation_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Thank you for your purchase!')]"))
        )
        return confirmation_message.text

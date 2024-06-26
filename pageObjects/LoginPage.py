from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    login_menu_xpath = (By.XPATH, "/html/body/nav/div[1]/ul/li[5]/a")
    username_xpath = (By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[1]/input")
    password_xpath = (By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[2]/input")
    login_button_xpath = (By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")

    def __init__(self, driver):
        self.driver = driver

    def clickLoginMenu(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Login.login_menu_xpath)
        ).click()

    def setUsername(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Login.username_xpath)
        ).send_keys(username)

    def setPassword(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Login.password_xpath)
        ).send_keys(password)

    def clickLoginButton(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Login.login_button_xpath)
        ).click()

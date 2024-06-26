from selenium.webdriver.common.by import By

class Login:
    button_login_menu_xpath = (By.XPATH, "/html/body/nav/div[1]/ul/li[5]/a")
    textbox_username_xpath = (By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[1]/input")
    textbox_password_xpath = (By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[2]/input")
    button_login_xpath = (By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")

    def __init__(self, driver):
        self.driver = driver

    def clickLogin(self):
        self.driver.find_element(*Login.button_login_menu_xpath).click()

    def setUsername(self, username):
        self.driver.find_element(*Login.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(*Login.textbox_password_xpath).send_keys(password)

    def clickSubmit(self):
        self.driver.find_element(*Login.button_login_xpath).click()
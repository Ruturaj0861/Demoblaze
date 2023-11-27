from selenium.webdriver.common.by import By


class Login:
    textbox_Email_xpath = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/form/div[1]/div[2]/div/input")
    textbox_Password_xpath = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/form/div[2]/div[2]/div/div/input")
    button_login_xpath = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/form/div[4]/button")
    button_logout_XPATH = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/ul/li[12]/div")

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, username):
        self.driver.find_element(*Login.textbox_Email_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(*Login.textbox_Password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*Login.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(*Login.button_logout_XPATH).click()

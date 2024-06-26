from selenium.webdriver.common.by import By


class Sign_up:
    button_sign_up_xpath = (By.XPATH, "/html/body/nav/div[1]/ul/li[8]/a")
    textbox_Username_xpath = (By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[1]/input")
    button_password_xpath = (By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[2]/input")
    left_element_Xpath = (By.XPATH, "/html/body/div[1]/div/div/div/div/div/div")

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, username):
        self.driver.find_element(*Dashboard.textbox_Email_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(*Dashboard.textbox_Password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*Dashboard.button_login_xpath).click()

from selenium.webdriver.common.by import By


class Sign_up:
    button_sign_up_xpath = (By.XPATH, "/html/body/nav/div[1]/ul/li[8]/a")
    textbox_Username_xpath = (By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[1]/input")
    textbox_password_xpath = (By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[2]/input")
    button_Sign_Register_xpath = (By.XPATH, "/html/body/div[2]/div/div/div[3]/button[2]")


    def __init__(self, driver):
        self.driver = driver

    def clickSignUp(self):
        self.driver.find_element(*Sign_up.button_sign_up_xpath).click()

    def setUsername(self, username):
        self.driver.find_element(*Sign_up.textbox_Username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(*Sign_up.textbox_password_xpath).send_keys(password)

    def clickRejester(self):
        self.driver.find_element(*Sign_up.button_Sign_Register_xpath).click()

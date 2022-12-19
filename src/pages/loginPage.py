from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    INPUT_USERNAME = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")

    BTN_LOGIN = (By.ID, "login-button")
    BTN_LOGOUT = (By.ID, "logout_sidebar_link")

    HAMBURGER_MENU = (By.ID, "react-burger-menu-btn")
    

    def __init__(self, driver):
        super().__init__(driver)

    def enter_login_credentials(self, user, pwd):
        self.input_element(self.INPUT_USERNAME, user)
        self.input_element(self.INPUT_PASSWORD, pwd)
        self.wait_page()

    def enter_login(self):
        self.click_element(self.BTN_LOGIN)
        self.wait_page()

    def log_out(self):
        self.click_element(self.HAMBURGER_MENU)
        self.wait_page()
        self.click_element(self.BTN_LOGOUT)
        self.wait_page()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages.utils.base_page_object import BasePage

class LoginPage(BasePage):
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    
    def __init__(self, context):
        super().__init__(context.browser)
    
    def type_user(self, username):
        self.type_text(self.username_input, username)
    
    def type_password(self, password):
        self.type_text(self.password_input, password)
    
    def click_login(self):
        self.click_element(self.login_button)
        
    def login(self, user, pwd):
        self.type_user(user)
        self.type_password(pwd)
        self.click_login()
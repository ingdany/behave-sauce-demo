from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages.base_page_object import BasePage

class LoginPage(BasePage):
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    
    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            # base_url='https://www.saucedemo.com/v1/index.html'
        )
    
    def type_user(self, username):
        wait = WebDriverWait(self, 10)
        username_element = wait.until(EC.element_to_be_clickable(self.username_input))
        username_element.send_keys(username)
    
    def type_password(self, password):
        wait = WebDriverWait(self, 10)
        password_element = wait.until(EC.element_to_be_clickable(self.password_input))
        password_element.send_keys(password)
    
    def click_login(self):
        wait = WebDriverWait(self, 10)
        login_element = wait.until(EC.element_to_be_clickable(self.login_button))
        login_element.click()  
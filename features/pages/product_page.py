from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages.base_page_object import BasePage

class ProductPage(BasePage):
    title_label = (By.CLASS_NAME, "product_label")
    
    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            # base_url='https://opensource-demo.orangehrmlive.com/'
        )
    
    def verify_product_title(self, title):
        wait = WebDriverWait(self, 10)
        title_element = wait.until(EC.element_to_be_clickable(self.title_label))
        assert title_element.text == title
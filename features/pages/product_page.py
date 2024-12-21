from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages.utils.base_page_object import BasePage

class ProductPage(BasePage):
    title_label = (By.CLASS_NAME, "product_label")
    
    def __init__(self, context):
        super().__init__(context.browser)
    
    def verify_product_title(self, title):
        title_element = lambda: self.wait_for_element(self.title_label).text
        assert title_element() == title
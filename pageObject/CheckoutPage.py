from selenium.webdriver.common.by import By
from pageObject.ConfirmPage import ConfirmPage

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    __card_title = (By.CSS_SELECTOR, ".card-title a")
    __card_footer = (By.CSS_SELECTOR, ".card-footer button")
    __checkout = (By.XPATH, "//button[@class='btn btn-success']")


    def get_card_title(self):
        return self.driver.find_elements(*CheckoutPage.__card_title)

    def get_card_footer(self):
        return self.driver.find_elements(*CheckoutPage.__card_footer)

    def checkout_items(self):
        self.driver.find_element(*CheckoutPage.__checkout).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page


from selenium.webdriver.common.by import By

from pageObject.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    __shop = (By.CSS_SELECTOR, "a[href*='shop']")
    __name = (By.CSS_SELECTOR, "[name='name']")
    __email = (By.NAME, "email")
    __check = (By.ID, "exampleCheck1")
    __gender = (By.ID, "exampleFormControlSelect1")
    __submit = (By.XPATH, "//input[@value='Submit']")
    __success_message = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shop_items(self):
        self.driver.find_element(*HomePage.__shop).click()  # use * to deserialize the shop tupple above, otherwise find_element wont work
        checkout_page= CheckoutPage(self.driver)
        return checkout_page

    def get_name(self):
        return self.driver.find_element(*HomePage.__name)

    def get_email(self):
        return self.driver.find_element(*HomePage.__email)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.__check)

    def get_gender(self):
        return self.driver.find_element(*HomePage.__gender)

    def submit_form(self):
        return self.driver.find_element(*HomePage.__submit)

    def get_success_message(self):
        return self.driver.find_element(*HomePage.__success_message)

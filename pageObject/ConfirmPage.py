from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    __country_text_box= (By.ID, "country")
    __agree_check_box=(By.XPATH,"//div[@class='checkbox checkbox-primary']")
    __submit_button=(By.CSS_SELECTOR,"[type='submit']")
    __success_alert=(By.CSS_SELECTOR,"[class*='alert-success']")

    def type_country(self, country):
        self.driver.find_element(*ConfirmPage.__country_text_box).send_keys(country)

    def select_country(self, country):
        self.driver.find_element(By.LINK_TEXT, country).click()

    def i_agree(self):
        self.driver.find_element(*ConfirmPage.__agree_check_box).click()

    def submit(self):
        self.driver.find_element(*ConfirmPage.__submit_button).click()

    def success_alert(self):
        return self.driver.find_element(*ConfirmPage.__success_alert).text



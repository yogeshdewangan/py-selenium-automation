from selenium import webdriver

from pageObject.CheckoutPage import CheckoutPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self, setup):
        log =self.getLogger()
        log.debug("starting test")
        home_page = HomePage(self.driver)
        checkout_page = home_page.shop_items()
        cards = checkout_page.get_card_title()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            if cardText == "Blackberry":
                checkout_page.get_card_footer()[i].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()

        confirm_page = checkout_page.checkout_items()
        confirm_page.type_country("ind")
        self.verify_link_presence("India")
        confirm_page.select_country("India")

        confirm_page.i_agree()
        confirm_page.submit()
        textMatch = confirm_page.success_alert()
        assert ("Success! Thank you!" in textMatch)

import pytest

from pageObject.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, getData):
        log= self.getLogger()
        log.debug("starting test")
        homepage = HomePage(self.driver)
        m =getData["firstname"]
        homepage.get_name().send_keys(getData["firstname"])
        homepage.get_email().send_keys(getData["lastname"])
        homepage.get_checkbox().click()
        self.select_option_by_text(homepage.get_gender(), getData["gender"])
        homepage.submit_form().click()
        alertText = homepage.get_success_message().text
        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param

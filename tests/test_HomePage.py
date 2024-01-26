
import pytest
from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)

        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        log.info("firstname is " + getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getCheckbox().click()
        self.selectOptionByText(homePage.getDropdown(), getData["gender"])
        homePage.getSubmitBtn().click()
        message = homePage.getMessageSuccess().text

        assert "successfully" in message

    # tap
    # @pytest.fixture(params=[("Marko","marko.gavrilovic88@yahoo.com","Male"), ("Ljubinka", "Vukovic", "Female")])
    # def getData(self, request):
    #     return request.param

    # dictionary
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param

    # # data from exel file
    # @pytest.fixture(params=HomePageData.getTestData("TestCase2"))
    # def getData(self, request):
    #     return request.param
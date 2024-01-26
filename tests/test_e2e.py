
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)

        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        checkoutPage = homePage.shopItems()
        log.info("getting all the card titlles")
        cards = checkoutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i +1
            cardName = card.text
            log.info(cardName)
            if cardName == "Blackberry":
                checkoutPage.getCardFooters()[i].click()

        confirmPage = checkoutPage.getCheckoutButton()
        log.info("Entering country name as ind")
        confirmPage.getGreenCheckoutButton().click()

        confirmPage.getCountryField().send_keys("Ind")
        self.verifyLinkPresence("India")

        confirmPage.getCountry().click()
        confirmPage.getCheckbox().click()
        confirmPage.getPurchaseButton().click()
        successText = confirmPage.getTextMessage().text
        log.info("Text received from applicationis " +successText)
        assert "Success! Thank you! Your order will be delivered in next few weeks :-).ERROR" in successText
        # self.driver.get_screenshot_as_file("screen.png")
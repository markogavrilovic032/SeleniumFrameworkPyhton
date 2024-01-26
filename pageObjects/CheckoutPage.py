from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.CSS_SELECTOR, "div.card.h-100")
    cardTitles = (By.CSS_SELECTOR, "h4.card-title")
    cardFooter = (By.CSS_SELECTOR, "button.btn")
    checkoutButton = (By.CSS_SELECTOR, "a.btn-primary")

    def getProducts(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitles)

    def getCardFooters(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def getCheckoutButton(self):
        self.driver.find_element(*CheckoutPage.checkoutButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
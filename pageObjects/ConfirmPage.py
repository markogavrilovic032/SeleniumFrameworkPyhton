
from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    greenCheckoutButton = (By.CSS_SELECTOR, "button.btn-success")
    countryField = (By.CSS_SELECTOR, "input.validate")
    country = (By.LINK_TEXT, "India")
    checkbox = (By.CSS_SELECTOR, "div.checkbox-primary")
    purchaseButton = (By.CSS_SELECTOR, "[type='submit']")
    textMesage = (By.CSS_SELECTOR, "div.alert-success")

    def getGreenCheckoutButton(self):
        return self.driver.find_element(*ConfirmPage.greenCheckoutButton)

    def getCountryField(self):
        return self.driver.find_element(*ConfirmPage.countryField)

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getTextMessage(self):
        return self.driver.find_element(*ConfirmPage.textMesage)
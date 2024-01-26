
from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage

class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    name = (By.NAME, "name")
    email = (By.CSS_SELECTOR, "input[name = 'email']")
    checkbox = (By.ID, "exampleCheck1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    submitBtn = (By.XPATH, "//input[@type='submit']")
    messageSuccess = (By.CLASS_NAME, "alert-success")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage
        # return self.driver.find_element(*HomePage.shop)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getDropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def getSubmitBtn(self):
        return self.driver.find_element(*HomePage.submitBtn)

    def getMessageSuccess(self):
        return self.driver.find_element(*HomePage.messageSuccess)

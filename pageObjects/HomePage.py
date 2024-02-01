from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckOutPage(self.driver)  # with click  initialize the next class
        return checkoutPage






# -->  me to * diavazei san tupple kai kanei diserialized kai to diavazei opws apo katw
#      self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
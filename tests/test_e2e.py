import pytest
import time
from selenium.webdriver.common.by import By
from tests.utilities.BaseClass import BaseClass
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
# from selenium.webdriver.support import expected_conditions as EC




class TestOne(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)
        checkoutPage = CheckOutPage(self.driver)

        homePage.shopItems().click()
        cards = checkoutPage.getCardTitles()


        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()

        checkoutPage.getItems().click()
        checkoutPage.checkOutItems().click()
        checkoutPage.getPresentCountry().send_keys("ind")

        time.sleep(10)
        #element = EC.presence_of_element_located((By.LINK_TEXT, "India"))
        # element = webDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))

        checkoutPage.getCountry().click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR,  "[type='submit']").click()
        textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text

        assert "Success! Thank you!" in textMatch

        time.sleep(5)


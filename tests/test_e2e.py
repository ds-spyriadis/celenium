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
        checkOutPage = homePage.shopItems() # make the initialization inside the class and return the object here

        # checkoutPage = CheckOutPage(self.driver)   # doesn't needed more
        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()

        checkOutPage.getItems().click()
        checkOutPage.checkOutItems().click()
        checkOutPage.getPresentCountry().send_keys("ind")

        time.sleep(10)
        #element = EC.presence_of_element_located((By.LINK_TEXT, "India"))
        # element = webDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))

        confirmpage = checkOutPage.getCountry()   # se auto to shmeio aplos epistrefw to antikeimeno, alla ta find 8a ta ektelesw edw 
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR,  "[type='submit']").click()
        textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text

        assert "Success! Thank you!" in textMatch

        time.sleep(5)


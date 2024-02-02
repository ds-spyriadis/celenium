import pytest
import time
from selenium.webdriver.common.by import By
from tests.utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage




class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()

        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems() # make the initialization inside the class and return the object here

        log.info("getting all the card titles")
        cards = checkOutPage.getCardTitles()

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()

        checkOutPage.getItems().click()
        checkOutPage.checkOutItems().click()
        log.info("Entering country name as ind")
        checkOutPage.getPresentCountry().send_keys("ind")

        self.verifyLinkPresence("India")  # sent it to baseclass to find the element presence

        confirmpage = checkOutPage.getCountry()   # se auto to shmeio aplos epistrefw to antikeimeno, alla ta find 8a ta ektelesw edw
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR,  "[type='submit']").click()
        textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        log.info("Text received from application is " +textMatch)

        assert "Success! ditriskljlkkjk Thank you!" in textMatch

        time.sleep(5)


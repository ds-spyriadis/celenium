import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from tests.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):  # se ka8e pytest  h clash prepei na 3ekinaei me onoma Test

    def test_formSubmission(self):

        homepage = HomePage(self.driver)
        homepage.getName().send_keys("Dimitris")
        #self.driver.find_element(By.CSS_SELECTOR, "[name='name']").send_keys("Dimitris")

        homepage.getEmail().send_keys("dani")
        homepage.getCheckBox().click()
        sel = Select(homepage.getGender())
        sel.select_by_visible_text("Male")
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)



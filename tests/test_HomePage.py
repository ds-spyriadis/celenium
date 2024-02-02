import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from tests.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):  # se ka8e pytest  h clash prepei na 3ekinaei me onoma Test

    def test_formSubmission(self,getData):       # h getdata exei ta dedomena apo to fixture
        log = self.getLogger()

        homepage = HomePage(self.driver)
        log.info("first name is" + getData["name"])
        homepage.getName().send_keys(getData["name"])      # <=> self.driver.find_element(By.CSS_SELECTOR, "[name='name']").send_keys("Dimitris")
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(),getData["gender"])
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)

        self.driver.refresh()   # xreazetai refresh giati h driver.get("http") einai se alh klash kai den ekteleitai kaue fora, ama thn ektelousa edw den 8a eixa problhma

    @pytest.fixture(params=HomePageData.test_HomePageData)
    def getData(self,request):
        return request.param           #epistrefei oles tis parametrous pou periexonte




from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self,driver):
        self.driver = driver

    #cards = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")
    #self.driver.find_elements(By.CSS_SELECTOR, ".card-footer button")[i].click()
    #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")
    getButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    presentCountry = (By.ID, "country")
    country = (By.LINK_TEXT, "India")



    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle) # epeidh einai tupple vazw to asteraki gia na kanei diserialized
    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)
    def checkOutItems(self):
        return self.driver.find_element(*CheckOutPage.checkOut)
    def getItems(self):
        return self.driver.find_element(*CheckOutPage.getButton)
    def getPresentCountry(self):
        return self.driver.find_element(*CheckOutPage.presentCountry)
    def getCountry(self):
        self.driver.find_element(*CheckOutPage.country).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage

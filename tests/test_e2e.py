import pytest
import time
# from selenium import webdriver
from selenium.webdriver.common.by import By
# # from pageObjects.CheckoutPage import CheckOutPage
# # from pageObjects.HomePage import HomePage
# from selenium.webdriver.support import expected_conditions as EC


from tests.utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")  # kanei dia8esimo to fixture pou periexei thn setup, se epomeno vhma feugei apo edw gia na  xrhsimoopoitai me klhromnomikothta apo polles klaseis
class TestOne(BaseClass):

    def test_e2e(self):





        self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        cards = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")


        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                self.driver.find_elements(By.CSS_SELECTOR, ".card-footer button")[i].click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

        self.driver.find_element(By.ID, "country").send_keys("ind")
        time.sleep(10)
        #element = EC.presence_of_element_located((By.LINK_TEXT, "India"))
        # element = webDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))

        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR,  "[type='submit']").click()
        textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text

        assert "Success! Thank you!" in textMatch


































# import pytest
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# from pageObjects.CheckoutPage import CheckOutPage
# from pageObjects.HomePage import HomePage
# from tests.utilities.BaseClass import BaseClass
# from selenium.webdriver.support import expected_conditions as EC
#
#
# #@pytest.mark.usefixtures("setup")   #den xreazetai giati ta kleiromonei apo thn parent
# def webDriverWait(driver, param):
#     pass
#
#
# class TestOne(BaseClass):
#
#     def test_e2e(self):
#         homePage = HomePage(self.driver)
#         homePage.shopItems().click()
#
#         checkOutPage = CheckOutPage(self.driver)
#         cards = checkOutPage.getCardTitles()
#
#         i = -1
#         for card in cards:
#             i = i + 1
#             cardText = card.text
#             print(cardText)
#             if cardText == "Blackberry":
#                 checkOutPage.getCardFooter()[i].click()
#                 self.driver.find_elements(By.CSS_SELECTOR, ".card-footer button")
#
#         self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
#
#         self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
#
#         self.driver.find_element(By.ID, "country").send_keys("ind")
#         time.sleep(5)
#         #element = webDriverWait(self.driver,10).until(
#          #   EC.presence_of_element_located((By.LINK_TEXT, "India")))
#
#         self.driver.find_element(By.LINK_TEXT, "India").click()
#         self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
#         self.driver.find_element(By.CSS_SELECTOR,  "[type='submit']").click()
#         textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
#
#         #assert ("Success! Thank you!" in textMatch)
#
#



#                                                                                       part 1


# import pytest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # from pageObjects.CheckoutPage import CheckOutPage
# # from pageObjects.HomePage import HomePage
# # from tests.utilities.BaseClass import BaseClass
# from selenium.webdriver.support import expected_conditions as EC
# import pytest
#
#
# class TestOne:
#
#     def test_e2e(self):
#
#         # driver = webdriver.Chrome()
#         # driver.get("https://rahulshettyacademy.com/angularpractice/")
#         # driver.maximize_window()
#
#         driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
#         cards = driver.find_elements(By.CSS_SELECTOR, ".card-title a")
#
#
#         i = -1
#         for card in cards:
#             i = i + 1
#             cardText = card.text
#             print(cardText)
#             if cardText == "Blackberry":
#                 driver.find_elements(By.CSS_SELECTOR, ".card-footer button")[i].click()
#
#         driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
#
#         driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
#
#         driver.find_element(By.ID, "country").send_keys("ind")
#         time.sleep(10)
#         #element = EC.presence_of_element_located((By.LINK_TEXT, "India"))
#         # element = webDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
#
#         driver.find_element(By.LINK_TEXT, "India").click()
#         driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
#         driver.find_element(By.CSS_SELECTOR,  "[type='submit']").click()
#         textMatch = driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
#
#         assert "Success! Thank you!" in textMatch

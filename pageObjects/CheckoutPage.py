# from selenium.webdriver.common.by import By
#
#
# class CheckOutPage:
#     def __init__(self,driver):
#         self.driver = driver
#
#     #cards = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")
#     #self.driver.find_elements(By.CSS_SELECTOR, ".card-footer button")[i].click()
#     #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
#
#     cardTitle = (By.CSS_SELECTOR, ".card-title a")
#     cardFooter =(By.CSS_SELECTOR, ".card-footer button")
#     checkOut = (By.XPATH, "//button[@class='btn btn-success']")
#
#
#     def getCardTitles(self):
#         return self.driver.find_elements(*CheckOutPage.cardTitle) # epeidh eiani tupple vazw to asteraki gia na kanei diseirialized
#
#
#     def getCardFooter(self):
#         return self.driver.find_elements(*CheckOutPage.cardFooter)
#
#     def checkOutItems(self):
#         return self.driver.find_elements(CheckOutPage.checkOut)

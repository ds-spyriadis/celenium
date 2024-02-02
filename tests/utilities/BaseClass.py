from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:   # mporei na kleirodotei to setup se polles klaseis

    def verifyLinkPresence(self,text):                # make a reusable function to find dynamic LINK_TEXT
        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)



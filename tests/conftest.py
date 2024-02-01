import pytest
from selenium import webdriver


def pytest_addoption(parser):                 # psaxnei gia browser input
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):                     #    ->   otan kanoume decrare ena fixture exoume kai ena request instance

    browser_name = request.config.getoption("browser_name")    # eisagei ton browser sth metavlhth
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name == "IE":
        print("IE Driver")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver         #    -> the driver sent to class object,
    yield                               # opote opoia klash xrhsimopoioi afto to fixture exei prosvash sto class driver (cls.driver)
    driver.close()




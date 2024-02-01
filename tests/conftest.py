import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):                     #    ->   otan kanoume decrare ena fixture exoume kai ena request instance
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver         #    -> the driver sent to class object,
    yield                               # opote opoia klash xrhsimopoioi afto to fixture exei prosvash sto class driver (cls.driver)
    driver.close()
    return driver



























# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import service
#
#
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_name", action="store", default="chrome"
#     )
#
#
# @pytest.fixture(scope="class")
# def setup(request):
#     browser_name = request.config.getoption("browser_name")
#     if browser_name == "chrome":
#         driver = webdriver.Chrome()
#     elif browser_name == "edge":
#         driver = webdriver.Edge()
#     elif browser_name == "IE":
#         print("IE Driver")
#
#     driver.get("https://rahulshettyacademy.com/angularpractice/")
#     driver.maximize_window()
#
#
#
#     request.cls.driver = driver
#     yield
#     driver.close()
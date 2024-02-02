import pytest
from selenium import webdriver

driver = None           # declare globally gia na exw prosbash se oles tis synarthseis


def pytest_addoption(parser):                 # psaxnei gia browser input
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):                     #    ->   otan kanoume decrare ena fixture exoume kai ena request instance
    global driver

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






#        kanei screenshot pla to ekana copy paste den to ema8a

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)



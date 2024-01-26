import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: chrome or firefox"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_path = "../drivers/chromedriver.exe"
        # Use the Service class to set the executable path
        service = Service(chrome_path)
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox": #pyhton
        # options = webdriver.FirefoxOptions()
        # options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        # driver = webdriver.Firefox(options=options)
        # driver = webdriver.Firefox(executable_path="geckodriver.exe")
        driver = webdriver.Firefox()

    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Ehtents the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)"  align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file("../reports/"+name)
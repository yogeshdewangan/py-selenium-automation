import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = None


def python_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"  # define a command line option for pytest
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome(executable_path="c:/chromedriver.exe")

    # browser_name = request.config.getoption("browser")
    # if browser_name=="chrome":
    #     driver = webdriver.Chrome(executable_path="c:/chromedriver.exe")
    # if browser_name=="firefox":
    #     driver = webdriver.firefox(executable_path="c:/geckodriver.exe")
    # if browser_name=="IE":
    #     driver = webdriver.Chrome(executable_path="c:/ie.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


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
    import os
    dir_name = "tests/screenshots/"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    try:

        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                print(file_name)
                file_name=dir_name+file_name.replace("tests/","")
                print(file_name)
                _capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra
    except:
        pass


def _capture_screenshot(name):
    print(name)
    driver.get_screenshot_as_file(name)

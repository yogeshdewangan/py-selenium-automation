import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver=None

def python_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome" # define a command line option for pytest
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

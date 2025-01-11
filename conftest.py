import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def chrome_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

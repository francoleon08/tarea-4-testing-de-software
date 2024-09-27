import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope="function")
def setup_teardown():
    firefox_options = Options()
    firefox_options.add_argument("--width=532")
    firefox_options.add_argument("--height=788")

    driver = webdriver.Firefox(service=Service(), options=firefox_options)
    yield driver
    driver.quit()

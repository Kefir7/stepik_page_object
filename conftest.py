import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help="Choose language: e.g., en, es, fr"
    )

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print(f"\n[INFO] Starting Chrome browser with language: {language}")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    driver = webdriver.Chrome(options=options)
    yield driver
    print("\n[INFO] Quitting browser...")
    driver.quit()

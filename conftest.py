from selenium import webdriver
import pytest
import os
from datetime import datetime

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            nome_arquivo = f"screenshots/{item.name}_{datetime.now():%Y%m%d_%H%M%S}.png"
            driver.save_screenshot(nome_arquivo)
            print(f"\nScreenshot salvo em {nome_arquivo}")

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    d = webdriver.Chrome(options=options)

    yield d

    d.quit()
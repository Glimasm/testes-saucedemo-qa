import pytest
from pages.login_page import LoginPage

def test_login_sucesso(driver):
    login_page = LoginPage(driver)
    login_page.realizar_login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url

def test_login_invalido(driver):
    login_page = LoginPage(driver)
    login_page.realizar_login("standard_user", "secretsauce")

    assert "inventory.html" not in driver.current_url
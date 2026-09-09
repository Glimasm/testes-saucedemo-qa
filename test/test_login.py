import pytest
from pages.login_page import LoginPage

def test_login_sucesso(usuario_logado):
    login_page = LoginPage(usuario_logado)
    login_page.realizar_login("standard_user", "secret_sauce")

    assert "inventory.html" in usuario_logado.current_url

def test_login_invalido(usuario_logado):
    login_page = LoginPage(usuario_logado)
    login_page.realizar_login("standard_user", "secretsauce")

    assert "inventory.html" not in usuario_logado.current_url
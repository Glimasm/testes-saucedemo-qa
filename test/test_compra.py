import pytest
from pages.login_page import LoginPage
from pages.produtos_page import ProdutoPage
from pages.carrinho_page import CarrinhoPage

def test_adicionar_produto(driver):
    login_page = LoginPage(driver)
    login_page.realizar_login("standard_user", "secret_sauce")

    produto_page = ProdutoPage(driver)
    produto_page.adicionar_ao_carrinho("sauce-labs-backpack")
    produto_page.adicionar_ao_carrinho("sauce-labs-bike-light")


    carrinho = CarrinhoPage(driver)
    carrinho.abrir_carrinho()
    carrinho.obter_nome_produto()

    nomes_esperados = [
      "Sauce Labs Backpack",
      "Sauce Labs Bike Light",
  ]


    assert sorted(carrinho.obter_nome_produto()) == sorted(nomes_esperados)

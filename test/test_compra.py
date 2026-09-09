import pytest
from pages.produtos_page import ProdutoPage
from pages.carrinho_page import CarrinhoPage

def test_adicionar_multiplos_produtos_ao_carrinho(usuario_logado):

    produto_page = ProdutoPage(usuario_logado)
    produto_page.adicionar_ao_carrinho("sauce-labs-backpack")
    produto_page.adicionar_ao_carrinho("sauce-labs-bike-light")


    carrinho = CarrinhoPage(usuario_logado)
    carrinho.abrir_carrinho()

    nomes_esperados = [
      "Sauce Labs Backpack",
      "Sauce Labs Bike Light",
  ]


    assert sorted(carrinho.obter_nome_produto()) == sorted(nomes_esperados)


def test_remover_produto_do_carrinho(usuario_logado):
    
    produto_page = ProdutoPage(usuario_logado)
    produto_page.adicionar_ao_carrinho("sauce-labs-backpack")
    produto_page.adicionar_ao_carrinho("sauce-labs-bike-light")

    carrinho = CarrinhoPage(usuario_logado)
    carrinho.abrir_carrinho()
    carrinho.remover_produto("sauce-labs-backpack")

    nomes_esperado = [
        "Sauce Labs Bike Light"
    ]

    assert carrinho.numero_contador() == len(nomes_esperado)

def test_carrinho_vazio(usuario_logado):
    
    produto_page = ProdutoPage(usuario_logado)
    produto_page.adicionar_ao_carrinho("sauce-labs-backpack")
    produto_page.adicionar_ao_carrinho("sauce-labs-bike-light")

    carrinho = CarrinhoPage(usuario_logado)
    carrinho.abrir_carrinho()
    carrinho.remover_produto("sauce-labs-backpack")
    carrinho.remover_produto("sauce-labs-bike-light")

    nomes_esperados = []

    assert carrinho.numero_contador() == len(nomes_esperados)
from pages.produtos_page import ProdutoPage
from pages.carrinho_page import CarrinhoPage
from pages.checkout_page import CheckoutPage
from decimal import Decimal, ROUND_HALF_UP


def test_sem_primeiro_nome_checkout(usuario_logado):
    carrinho = CarrinhoPage(usuario_logado)
    carrinho.abrir_carrinho()
    carrinho.clicar_checkout()

    checkout = CheckoutPage(usuario_logado)
    checkout.realizar_checkout("", "Lima", "12345678")

    assert checkout.obter_mensagem_erro() == "Error: First Name is required"

def test_sem_sobrenome_checkout(usuario_logado):
    carrinho = CarrinhoPage(usuario_logado)
    carrinho.abrir_carrinho()
    carrinho.clicar_checkout()

    checkout = CheckoutPage(usuario_logado)
    checkout.realizar_checkout("Gabriel", "", "12345678")

    assert checkout.obter_mensagem_erro() == "Error: Last Name is required"

def test_sem_postalcode_checkout(usuario_logado):
    carrinho = CarrinhoPage(usuario_logado)
    carrinho.abrir_carrinho()
    carrinho.clicar_checkout()

    checkout = CheckoutPage(usuario_logado)
    checkout.realizar_checkout("Gabriel", "Lima", "")

    assert checkout.obter_mensagem_erro() == "Error: Postal Code is required"

def test_comprar_carrinho_vazio(usuario_logado):
    carrinho = CarrinhoPage(usuario_logado)
    carrinho.abrir_carrinho()
    carrinho.clicar_checkout()

    checkout = CheckoutPage(usuario_logado)
    checkout.realizar_checkout("Gabriel", "Lima", "12345678")
    checkout.finalizar_checkout()

    assert checkout.obter_mensagem_compra() == "Thank you for your order!"

def test_comprar_produtos(usuario_logado):

    produtos_esperados = [
        {"nome": "Sauce Labs Backpack", "preco": Decimal("29.99")},
        {"nome": "Sauce Labs Bike Light", "preco": Decimal("9.99")},
    ]
    
    produto_page = ProdutoPage(usuario_logado)
    produto_page.adicionar_ao_carrinho("sauce-labs-backpack")
    produto_page.adicionar_ao_carrinho("sauce-labs-bike-light")


    carrinho = CarrinhoPage(usuario_logado)
    carrinho.abrir_carrinho()

    produtos_encontrados = carrinho.obter_produtos_com_precos()


    assert sorted(produtos_encontrados, key=lambda p: p["nome"]) == sorted(
        produtos_esperados, key=lambda p: p["nome"]
    )

    carrinho.clicar_checkout()

    checkout = CheckoutPage(usuario_logado)
    checkout.realizar_checkout("Gabriel", "Lima", "12345678")


    subtotal_esperado = sum((produto["preco"] for produto in produtos_esperados),
                            Decimal("0.00"))

    assert checkout.obter_subtotal() == subtotal_esperado

    percentual_imposto = Decimal("0.08")
    imposto_esperado = (
        subtotal_esperado * percentual_imposto
    ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    imposto_exibido = checkout.obter_taxa()

    assert imposto_exibido == imposto_esperado

    total_esperado = subtotal_esperado + imposto_exibido

    assert checkout.obter_total() == total_esperado
    
    checkout.finalizar_checkout()

    assert checkout.obter_mensagem_compra() == "Thank you for your order!"
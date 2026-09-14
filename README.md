# Testes de Login e Carrinho — SauceDemo

Suíte de testes automatizados em Python, cobrindo o fluxo de login do site
de prática [saucedemo.com](https://www.saucedemo.com) com caminho cujo login está correto e
caminho do login errado, além da adição e conferência de produtos no carrinho,
seguindo o padrão Page Object Model.

## Stack

Python · Selenium WebDriver · pytest · Google Chrome

## Estrutura do projeto

```
.
├── conftest.py            # fixture do driver + hook de screenshot automático em falha
├── pages/
│   ├── __init__.py
│   ├── base_page.py       # ações genéricas (clicar, escrever, esperar)
│   ├── login_page.py      # Page Object da tela de login
│   ├── produtos_page.py   # Page Object para adicionar produtos ao carrinho
│   ├── carrinho_page.py   # itens, preços, remoção e acesso ao checkout
│   └── checkout_page.py   # dados do comprador, valores e finalização da compra
├── test/
│   ├── __init__.py
│   ├── test_login.py      # login válido e inválido
│   ├── test_compra.py     # adição, remoção e conferência do carrinho
│   └── test_checkout.py   # campos obrigatórios, compra vazia, produtos e totais
├── requirements.txt
├── .gitignore
└── README.md
```

## Como rodar

```bash
pip install -r requirements.txt
pytest
```

## O que está coberto

- Login com credenciais válidas → redireciona para a página de inventário
- Login com credenciais inválidas → permanece na tela de login
- Adição de produtos ao carrinho → o teste `test_adicionar_multiplos_produtos_ao_carrinho` adiciona
  Sauce Labs Backpack e Sauce Labs Bike Light, abre o carrinho e compara os
  nomes exibidos com a lista esperada, independentemente da ordem
- Remoção de produto → verifica que o contador do carrinho passa de dois itens para um
- Esvaziamento do carrinho → verifica que o contador retorna zero após remover todos os produtos
- Campos obrigatórios do checkout → confere as mensagens de erro para primeiro nome,
  sobrenome e código postal vazios, em cenários separados
- Produtos e preços → compara os nomes e preços do carrinho com os valores esperados
- Subtotal → compara o valor exibido no checkout com a soma dos preços esperados usando `Decimal`
- Total → verifica se corresponde ao subtotal mais o imposto exibido,
  sem validar de forma independente a regra de cálculo do imposto
- Finalização da compra → verifica a mensagem de confirmação após finalizar o checkout
- Compra com carrinho vazio → documenta que a aplicação permite finalizar uma compra sem produtos
- Screenshot automático salvo em screenshots/ sempre que um teste falha,
  via hook pytest_runtest_makereport

## Decisões de design

- **Page Object Model**: `LoginPage`, `ProdutoPage`, `CarrinhoPage` e
  `CheckoutPage` encapsulam os localizadores e as interações com cada tela.
  As ações comuns de espera, clique, escrita e leitura ficam em `BasePage`,
  enquanto os valores esperados e os asserts ficam nos testes.
- **Esperas explícitas**: `WebDriverWait` aguarda a visibilidade dos elementos
  usados nas ações de `BasePage` e na leitura dos produtos do carrinho.
  Isso permite acompanhar o carregamento da página sem pausas de duração fixa.
- **Associação entre produto e preço**: `obter_produtos_com_preços()` busca
  o nome e o preço dentro de cada `.cart_item` e retorna uma lista de dicionários.
  Assim, cada preço permanece associado ao produto correspondente.
  `obter_nome_produto()` continua disponível para os testes que precisam apenas dos nomes.
- **Comparação sem depender da ordem**: os testes usam `sorted()` para comparar
  as listas de produtos. Na comparação de nomes e preços, a ordenação usa o nome
  como chave e preserva os dados de cada item.
- **Valores monetários com `Decimal`**: os Page Objects convertem os textos de
  preços, subtotal, imposto e total diretamente para `Decimal`, sem passar por
  `float`, evitando imprecisões de representação binária nos cálculos monetários.
- **Valores esperados definidos no teste**: os nomes e preços esperados são
  declarados na massa de teste, e o subtotal esperado é calculado a partir dela.
  O total é comparado com esse subtotal mais o imposto exibido; a regra de cálculo
  do imposto não é validada de forma independente.
- **Cenários separados**: cada campo obrigatório vazio tem seu próprio teste.
  A compra com produtos e a compra com carrinho vazio também são cenários distintos;
  o segundo registra o comportamento atual de permitir a finalização sem itens.
- **Preparação com fixtures**: `driver` cria uma sessão do Chrome para cada teste
  e a encerra após a execução. `usuario_logado` reutiliza essa fixture para preparar
  a autenticação dos cenários.

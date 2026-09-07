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
├── conftest.py           # fixture do driver + hook de screenshot automático em falha
├── pages/
│   ├── __init__.py
│   ├── base_page.py     # ações genéricas (clicar, escrever, esperar)
│   ├── login_page.py    # Page Object da tela de login
│   ├── produtos_page.py # Page Object para adicionar produtos ao carrinho
│   └── carrinho_page.py # Page Object para abrir o carrinho e obter os nomes dos produtos
├── test/
│   ├── __init__.py
│   ├── test_login.py    # casos de teste: login válido e inválido
│   └── test_compra.py   # teste de adição e conferência dos produtos no carrinho
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
- Adição de produtos ao carrinho → o teste `test_adicionar_produto` adiciona
  Sauce Labs Backpack e Sauce Labs Bike Light, abre o carrinho e compara os
  nomes exibidos com a lista esperada, independentemente da ordem
- Screenshot automático salvo em screenshots/ sempre que um teste falha,
  via hook pytest_runtest_makereport

## Decisões de design

- **Page Object Model**: cada página do site é uma classe (`LoginPage`,
  `ProdutoPage` e `CarrinhoPage`), que herda ações genéricas de
  espera/clique/escrita de `BasePage`. Isso isola
  os localizadores de elemento da lógica do teste — se o site mudar um `id`,
  a correção fica em um único lugar.
- **Esperas explícitas em vez de implicitly_wait**: as ações aguardam
  a visibilidade dos elementos via WebDriverWait, evitando
  misturar espera implícita e explícita — uma causa comum de teste flaky.
- **Conferência do carrinho**: o método `obter_nome_produto` retorna uma lista
  com os nomes dos produtos. O teste compara essa lista com os nomes esperados
  usando `sorted()`, verificando se há produtos faltando ou sobrando.
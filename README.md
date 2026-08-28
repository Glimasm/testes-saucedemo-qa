# Testes de Login — SauceDemo

Suíte de testes automatizados em Python, cobrindo o fluxo de login do site
de prática [saucedemo.com](https://www.saucedemo.com) com caminho cujo login está correto e
caminho do login errado, seguindo o padrão Page Object Model.

## Stack

Python · Selenium WebDriver · pytest · Google Chrome

## Estrutura do projeto

```
.
├── conftest.py     # fixture do driver + hook de screenshot automático em falha
├── pages/
│   ├── __init__.py
│   └── base_page.py      # ações genéricas (clicar, escrever, esperar)
│   └── login_page.py    # Page Object da tela de login
└── tests/
│   └── __init__.py
│   └── test_login.py    # casos de teste: login válido e inválido
```

## Como rodar

```bash
pip install -r requirements.txt
pytest
```

## O que está coberto

- Login com credenciais válidas → redireciona para a página de inventário
- Login com credenciais inválidas → permanece na tela de login
- Screenshot automático salvo em screenshots/ sempre que um teste falha,
  via hook pytest_runtest_makereport

## Decisões de design

- **Page Object Model**: cada página do site é uma classe (LoginPage), que
  herda ações genéricas de espera/clique/escrita de `BasePage`. Isso isola
  os localizadores de elemento da lógica do teste — se o site mudar um `id`,
  a correção fica em um único lugar.
- **Esperas explícitas em vez de implicitly_wait**: todas as ações esperam
  a condição certa (visibilidade, clicabilidade) via WebDriverWait, evitando
  misturar espera implícita e explícita — uma causa comum de teste flaky.

## Próximos passos

- Testes de API com requests
- Integração contínua com GitHub Actions

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from decimal import Decimal

class CarrinhoPage(BasePage):

    def abrir_carrinho(self):
        self.clicar((By.CLASS_NAME, "shopping_cart_link"))

    def remover_produto(self, produto: str):
        self.clicar((By.ID, f"remove-{produto}"))

    def obter_nome_produto(self):
        elementos = self.wait.until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
            )
        )
        return [elemento.text for elemento in elementos]

    def obter_produtos_com_preços(self):
        elementos = self.wait.until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, ".cart_item")
            )
        )

        produtos = []
        for elemento in elementos:
            nome = elemento.find_element(
                By.CSS_SELECTOR, ".inventory_item_name"
            ).text
            preco_texto = elemento.find_element(
                By.CSS_SELECTOR, ".inventory_item_price"
            ).text

            preco = Decimal(preco_texto.replace("$","").strip())

            produtos.append({"nome": nome, "preco": preco})

        return produtos

    def numero_contador(self):
        elementos = self.driver.find_elements(By.CLASS_NAME,
    "shopping_cart_badge")
        if not elementos:
            return 0
        return int(elementos[0].text)

    def clicar_checkout(self):
        self.clicar((By.ID, "checkout"))
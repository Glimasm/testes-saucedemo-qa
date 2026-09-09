from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

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

    def numero_contador(self):
        elementos = self.driver.find_elements(By.CLASS_NAME,
    "shopping_cart_badge")
        if not elementos:
            return 0
        return int(elementos[0].text)
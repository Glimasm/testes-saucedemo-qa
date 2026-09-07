from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CarrinhoPage(BasePage):

    def abrir_carrinho(self):
        self.clicar((By.CLASS_NAME, "shopping_cart_link"))

    def obter_nome_produto(self):
        elementos = self.wait.until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
            )
        )
        return [elemento.text for elemento in elementos]
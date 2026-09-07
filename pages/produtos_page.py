from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProdutoPage(BasePage):

    def adicionar_ao_carrinho(self, produto: str):
        locator = (By.ID, f"add-to-cart-{produto}")
        self.clicar(locator)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from decimal import Decimal

class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.botao_continue = (By.ID, "continue")

    def realizar_checkout(self, first_name, last_name, zip_code):
        self.escrever(self.first_name, first_name)
        self.escrever(self.last_name, last_name)
        self.escrever(self.zip_code, zip_code)
        self.clicar(self.botao_continue)

    def obter_subtotal(self):
        texto = self.obter_texto((
            By.CLASS_NAME, "summary_subtotal_label"
        ))
        return Decimal(texto.split("$")[-1].strip())

    def obter_taxa(self):
        texto = self.obter_texto((
            By.CLASS_NAME, "summary_tax_label"
        ))
        return Decimal(texto.split("$")[-1].strip())

    def obter_total(self):
        texto = self.obter_texto((
            By.CLASS_NAME, "summary_total_label"
        ))
        return Decimal(texto.split("$")[-1].strip())

    def finalizar_checkout(self):
        self.clicar((By.ID, "finish"))

    def obter_mensagem_compra(self):
        return self.obter_texto(
            (By.CSS_SELECTOR, "[data-test='complete-header']")
        )
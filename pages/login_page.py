from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.campo_usuario = (By.ID, "user-name")
        self.campo_senha = (By.ID, "password")
        self.botao_login = (By.ID, "login-button")

    def carregar_pagina(self):
        self.abrir_url("https://www.saucedemo.com")

    def realizar_login(self, usuario, senha):
        self.carregar_pagina()
        self.escrever(self.campo_usuario, usuario)
        self.escrever(self.campo_senha, senha)
        self.clicar(self.botao_login)
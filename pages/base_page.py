from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage():

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def abrir_url(self, url: str):
        self.driver.get(url)

    def encontrar_elemento(self, locator: tuple):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def clicar(self, locator: tuple):
        self.encontrar_elemento(locator).click()

    def escrever(self, locator: tuple, texto: str):
        elemento = self.encontrar_elemento(locator)
        elemento.clear()
        elemento.send_keys(texto)

    def obter_texto(self, locator: tuple) -> str:
        return self.encontrar_elemento(locator).text

    def obter_mensagem_erro(self):
        return self.obter_texto(
            (By.CSS_SELECTOR, "[data-test='error']")
        )

    def obter_url_atual(self):
        return self.driver.current_url
from botcity.web import WebBot, By, Browser
from webdriver_manager.chrome import ChromeDriverManager

# Define a classe base para os bots
class BotBase:
    def preencher_formulario(self, bot: WebBot):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

    def salvar_dados(self, dados: dict, arquivo: str):
        with open(arquivo, "a", encoding="utf-8") as file:
            for campo, valor in dados.items():
                file.write(f"{campo}: {valor}\n")
            file.write("\n")

# Bot para cadastro de autor
class BotAutor(BotBase):
    def preencher_formulario(self, bot: WebBot):
        dados = {
            "nome_autor": "Machado de Assis",
            "livros_autor": "Dom Casmurro, Memórias Póstumas de Brás Cubas"
        }
        bot.find_element("nome_autor", By.ID).send_keys(dados["nome_autor"])
        bot.wait(1000)
        bot.find_element("livros_autor", By.ID).send_keys(dados["livros_autor"])
        bot.wait(1000)
        bot.find_element("submit_autor", By.ID).click()
        bot.wait(1000)
        self.salvar_dados(dados, "dados_biblioteca.txt")
        bot.find_element("/html/body/nav/button[2]", By.XPATH).click()

# Bot para cadastro de livro
class BotLivro(BotBase):
    def preencher_formulario(self, bot: WebBot):
        dados = {
            "titulo_livro": "Dom Casmurro",
            "autor_livro": "Machado de Assis",
            "codigo_livro": "123456",
            "disponibilidade": "Sim"
        }
        bot.find_element("titulo_livro", By.ID).send_keys(dados["titulo_livro"])
        bot.wait(1000)
        bot.find_element("autor_livro", By.ID).send_keys(dados["autor_livro"])
        bot.wait(1000)
        bot.find_element("codigo_livro", By.ID).send_keys(dados["codigo_livro"])
        bot.wait(1000)
        bot.find_element('//*[@id="disponibilidade"]/option[2]', By.XPATH).click()
        bot.wait(1000)
        bot.find_element("submit_livro", By.ID).click()
        bot.wait(1000)
        self.salvar_dados(dados, "dados_biblioteca.txt")
        bot.find_element('/html/body/nav/button[3]', By.XPATH).click()


# Bot para registro de biblioteca
class BotBiblioteca(BotBase):
    def preencher_formulario(self, bot: WebBot):
        dados = {
            "nome_biblioteca": "Biblioteca Central",
            "livro_codigo": "123456",
            "cliente_nome": "João Silva"
        }
        bot.find_element("nome_biblioteca", By.ID).send_keys(dados["nome_biblioteca"])
        bot.wait(1000)
        bot.find_element("livro_codigo", By.ID).send_keys(dados["livro_codigo"])
        bot.wait(1000)
        bot.find_element("cliente_nome", By.ID).send_keys(dados["cliente_nome"])
        bot.wait(1000)
        bot.find_element("submit_biblioteca", By.ID).click()
        bot.wait(1000)
        self.salvar_dados(dados, "dados_biblioteca.txt")

# Função para processar o bot
def processar_bot(bot: BotBase, web_bot: WebBot):
    bot.preencher_formulario(web_bot)

def main():
    # Configuração do WebBot
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    # ALTERE AQUI!!!!!
    bot.browse(r"C:\Users\lrand\OneDrive\Área de Trabalho\Atividades\Atividade 08\biblioteca.html")

    # Executa cada bot para preencher a seção correspondente
    bot_autor = BotAutor()
    processar_bot(bot_autor, bot)
    bot.wait(3000)  

    bot_livro = BotLivro()
    processar_bot(bot_livro, bot)
    bot.wait(3000)  

    bot_biblioteca = BotBiblioteca()
    processar_bot(bot_biblioteca, bot)
    bot.wait(3000)

    # Encerra o navegador
    bot.stop_browser()

if __name__ == '__main__':
    main()

class Autor:
    def __init__(self, nome):
        self.__nome = nome
        self.__livros = []

    def adicionar_livro(self, livro):
        self.__livros.append(livro)

    def mostrar_livros(self):
        if self.__livros:
            print(f"Livros de {self.__nome}:")
            for livro in self.__livros:
                print(f"- {livro}")
        else:
            print(f"{self.__nome} não possui livros registrados.")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def livros(self):
        return self.__livros

    @livros.setter
    def livros(self, livros):
        if isinstance(livros, list):
            self.__livros = livros
        else:
            print("Erro: Atribuição de livros deve ser uma lista.")

class Livro:
    def __init__(self, titulo, autor, codigo):
        self.__titulo = titulo
        self.__autor = autor
        self.__codigo = codigo
        self.__disponivel = True

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print(f"O livro '{self.__titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.__titulo}' já está emprestado.")

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            print(f"O livro '{self.__titulo}' foi devolvido e está disponível.")
        else:
            print(f"O livro '{self.__titulo}' já está disponível.")

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def disponivel(self):
        return self.__disponivel

    @disponivel.setter
    def disponivel(self, disponivel):
        if isinstance(disponivel, bool):
            self.__disponivel = disponivel
        else:
            print("Erro: A disponibilidade deve ser um valor booleano.")

    @property
    def autor(self):
        return self.__autor

class Biblioteca:
    total_livros = 0

    def __init__(self, nome):
        self.nome = nome
        self.__livros = []
        self.__emprestimos = {}

    def adicionar_livro(self, livro):
        self.__livros.append(livro)
        Biblioteca.total_livros += 1
        print(f"Livro '{livro.titulo}' adicionado à biblioteca '{self.nome}'.")

    def registrar_emprestimo(self, codigo_livro, cliente):
        livro = self.__buscar_livro_por_codigo(codigo_livro)
        if livro and livro.disponivel:
            livro.emprestar()
            self.__emprestimos[codigo_livro] = cliente
            print(f"Empréstimo registrado: {livro.titulo} para {cliente}.")
        elif livro:
            print(f"O livro '{livro.titulo}' já está emprestado.")
        else:
            print(f"Livro com código {codigo_livro} não encontrado.")

    def registrar_devolucao(self, codigo_livro):
        livro = self.__buscar_livro_por_codigo(codigo_livro)
        if livro and not livro.disponivel:
            livro.devolver()
            del self.__emprestimos[codigo_livro]
            print(f"Devolução registrada: {livro.titulo} agora está disponível.")
        elif livro:
            print(f"O livro '{livro.titulo}' já está disponível.")
        else:
            print(f"Livro com código {codigo_livro} não encontrado.")

    def mostrar_livros_disponiveis(self):
        print("Livros disponíveis para empréstimo:")
        livros_disponiveis = [livro for livro in self.__livros if livro.disponivel]
        if livros_disponiveis:
            for livro in livros_disponiveis:
                print(f"- {livro.titulo}")
        else:
            print("Nenhum livro disponível no momento.")

    @classmethod
    def mostrar_total_livros(cls):
        print(f"Total de livros na biblioteca: {cls.total_livros}")

    def __buscar_livro_por_codigo(self, codigo_livro):
        for livro in self.__livros:
            if livro.codigo == codigo_livro:
                return livro
        return None
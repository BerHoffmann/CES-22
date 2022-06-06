
class Produtos:
    def __init__(self):
        pass
        
class Livro(Produtos):

    def __init__(self,nome,autor,edicao,editora,venda,compra,imposto):
        self.nome = nome
        self.autor = autor
        self.edicao = edicao
        self.editora = editora
        self.imposto = Impostos(imposto)
        self.preco = Preco(venda,compra)

    def atualizarPreco(self,novopreco):
        auxiliar = self.preco.preco_de_compra
        self.preco = Preco(novopreco,auxiliar)
    
    def atualizarEdicao(self,novaEdicao):
        self.edicao = novaEdicao
    
    def alterarPrecoLivro(livro,novoPreco):
        livro.preco = Preco(novoPreco)

    def consultaLivro(livro):
        print(livro.nome)
        print(livro.autor)
        print(livro.edicao)
        print(livro.editora)
        print(livro.preco.preco_de_venda)



class Preco:
    def __init__(self,venda,compra):
        self.preco_de_venda = venda
        self.preco_de_compra = compra
        self.lucro = self.preco_de_venda - self.preco_de_compra
    
class Impostos:
    def __init__(self,imposto):
        self.imposto = imposto

class Cadastros:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Autores(Cadastros):
    def __init__(self):
        self.livrosPublicados = None

class Compra:
    def __init__(self):
        pass

def adicionar_livro(titulo, autor, edicao, editora, venda, compra, imposto):
    titulo = Livro(titulo, autor, edicao, editora,venda,compra,imposto)


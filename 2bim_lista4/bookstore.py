
from calendar import c


class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def deleteNode(self,data):

        temp = self.head

        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return

        while(temp is not None):
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        
        if(temp == None):
            return
        
        prev.next = temp.next

        temp = None

            
class Produtos:
    def __init__(self,produto):
        self.produto = produto
        
class Livro(Produtos):

    def __init__(self,nome,autor,edicao,editora,venda,compra,imposto):
        self.nome = nome
        self.produto = nome
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

    def consultaLivro(self):
        print("\n\n--CONSULTA DE LIVRO:\n")
        print("nome: ",self.nome,"\n")
        print("autor: ", self.autor)
        print("edicao: " ,self.edicao)
        print("editora: ",self.editora)
        print("preco de venda: ",self.preco.preco_de_venda)
        print("imposto sobre produto: ", self.imposto.imposto)

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

    def printCad(cadastros):
        print("\n\nusuários cadastrados:")
        aux = cadastros.head
        while(aux is not None):
            print(aux.data.nome)
            print(aux.data.email)
            aux = aux.next

class Autores(Cadastros):
    def __init__(self,nome,email):
        self.publicados = LinkedList()
        self.nome = nome
        self.email = email
    
    def adicionarLivroPublicado(self,livro):
        self.publicados.insert(livro)

    def printLivros(self,lista):
        aux = lista.head
        while(aux is not None):
            print(aux.data.nome)
            aux = aux.next

    def consultaAutor(self):
        print("----------------consulta por autor ----------------------")
        print("livros do autor",self.nome,":")
        self.printLivros(self.publicados)

        self.cur = self.publicados.head
        self.curl = livraria.head

        self.disponiveis = LinkedList()

        while(True):
            while(True):
                if self.cur.data == self.curl.data:
                    self.disponiveis.insert(self.cur.data)

                if(self.curl.next is None):
                    break
                self.curl = self.curl.next

            if(self.cur.next is None):
                break
            self.cur = self.cur.next

        print("-------------livros disponiveis no estoque---------------")
        self.printLivros(self.disponiveis)

class Cliente(Cadastros):
    def __init__(self,nome,email):
        self.compras = Compra()
        self.nome = nome
        self.email = email
            
class Compra:
    def __init__(self):
        self.carrinho = LinkedList()

    def atualizarCompra(self,produto):
        aux = livraria.head
        while(aux is not None):
            if produto == aux.data.produto:
                self.carrinho.insert(aux.data)
            aux = aux.next

    def verCarrinho(self):
        aux = self.carrinho.head
        print("\n----Carrinho de compras----")

        while(aux is not None):
            print(aux.data.produto)
            aux = aux.next
    
    def retirar(self,objeto):
        aux = self.carrinho.head
        while(aux is not None):
            if objeto == aux.data.produto:
                self.carrinho.deleteNode(aux.data)
            aux = aux.next



livraria = LinkedList()
cadastros = LinkedList()

def adicionarCadastro(nome,email):
    cliente = Cliente(nome,email)
    cadastros.insert(cliente)

def adicionarAutor(nome,email):
    cliente = Autores(nome,email)
    cadastros.insert(cliente)

def removerCadastro(nome):
    aux = cadastros.head
    while(aux is not None):
        if aux.data.nome == nome:
            cadastros.deleteNode(aux.data)
        aux = aux.next

def alterarEmail(nome,novoemail):
    aux = cadastros.head
    while(aux is not None):
        if aux.data.nome == nome:
            aux.data.email = novoemail 
        aux = aux.next

def adicionarAoCarrinho(nome,objeto):
    aux = cadastros.head
    while(aux is not None):
        if aux.data.nome == nome:
            aux.data.compras.atualizarCompra(objeto)
        aux = aux.next

def verCarrinho(nome):
    aux = cadastros.head
    while(aux is not None):
        if aux.data.nome == nome:
            aux.data.compras.verCarrinho()
        aux = aux.next

def excluirItem(nome,objeto):
    aux = cadastros.head
    while(aux is not None):
        if aux.data.nome == nome:
            aux.data.compras.retirar(objeto)
        aux = aux.next

def adicionar_livro(titulo, autor, edicao, editora, venda, compra, imposto):

    obra = Livro(titulo, autor, edicao, editora,venda,compra,imposto)
    livraria.insert(obra)

    aux = cadastros.head
    while(aux is not None):
        if aux.data.nome == autor:
            aux.data.adicionarLivroPublicado(obra)
            return
        aux = aux.next
    
    adicionarAutor(autor, "email do autor, caso exista")

    aux = cadastros.head
    while(aux is not None):
        if aux.data.nome == autor:
            aux.data.adicionarLivroPublicado(obra)
            return
        aux = aux.next
    
def consultarLivro(titulo):
    aux = livraria.head
    while(aux is not None):
        if aux.data.nome == titulo:
            aux.data.consultaLivro()
            return
        aux = aux.next
        if(aux is None):
            print("livro nao dispovivel")
        
def removerLivro(titulo):
    aux = livraria.head
    while(aux is not None):
        if aux.data.nome == titulo:
            livraria.deleteNode(aux.data)
        aux = aux.next

def AtualizarPreco(titulo,novoPreco):
    aux = livraria.head
    while(aux is not None):
        if aux.data.nome == titulo:
            aux.data.atualizarPreco(novoPreco)
        aux = aux.next

def AtualizarEdicao(titulo,novaEdicao):
    aux = livraria.head
    while(aux is not None):
        if aux.data.nome == titulo:
            aux.data.atualizarEdicao(novaEdicao)
        aux = aux.next

def consultarAutor(nome):
    aux = cadastros.head
    while(aux is not None):
        if aux.data.nome == nome:
            aux.data.consultaAutor()
        aux = aux.next


#Testes para o prototipo da livraria

adicionarCadastro("Bernardo","ber@gmail")
Cadastros.printCad(cadastros)
adicionarCadastro("Luísa", "Luisa@hotmail")
Cadastros.printCad(cadastros)
removerCadastro("Bernardo")
Cadastros.printCad(cadastros)
alterarEmail("Luísa","lu@gmail")
Cadastros.printCad(cadastros)


adicionar_livro("brave new world","huxley",4,"moderna",40,20,5)
consultarLivro("brave new world")
adicionar_livro("1984","Orwell",6,"companhia", 60,40, 10)
consultarLivro("1984")
AtualizarPreco("1984",75)
consultarLivro("1984")
AtualizarEdicao("brave new world", 5)
consultarLivro("brave new world")
removerLivro("1984")
consultarLivro("1984")
adicionar_livro("animal farm","Orwell",6,"companhia", 40, 25, 10)

Cadastros.printCad(cadastros)
consultarAutor("Orwell")


adicionarAoCarrinho("Luísa","animal farm")
verCarrinho("Luísa")

adicionar_livro("harry potter", "jk rowling", 3, "rocco", 30,10,7)

adicionarAoCarrinho("Luísa","harry potter")
verCarrinho("Luísa")
excluirItem("Luísa","animal farm")
verCarrinho("Luísa")








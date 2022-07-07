#class Estado do documento
class Estado:
    def currState(self):
        print("O documento está em " + self.__class__.__name__)

#classe de documento moderação. Possui uma variavel booleana para verificar se or review do admin foi positivo ou negativo
class Moderacao(Estado):
    def __init__(self):
        self.review = False

    def nextState(self,doc):
        if self.review == False:
            doc.estado = Rascunho()
        else:
            doc.estado = Publicado()
    
    def check(self):
        self.review = True

#classe de documento rascunho. Possui uma variavel booleana para verificar login de admin para mudança de estado ocorrer
#para moderacao ou publicado
class Rascunho(Estado):
    def __init__(self):
        self.admin = False

    def adminLogin(self, user):
        if user.nome == 'admin':
            self.admin = True

    def nextState(self,doc):
        if self.admin == False:
            doc.estado = Moderacao()
        else:
            doc.estado = Publicado()

#classe de documento publicado. Possui uma variavel booleana para verificar se expirou
class Publicado(Estado):
    def __init__(self):
        self.exp = False

    def nextState(self,doc):
        if self.exp == True:
            doc.estado = Rascunho()
        else:
            pass

    def Exp(self):
        self.exp = True

#classe de documento que possui um estado por composição 
class Documento:
    def __init__(self,nome):
        self.estado = Rascunho()
        self.nome = nome

    def changeState(self):
        self.estado.nextState(self)

#Classes dos usuarios que irao realizar as operacoes com os documentos
class user:
    def __init__(self,nome):
        self.nome = nome
    
    def createDoc(self,nome):
        return Documento(nome)

    def changeS(self,doc):
        doc.changeState()
    
    def checkReview(self,doc):
        if self.nome == 'admin':
            doc.estado.check()
    
    def checkExp(self,doc):
        if self.nome == 'admin':
            doc.estado.Exp()
    
    def checkstate(self,doc):
        doc.estado.currState()
    
    def adminLogin(self,doc):
        doc.estado.adminLogin(self)

u1 = user("user1")
u2 = user("admin")

#usuário normal cria um documento e checa seu estado: rascunho
doc1 = u1.createDoc("prontuario")
u1.checkstate(doc1)

#usuario normal muda o estado do documento 1 para Moderacao e checa seu estado
u1.changeS(doc1)
u1.checkstate(doc1)

#usuario admin cria novo documento, checa seu estado, faz login como admin e muda seu estado de Rascunho para Publicado
doc2 = u2.createDoc("certidao")
u2.checkstate(doc2)
u2.adminLogin(doc2)
u2.changeS(doc2)
u2.checkstate(doc2)

#Usuario admin diz que o documento 2 expirou e muda seu estado de publicado para rascunho
u2.checkExp(doc2)
u2.changeS(doc2)
u2.checkstate(doc2)

#Usuario admin muda o estado do documento 1 para rascunho novamente
u2.changeS(doc1)
u2.checkstate(doc1)

#Usuario normal altera o estado do documento 1 para Moderacao
u1.changeS(doc1)

#Usuario admin faz um review positivo do documento 1 e muda seu estado para Publicado
u2.checkstate(doc1)
u2.checkReview(doc1)
u2.changeS(doc1)
u2.checkstate(doc1)
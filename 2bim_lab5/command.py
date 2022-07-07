from cProfile import label
from cgitb import text
import collections
from functools import partial
from http import client
from subprocess import CREATE_NO_WINDOW
from tkinter import *
from tkinter import ttk
from click import command
from sqlalchemy import column

#Classe comando para caso desejasse realizar operacoes gerais com todos os comandos
class Command:
    pass

#classes de comando concretas, que realizam as operacoes. Como sao operacoes simples, nao foi necessario delegá-las a um sistema diferente
#realizou-se as operacoes dentro do próprio comando

#comando de consultar o saldo do cliente
class Saldo(Command):
    def executar(self,cliente):
        janelaSaldo= Tk()
        janelaSaldo.geometry("300x100")
        t = Label(janelaSaldo, text= "o seu saldo é " + str(cliente.getSaldo()))
        t.grid(column=1,row = 1)
        janelaSaldo.mainloop()
        
#comando de consultar o extrato de operações do cliente
class Extrato(Command):

    def executar(self,cliente):
        janelaext= Tk()
        janelaext.geometry("300x100")
        t = Label(janelaext, text= "EXTRATO DE OPERACOES")
        t.grid(column=1,row = 1)
        t2 = Label(janelaext, text=str(cliente.Ext()))
        t2.grid(column=1,row = 2)
        janelaext.mainloop()

#comando de depositar certo valor para sua propria conta do banco
class Depositar(Command):

    def executar(self,cliente):
        janelat= Tk()
        t = Label(janelat, text= "Digite o valor que deseja depositar")
        t.grid(column=0,row = 1)

        t2 = Label(janelat, text= "Valor")
        t2.grid(column=0,row = 4)
        entry2= Entry(janelat)
        entry2.grid(column=0,row = 5)

        exec3 = partial(self.depositar,cliente0,entry2)
        bt = Button(janelat, text = "depositar", command= exec3)
        bt.grid(column=0,row = 6)
        janelat.mainloop()

    def depositar(self,cliente,entry2):
        valor = float(entry2.get())
        cliente.setSaldo(valor)
        sucesso = Tk()
        sucesso.geometry("500x200")
        tsucesso = Label(sucesso, text = "Operacao realizada com sucesso. Feche essa e a janela da operacao.")
        tsucesso.grid(column=0,row = 1)
        sucesso.mainloop()

#comando de depositar certo valor para outro cliente cadastrado no banco
class Transferencia(Command):

    def executar(self,cliente0):

        janelat= Tk()
        t = Label(janelat, text= "Digite o nome para quem deseja transferir e o valor. Clientes cadastrados: Maria, Luisa, Beto")
        t.grid(column=0,row = 1)

        t1 = Label(janelat, text= "Nome")
        t1.grid(column=0,row = 2)
        entry1= Entry(janelat)
        entry1.grid(column=0,row = 3)

        t2 = Label(janelat, text= "Valor")
        t2.grid(column=0,row = 4)
        entry2= Entry(janelat)
        entry2.grid(column=0,row = 5)

        exec3 = partial(self.transferir,cliente0,entry1,entry2)
        bt = Button(janelat, text = "transferir", command= exec3)
        bt.grid(column=0,row = 6)

        janelat.mainloop()

    def transferir(self, cliente0,entrycliente,entryvalor):

        valor = float(entryvalor.get())
        cliente = entrycliente.get()

        achou = False
        for i in Clientes:
            if i.getName() == cliente:
                destino = i
                destino.setSaldo(valor)
                cliente0.setSaldo(-valor)
                achou = True

                sucesso = Tk()
                sucesso.geometry("500x200")
                tsucesso = Label(sucesso, text = "Operacao realizada com sucesso. Feche essa e a janela da operacao.")
                tsucesso.grid(column=0,row = 1)
                sucesso.mainloop()

        if achou == False:
            erro = Tk()
            erro.geometry("300x300")
            terro = Label(erro, text = "Cliente não cadastrado no banco")
            terro.grid(column=0,row = 1)
            erro.mainloop()

#classe cliente que utilizará o sistema
class cliente:
    def __init__(self,nome,saldoinicial):
        self.nome = nome
        self.saldo = saldoinicial
        self.extrato = []
        self.extrato.append(saldoinicial)
        self.historico = []

    #retorna o extrato do cliente
    def Ext(self):
        return self.extrato

    #retorna o nome do cliente
    def getName(self):
        return self.nome
    
    #retorna o saldo do cliente
    def getSaldo(self):
        return self.saldo
    
    #adiciona ou retira certo valor do saldo e salva a operacao no extrato
    def setSaldo(self,add):
        self.saldo = self.saldo + add
        self.extrato.append(add)
    
    #funcao de execucao do comando selecionado e armazenamento do comando no historico do usuario
    def executarComando(self,comando):
        comando.executar(self)
        self.historico.append(comando)


#Suposicao de lista de clientes do banco, gravados em banco de dados para consulta
#Supõe-se cliente usuario com saldo inicial de 4000
cliente0 = cliente('usuario', 4000)
cliente1 = cliente('Beto', 1000)
cliente2 = cliente('Maria',2000)
cliente3 = cliente('Luisa', 500)
Clientes = []
Clientes.append(cliente0)
Clientes.append(cliente1)
Clientes.append(cliente2)
Clientes.append(cliente3)



#Objetos de comanddo para o design pattern Command
ComandoSal= Saldo()
ComandoTransf = Transferencia()
ComandoExt = Extrato()
ComandoDep = Depositar()


#interface do usuario para realização das operações
janela = Tk()
janela.geometry("300x300")
janela.title("Página do banco")
titulo = Label(janela, text = "Bem vindo, faça as operações:")
titulo.grid(column=0,row = 1)

exec = partial(cliente0.executarComando,ComandoSal)
bsaldo = Button(janela, text="VER SALDO", command= exec)
bsaldo.grid(column=1,row = 1)

exec2 = partial(cliente0.executarComando,ComandoExt)
bextrato = Button(janela, text="EXTRATO", command= exec2)
bextrato.grid(column=1,row = 2)

exec3 = partial(cliente0.executarComando,ComandoTransf)
btransf = Button(janela, text="TRANSFERIR", command= exec3)
btransf.grid(column=1,row = 3)

exec4 = partial(cliente0.executarComando,ComandoDep)
btransf = Button(janela, text="DEPOSITAR", command= exec4)
btransf.grid(column=1,row = 4)

janela.mainloop()

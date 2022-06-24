from cgitb import text
import collections
from functools import partial
from subprocess import CREATE_NO_WINDOW
from tkinter import *
from tkinter import ttk
from click import command

from sqlalchemy import column



class Participante:
    def __init__(self,name,log,se,em,end,tel):
        self.nome = name
        self.login = log
        self.senha = se
        self.email = em
        self.endereco = end
        self.telefone = tel

    def Login(self):
        return self.login
    
    def Nome(self):
        return self.nome

    def Email(self):
        return self.email

    def End(self):
        return self.endereco

    def Tel(self):
        return self.telefone
    
    def newAd(self,nl):
        self.endereco = nl
        print("endereço alterado")

    def newTel(self,nl):
        self.telefone = nl
        print("telefone alterado")



janela = Tk()
i = 0
usuarios = []
def create(nome,login,senha,email,endereco,telefone):
    n = nome.get()
    l = login.get()
    s = senha.get()
    e = email.get()
    en = endereco.get()
    t = telefone.get()
    p = Participante(n,l,s,e,en,t)
    usuarios.append(p)
    aviso = Tk()
    l = Label(aviso,text="Usuario criado. Feche a janela de criação de usuario")
    l.pack()
    aviso.mainloop()

janela.title("participantes")
texto = Label(janela, text = "Clique no botao para adicionar participante")
texto.grid(column = 0, row = 0)

def criar():
    janela2 = Tk()
    janela2.title("criacao de usuario")
    t1 = Label(janela2,text="-------------Digite o nome do usuario-------------")
    t1.grid(column = 0, row = 0)

    entry1= Entry(janela2)
    entry1.grid(column=0,row = 1)

  
    t2 = Label(janela2,text="-------------Digite o login do usuario-------------")
    t2.grid(column = 0, row = 3)
    entry2= Entry(janela2)
    entry2.grid(column=0,row = 4)

   
    t3 = Label(janela2,text="-------------Digite a senha do usuario-------------")
    t3.grid(column = 0, row = 5)
    entry3= Entry(janela2)
    entry3.grid(column=0,row = 6)


    t4 = Label(janela2,text="-------------Digite o email do usuario-------------")
    t4.grid(column = 0, row =7)
    entry4= Entry(janela2)
    entry4.grid(column=0,row = 8)

   
    t5 = Label(janela2,text="-------------Digite o endereço do usuario-------------")
    t5.grid(column = 0, row = 9)
    entry5= Entry(janela2)
    entry5.grid(column=0,row = 10)

    
    t6 = Label(janela2,text="-------------Digite o telefone do usuario-------------")
    t6.grid(column = 0, row = 11)
    entry6= Entry(janela2)
    entry6.grid(column=0,row = 12)
    
    crias = partial(create, entry1, entry2, entry3, entry4, entry5, entry6)

    cri = Button(janela2, text= "Criar", command= crias)
    cri.grid(column =0,row = 13)
    janela2.mainloop()


botaoCriar = Button(janela, text="criar Usuario", command= criar )
botaoCriar.grid(column=0,row = 1)


def ver(no):
    nome = no.get()
    for i in range(len(usuarios)):
        if usuarios[i].Nome() == nome:
            
            j3 = Tk()

            lab11 = Label(j3,text="Nome do usuario")
            lab11.grid(column=0,row = 0)
            lab1 =Label(j3,text=usuarios[i].Nome())
            lab1.grid(column=0,row = 1)

            lab21 = Label(j3,text="Login do usuario")
            lab21.grid(column=0,row = 2)
            lab2 = Label(j3,text=usuarios[i].Login())
            lab2.grid(column=0,row = 3)

            lab31 = Label(j3,text = "Email do usuario")
            lab31.grid(column=0,row = 4)
            lab3 = Label(j3,text=usuarios[i].Email())
            lab3.grid(column=0,row = 5)

            lab41 = Label(j3,text="Endereco do usuario")
            lab41.grid(column=0,row = 6)
            lab5 = Label(j3,text=usuarios[i].End())
            lab5.grid(column=0,row = 7)

            lab51 = Label(j3,text="Telefone do usuario")
            lab51.grid(column=0,row = 8)
            lab6 = Label(j3,text=usuarios[i].Tel())
            lab6.grid(column=0,row = 9)

            j3.mainloop()
            

lab = Label(janela, text = "Digite um nome e veja os dados do usuario")
lab.grid(column = 0, row = 2)

entr = Entry(janela)
entr.grid(column=0,row = 3)

v = partial(ver,entr)

botaoVer = Button(janela,text="ver dados de usuario",command = v)
botaoVer.grid(column=0,row = 4)

def uend(no):
    usuarios[i].newAd(no.get())
    aviso = Tk()
    l = Label(aviso,text="Endereço atualizado com sucesso")
    l.pack()
    aviso.mainloop()


def utel(no):
    usuarios[i].newTel(no.get())
    aviso = Tk()
    l = Label(aviso,text="telefone atualizado com sucesso")
    l.pack()
    aviso.mainloop()

def up(no):
    nome = no.get()
    for i in range(len(usuarios)):
        if usuarios[i].Nome() == nome:
            j4 = Tk()

            lab41 = Label(j4,text="Endereco do usuario")
            lab41.grid(column=0,row = 1)
            lab5 = Entry(j4)
            lab5.grid(column=0,row = 2)
            uen = partial(uend,lab5)
            botaoUp2 = Button(j4,text="atualizar endereco",command = uen)
            botaoUp2.grid(column=0,row = 3)

            lab51 = Label(j4,text="Telefone do usuario")
            lab51.grid(column=0,row = 4)
            lab6 = Entry(j4)
            lab6.grid(column=0,row = 5)
            ut = partial(utel,lab6)
            botaoUp3 = Button(j4,text="atualizar Telefone",command = ut)
            botaoUp3.grid(column=0,row = 6)

            j4.mainloop()



update = Label(janela,text="Atualize dados de um usuario")
update.grid(column=0,row = 5)
enup = Entry(janela)
enup.grid(column=0,row = 6)
u = partial(up,enup)
botaoUp = Button(janela,text="atualizar dados",command = u)
botaoUp.grid(column=0,row = 7)



janela.mainloop()

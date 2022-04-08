import abc

class Computador(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, processador, video, ram):
        self.processador = processador
        self.video = video
        self.ram = ram

    @abc.abstractmethod
    def OS(self):
        pass

    @staticmethod
    def help():
        print("crie objetos de Computadores utilizando as classes Acer, Dell e Apple")

    @staticmethod
    def quem_sou():
        return "Sou um computador"

    @classmethod
    def pc_generico(cls):
        return cls("pentium","integrado","4")


    def Ram(self, new_ram):
        return "Fui de {0} para {1} Gb de Ram ".format(self.ram, new_ram)
        self.ram = new_ram


class Dell(Computador):
    def __init__(self):
        self.processador = "intel"
        self.video = "RTX 3060"
        self.ram = 16

    def OS(self):
        return "I use Windows"

    def quem_sou(self):
        return super().quem_sou() + " da marca Dell"


class Acer(Computador):
    def __init__(self):
        self.processador = "amd"
        self.video = "gtx 1080"
        self.ram = 8

    def OS(self):
        return "I use Windows"

    def quem_sou(self):
        return super().quem_sou() + " da marca Acer"

class Apple(Computador):
    def __init__(self):
        self.processador = "M1"
        self.video = "M1 Graphics"
        self.ram = 32

    def OS(self):
        return "I use MacOS"

    def quem_sou(self):
        return super().quem_sou() + " da marca Apple"


Computador.help()

pc1 = Dell()
pc2 = Acer()
pc3 = Dell()
pc4 = Apple()
pc5 = Computador.pc_generico()

print(pc1.quem_sou())
print(pc1.Ram(32))

print(pc2.quem_sou())

print(pc3.quem_sou())

print(pc5.quem_sou())

print(pc4.OS())




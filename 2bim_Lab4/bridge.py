#classe abstrata de veciulo e suas hierarquias concretas
#Nota-se que todo veiculo possui um parametro motor que é uma instancia da classe Motor, mostrando o design pattern Bridge
class Veiculo:
    def __init__(self):
        self.motor = Motor()
    
class Carro(Veiculo):
    def getDesc(self):
        return self.__class__.__name__

class Moto(Veiculo):
    def getDesc(self):
        return self.__class__.__name__
        

class Caminhao(Veiculo):
    def getDesc(self):
        return self.__class__.__name__
        

#Classe abstrata de motores e suas hierarquias concretas
class Motor:
    pass

class Hibrido(Motor):
    def getDesc(self):
        return self.__class__.__name__

class Eletrico(Motor):
    def getDesc(self):
        return self.__class__.__name__

class Combustao(Motor):
    def getDesc(self):
        return self.__class__.__name__

#Fabrica concreta de veiculos eletricos
class EletricoFactory:

    def createCarro(self):
        self.carro = Carro()
        self.carro.motor = Eletrico()
        return self.carro

    def createMoto(self):
        self.moto = Moto()
        self.moto.motor = Eletrico()
        return self.moto

    def createCaminhao(self):
        self.caminhao = Caminhao()
        self.caminhao.motor = Eletrico()
        return self.caminhao

#Fabrica concreta de veiculos hibridos
class HibridoFactory:

    def createCarro(self):
        self.carro = Carro()
        self.carro.motor = Hibrido()
        return self.carro

    def createMoto(self):
        self.moto = Moto()
        self.moto.motor = Hibrido()
        return self.moto

    def createCaminhao(self):
        self.caminhao = Caminhao()
        self.caminhao.motor = Hibrido()
        return self.caminhao   

#Fabrica concreta de veiculos a combustao
class CombustaoFactory:

    def createCarro(self):
        self.carro = Carro()
        self.carro.motor = Combustao()
        return self.carro

    def createMoto(self):
        self.moto = Moto()
        self.moto.motor = Combustao()
        return self.moto

    def createCaminhao(self):
        self.caminhao = Caminhao()
        self.caminhao.motor = Combustao()
        return self.caminhao

class Interface:
    def __init__(self):
        self.Cfac = CombustaoFactory()
        self.Hfac = HibridoFactory()
        self.Efac = EletricoFactory()

#utilização das fabricas pelo usuario para criar objetos

user = Interface()
Carro1 = user.Cfac.createCarro()
Moto1 = user.Efac.createMoto()
Carro2 = user.Efac.createCarro()
Caminhao1 = user.Hfac.createCaminhao()

print(Carro1.getDesc())
print(Carro2.getDesc())
print(Moto1.getDesc())
print(Caminhao1.getDesc())
print(Carro1.motor.getDesc())
print(Caminhao1.motor.getDesc())

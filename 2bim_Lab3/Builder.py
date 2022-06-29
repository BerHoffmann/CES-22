class Bolo:
    def __init__(self):
        self.sabor
        self.cobertura

class Builder:
    def __init__(self):
        self.bolo = Bolo()
    
    def setSabor(self, massa):
        self.bolo.sabor = massa
    
    def setCobertura(self,tema):
        self.bolo.cobertura = tema
    
    def getBolo(self):
        return self.bolo


class Director:
    def __init__(self):
        self.builder = Builder()

    def makeCenouraCasamento(self):
        self.builder.setSabor("cenoura")
        self.builder.setCobertura("Casamento")
        return self.builder.getBolo()
    
    def makeCenouraAniversario(self):
        self.builder.setSabor("cenoura")
        self.builder.setCobertura("Aniversario")
        return self.builder.getBolo()

    def makeChocolateCasamento(self):
        self.builder.setSabor("Chocolate")
        self.builder.setCobertura("Casamento")
        return self.builder.getBolo()

    def makeMandiocaInformal(self):
        self.builder.setSabor("Mandioca")
        self.builder.setCobertura("Informal")
        return self.builder.getBolo()

    


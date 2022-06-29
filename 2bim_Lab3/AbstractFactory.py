class AbstractFactory:

    def create_bolo_chocolate(self):
        pass

    def create_bolo_cenoura(self):
        pass

    def create_bolo_mandioca(self):
        pass

class FactoryAniversario(AbstractFactory):
    def create_bolo_chocolate(self):
        bolo = ChocolateAniversario()
        return bolo
    def create_bolo_cenoura(self):
        bolo = CenouraAniversario
        return bolo

    def create_bolo_mandioca(self):
        bolo = MandiocaAniversario
        return bolo

class FactoryCasamento(AbstractFactory):
    def create_bolo_chocolate(self):
        bolo = ChocolateCasamento()
        return bolo

    def create_bolo_cenoura(self):
        bolo = CenouraCasamento()
        return bolo

    def create_bolo_mandioca(self):
        bolo = MandiocaCasamento()
        return bolo

class FactoryInformal(AbstractFactory):
    def create_bolo_chocolate(self):
        bolo = ChocolateInformal()
        return bolo

    def create_bolo_cenoura(self):
        bolo = CenouraInformal()
        return bolo

    def create_bolo_mandioca(self):
        bolo = MandiocaInformal()
        return bolo


class BoloDeCenoura:
    pass

class CenouraAniversario(BoloDeCenoura):
    pass
class CenouraCasamento(BoloDeCenoura):
    pass
class CenouraInformal(BoloDeCenoura):
    pass


class BoloDeChocolate:
    pass

class ChocolateAniversario(BoloDeChocolate):
    pass
class ChocolateCasamento(BoloDeChocolate):
    pass
class ChocolateInformal(BoloDeChocolate):
    pass


class BoloDeMandioca:
    pass

class MandiocaAniversario(BoloDeMandioca):
    pass
class MandiocaCasamento(BoloDeMandioca):
    pass
class MandiocaInformal(BoloDeMandioca):
    pass



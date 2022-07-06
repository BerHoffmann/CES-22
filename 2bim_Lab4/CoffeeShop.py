#Classe de componentes da pizza
class PizzaComponent:
    def getDesc(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost
#Classe filha da componente, presente em todas as pizzas
class Massa(PizzaComponent):
    cost = 0.0

#Classe de componentes da pizza decorator, que poderá adicionar diversos ingredientes com o estilo Wrapper
class Decorator(PizzaComponent):
    def __init__(self,component):
        self.component = component
    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)
    def getDesc(self):
        return self.component.getDesc() + ' ' + PizzaComponent.getDesc(self)

#Classes dos ingredientes, herança do decorator
class Queijo(Decorator):
    cost = 10.0
    def __init(self, component):
        Decorator.__init__(self,component)

class Tomate(Decorator):
    cost = 5.0
    def __init(self, component):
        Decorator.__init__(self,component)

class Calabresa(Decorator):
    cost = 12.0
    def __init(self, component):
        Decorator.__init__(self,component)

class Frango(Decorator):
    cost = 9.0
    def __init(self, component):
        Decorator.__init__(self,component)

class Catupiry(Decorator):
    cost = 20.0
    def __init(self, component):
        Decorator.__init__(self,component)


#instanciacoes de objetos
calafrango = Frango(Calabresa(Queijo(Massa())))
print(calafrango.getDesc() + " : $" + str(calafrango.getTotalCost()))

frangoCatupiry = Frango(Queijo(Catupiry(Massa())))
print(frangoCatupiry.getDesc() + " : $" + str(frangoCatupiry.getTotalCost()))

margherita = Queijo(Tomate(Massa()))
print(margherita.getDesc() + " : $" + str(margherita.getTotalCost()))
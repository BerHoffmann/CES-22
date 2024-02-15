def decorador(funcao):
    def function_wrapper(*args, **kwargs):
    #decorator que junta todas as strings em uma so e a printa
        string = ""
        for strings in args:
            string += strings
        for strings in kwargs.values():
            string += strings
        print(string)
        funcao(*args,**kwargs)
    return function_wrapper

@decorador
def funcao(*args, **kwargs):
    for string in args:
        print(list(string))
    for string in kwargs.values():
        print(list(string))


funcao("lista","de","CES", "lista")

funcao("lista e dicionario", a = "de", c = "CES")

funcao(a = "lista", b = "de",c = "CES", d = "dicionario" )
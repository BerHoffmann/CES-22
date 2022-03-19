import math

def is_prime(n):
    """
    Verifica se n é primo, dividindo-o por todos os inteiros até o teto
    de sua raiz quadrada
    """
    bool = True

    if n == 1 or n == 0:
        bool = False
        return bool

    t = math.sqrt(n)
    t = math.ceil(t)

    for i in range(t):
        if (i+2) == n:
            return bool
        if n % (i+2) == 0:
            bool = False
            return bool
    return bool

numero = int(input("Type an integer to know if it is a prime number "))
bool = is_prime(numero)

if bool == True:
    print("True")
else:
    print("False")
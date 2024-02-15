def sum_to(n):
    """
    realiza a soma de todos os inteiros de 1 até 'n',
    inclusive, e retorna o resultado
    """
    sum = 0
    for i in range(n):
        sum = sum + (i + 1)
    return sum

numero = int(input("Type an integer to find the sum of all the integers from 1 up to that number inclusive: "))
soma = sum_to(numero)
print(soma)
def is_palindromo(palavra):
    """
    Verifica se a string 'palavra' é um palíndromo,
    comparando os caracteres de suas extremidades até o meio
    """
    bool = True
    for i in range(int(len(palavra) / 2)):
        if palavra[i] != palavra[(len(palavra) - 1) - i]:
            bool = False
            return bool
    return bool


palavra = input("Type something to find if it is a palindrome ")
bool = is_palindromo(palavra)

if bool == True:
    print(palavra, "is a palindrome!")
else:
    print(palavra, "is NOT a palindrome!")



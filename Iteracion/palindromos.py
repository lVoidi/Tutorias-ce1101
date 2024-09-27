"""
Ejemplo: Cómo saber si un número es palíndromo utilizando iteración.
"""

def es_palindromo(n):
    if not isinstance(n, int):
        return -1
    
    reverso = 0
    temp = n
    
    while temp > 0:
        reverso = reverso * 10 + temp % 10
        """
        121
        
        temp = 121
        reverso = 0
        
        reverso = 0 * 10 + 1 = 1
        
        reverso = 1 * 10 + 2 = 12

        reverso = 12 * 10 + 1 = 121
        
        """
        
        print(reverso)
        temp //= 10
    
    return n == reverso
    

def palindromo_string(string):
    if not isinstance(string, str):
        return -1
    
    return string == string[::-1]


def palindromo_lista(lista):
    if not isinstance(lista, list):
        return -1

    reverso = []
    
    for i in range(len(lista)):
        indice_actual = len(lista) - i - 1
        reverso.append(lista[indice_actual])
    
    return lista == reverso

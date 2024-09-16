"""
Ejercicios de recursividad para examen.
Rodrigo Arce

t.me/roarba

Este documento está protegido bajo la licencia GPL 3.0.
"""


"""
Primer ejercicio. Elaborar una función llamada hay_par que agarre una lista 
y devuelva True si hay un número par en la lista, False en caso contrario. 
"""

"""
Ejemplo de pila con índices
"""

def hay_par_pila(lista):
    if isinstance(lista, list):
        return hay_par_pila_aux(lista, 0)
    else:
        return "Error"

def hay_par_pila_aux(lista, indice):
    if indice == len(lista):
        return False
    
    elif lista[indice] % 2 == 0:
        return True
    else:
        return hay_par_pila_aux(lista, indice + 1)

# print(hay_par_pila([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print("------------------------------------------------")
# print(hay_par_pila([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))

"""
Ejemplo utilizando recursividad de cola y slicing.
"""
def hay_par_cola(lista):
    if isinstance(lista, list):
        return hay_par_cola_aux(lista)
    else:
        return "Error"
    

def hay_par_cola_aux(lista):
    if lista == []:
        return False
    elif lista[0] % 2 == 0:
        return True
    else:
        return hay_par_cola_aux(lista[1:])

# print(hay_par_cola([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print("------------------------------------------------")
# print(hay_par_cola([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))


"""
Segundo ejercicio. Elaborar una función llamada revise_num que 
reciba un número y devuelva una tupla de la forma (a, b) donde 
a es la cantidad de ceros y b es la cantidad de otros digitos.
"""

"""
Para este ejercicio, no hay versión de pila.
"""

def revise_num_cola(numero):
    if isinstance(numero, int):
        return revise_num_cola_aux(numero, 0, 0)
    else:
        return "Error"


def revise_num_cola_aux(numero, ceros, otros):
    if numero == 0:
        return (ceros, otros)
    elif numero % 10 == 0:
        return revise_num_cola_aux(numero // 10, ceros + 1, otros)
    else:
        return revise_num_cola_aux(numero // 10, ceros, otros + 1)
    
# print(revise_num_cola(100))
# print("------------------------------------------------")
# print(revise_num_cola(1234567890))



"""
Tercer ejercicio. Escriba una función llamada divida(num, dig) que devuelva 
una tupla con los dígitos mayores al número dado y los dígitos menores al número dado.
No debe ser un contador, se debe formar un nuevo digito a partir de los dígitos 
que cumplan la condicion
"""

"""
Version de cola. Este ejercicio también solo se puede hacer de cola.
"""

def divida(num, dig):
    if isinstance(num, int) and isinstance(dig, int):
        return divida_aux(num, dig, 0, 0, 0, 0)
    else:
        return "Error"
    
def divida_aux(num, dig, menores, mayores, exp_mayores, exp_menores):
    if num == 0:
        return (menores, mayores)
    
    elif num % 10 < dig:
        return divida_aux(num // 10, dig, (num % 10)*(10**exp_menores) + menores, mayores, exp_mayores, exp_menores + 1)
    else:
        return divida_aux(num // 10, dig, menores, (num % 10)*(10**exp_mayores) + mayores, exp_mayores + 1, exp_menores)


# print(divida(1234567890, 5))
# print("------------------------------------------------")
# print(divida(1234567890, 5))


"""
Cuarto ejercicio. Escriba una función llamada parejas(num) que 
reciba un numero y cuente la cantidad de parejas que hay en el número.
"""

def parejas(num):
    if isinstance(num, int):
        return parejas_aux(num, 0)
    else:
        return "Error"
    
def parejas_aux(num, parejas):
    if num == 0:
        return parejas
    elif (num // 10 != 0) and num % 10 == (num // 10) % 10:
        return parejas_aux(num // 100, parejas + 1)
    else:
        return parejas_aux(num // 100, parejas)

# print(parejas(112233445566778899))
# print("------------------------------------------------")
# print(parejas(1234567890))


"""
Quinto ejercicio. Haga una función que se llama  forme1 que tome una lista
y cree una nueva lista con todos los unos que hay en la lista original.
"""

"""
Version de cola y slicing
"""

def forme1(lista):
    if isinstance(lista, list):
        return forme1_aux(lista, [])
    else:
        return "Error"

def forme1_aux(lista, nueva_lista):
    if lista == []:
        return nueva_lista
    elif lista[0] == 1:
        return forme1_aux(lista[1:], nueva_lista + [1])
    else:
        return forme1_aux(lista[1:], nueva_lista)


"""
Version de pila con índices
"""

def forme1_pila(lista):
    if isinstance(lista, list):
        return forme1_pila_aux(lista, 0)
    else:
        return "Error"

def forme1_pila_aux(lista, indice):
    if indice == len(lista):
        return []
    elif lista[indice] == 1:
        return [lista[indice]] + forme1_pila_aux(lista, indice + 1)
    else:
        return forme1_pila_aux(lista, indice + 1)

# print(forme1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print("------------------------------------------------")
# print(forme1([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

# print(forme1_pila([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print("------------------------------------------------")
# print(forme1_pila([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))


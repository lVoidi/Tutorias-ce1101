"""
Lista de ejercicios con matrices para la clase de iteración.
"""

"""
Ejercicio 1. Crea una función que reciba una matriz y devuelva la suma de todos los elementos de la matriz.
"""

def suma_matriz(matriz):
    ...
    
# Prueba
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
assert suma_matriz(matriz) == 45

"""
Ejercicio 2. Crea una función que reciba una matriz y devuelva la suma de los elementos de cada fila.
Cada suma debe ser guardada en una lista.
"""
def suma_filas(matriz):
    ...

# Prueba
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
assert suma_filas(matriz) == [6, 15, 24]

"""
Ejercicio 3. Una matriz recibe el nombre de matriz identidad si todos los elementos de la diagonal principal
son 1 y todos los demás elementos son 0. Crea una función que reciba una matriz y devuelva True si es una
matriz identidad y False en caso contrario. La matriz debe ser cuadrada.
"""
def matriz_identidad(matriz):
    ...

# Prueba
matriz = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
assert matriz_identidad(matriz) == True

"""
Ejercicio 4. Crea una función que reciba una matriz y devuelva la suma de los elementos de la diagonal principal.
"""

def suma_diagonal(matriz):
    ...
    
# Prueba
matriz = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

assert suma_diagonal(matriz) == 3

"""
Ejercicio 5. Crea una funcion llamada sustitucion, que reciba una matriz, un elemento y un nuevo elemento.
Por cada aparición del elemento en la matriz, debe ser sustituido por el nuevo elemento. La función debe
devolver la matriz modificada.
"""

def sustitucion(matriz, elemento, nuevo_elemento):
    ...

# Prueba
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
nueva_matriz = sustitucion(matriz, 5, 0)
assert nueva_matriz == [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]
    
"""
Ejercicio 6. Resta de matrices. Una funcion llamada resta_matrices que reciba dos matrices y devuelva una nueva
matriz que sea la resta de las dos matrices. Si las matrices no tienen las mismas dimensiones, la función debe
devolver None.
"""

def resta_matrices(matriz1, matriz2):
    ...
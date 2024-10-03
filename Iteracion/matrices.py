"""
Lista de ejercicios con matrices para la clase de iteración.
"""

"""
Ejercicio 1.
Crea una función que reciba una matriz
y devuelva la suma de todos los elementos de la matriz.
"""


def suma_matriz(matriz: list) -> int:
    if not matriz:
        return -1
    suma = 0
    filas, columnas = len(matriz), len(matriz[0])

    # Para las matrices, siempre es recomendable
    # recorrerlas usando indices, en vez de iterarla
    # directamente con un for
    for i in range(filas):
        for j in range(columnas):
            item = matriz[i][j]
            suma += item
    return suma


# Prueba
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

assert suma_matriz(matriz) == 45

"""
Ejercicio 2. Crea una función que reciba una matriz
y devuelva la suma de los elementos de cada fila.
Cada suma debe ser guardada en una lista.
"""


def suma_filas(matriz: int) -> list:
    suma = []
    filas, columnas = len(matriz), len(matriz[0])

    for i in range(filas):
        suma_fila = 0
        for j in range(columnas):
            item = matriz[i][j]
            suma_fila += item
        suma.append(suma_fila)
    return suma


# Prueba
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert suma_filas(matriz) == [6, 15, 24]

"""
Ejercicio 3. Una matriz recibe el nombre de matriz identidad
si todos los elementos de la diagonal principal
son 1 y todos los demás elementos son 0.
Crea una función que reciba una matriz y devuelva True si es una
matriz identidad y False en caso contrario. La matriz debe ser cuadrada.
"""


def matriz_identidad(matriz: list) -> bool:
    filas, columnas = len(matriz), len(matriz[0])

    # Comprobamos que no esté vacía y que sea cuadrada
    if not matriz or filas != columnas:
        return False

    for i in range(filas):
        for j in range(columnas):
            item = matriz[i][j]

            # Comprueba si el elemento no cumple las condiciones
            if i == j and item != 1 or i != j and item != 0:
                return False

    return True


# Prueba
matriz = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
assert matriz_identidad(matriz)

matriz = [[1, 2, 3], [4, 9, 8], [3, 4, 5]]
assert not matriz_identidad(matriz)

"""
Ejercicio 4.
Crea una función que reciba una matriz y
devuelva la suma de los elementos de la diagonal principal.

NOTA: Una matriz solo tiene diagonal principal si es cuadrada
"""


def suma_diagonal(matriz: list) -> int:
    filas, columnas = len(matriz), len(matriz[0])
    if filas != columnas:
        return -1
    suma = 0
    for i in range(filas):
        for j in range(columnas):
            if i == j:
                item = matriz[i][j]
                suma += item
    return suma


# Prueba
matriz = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

assert suma_diagonal(matriz) == 3

"""
Ejercicio 5. Crea una funcion llamada sustitucion,
que reciba una matriz, un elemento y un nuevo elemento.
Por cada aparición del elemento en la matriz,
debe ser sustituido por el nuevo elemento. La función debe
devolver la matriz modificada.
"""


def sustitucion(matriz: list, elemento: int, nuevo_elemento: int) -> list:
    filas, columnas = len(matriz), len(matriz[0])
    resultadoado = matriz
    for i in range(filas):
        for j in range(columnas):
            item = matriz[i][j]
            if item == elemento:
                resultadoado[i][j] = nuevo_elemento

    return resultadoado


# Prueba
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nueva_matriz = sustitucion(matriz, 5, 0)
assert nueva_matriz == [[1, 2, 3], [4, 0, 6], [7, 8, 9]]

"""
Ejercicio 6. Resta de matrices. Una funcion llamada resta_matrices
que reciba dos matrices y devuelva una nueva
matriz que sea la resta de las dos matrices.
Si las matrices no tienen las mismas dimensiones, la función debe
devolver None.
"""


def resta_matrices(matriz_1: list, matriz_2: list) -> list:
    filas, columnas = len(matriz_1), len(matriz_1[0])
    if filas != len(matriz_2) or columnas != len(matriz_2[0]):
        return []

    resultado = matriz_1
    for i in range(filas):
        for j in range(columnas):
            item_1, item_2 = matriz_1[i][j], matriz_2[i][j]
            resultado[i][j] = item_1 - item_2
    return resultado


matriz_1 = [[1, 2], [3, 4]]
matriz_2 = [[0, 1], [2, 3]]

assert resta_matrices(matriz_1, matriz_2) == [[1, 1], [1, 1]]


"""
Ejercicio 7. Crea una función que reciba una matriz.
Debe devolver el valor menor, el valor mayor y
el promedio de la matriz.
"""


def ejercicio_examen(matriz: int) -> tuple:
    if not matriz:
        return (0, 0, 0)

    filas, columnas = len(matriz), len(matriz[0])
    cantidad = filas * columnas
    suma, mayor, menor = 0, matriz[0][0], matriz[0][0]

    for i in range(filas):
        for j in range(columnas):
            item = matriz[i][j]
            suma += item
            mayor = item if item > mayor else mayor
            menor = item if item < menor else menor

    return (suma / cantidad, mayor, menor)


# Prueba
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert ejercicio_examen(matriz) == (5.0, 9, 1)


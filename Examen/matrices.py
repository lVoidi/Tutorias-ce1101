"""
En este documento, encontraran ejercicios relacionados con matrices. 

Los ejercicios los vamos a categorizar por estrellas. 

* Ejercicios básicos
** Ejercicios intermedios
*** Ejercicios avanzados

TODO Instrucciones:
- Hacer un fork del repositorio de Github
- Clonar el repositorio (fork) en su computadora
- Crear una rama con su nombre
- Hacer un commit por cada ejercicio resuelto 
- Hacer un push de la rama al repositorio de Github fork, una vez que hayan resuelto todos los ejercicios deseados
- Crear un pull request de la rama al repositorio original 
- En el mensaje del pull request, poner su nombre completo y carné 

Ejemplo de mensaje de commit:
git commit -m "Ejercicio básico 1 resuelto"
git push origin nombre_rama

Ejemplo de mensaje de pull request:
Nombre completo: Juan Pérez 202xxxxxxx

Notas: Recordemos cómo iterar matrices 

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        elemento = matrix[i][j]
        
Para acceder a un elemento de una matriz, se hace de la siguiente forma:
matrix[fila][columna]

Matrices cuadradas: Son matrices en las que la cantidad de filas es igual a la cantidad de columnas.
Matrices rectangulares: Son matrices en las que la cantidad de filas es diferente a la cantidad de columnas.
Matriz identidad: Es una matriz cuadrada en la que todos los elementos de la diagonal principal son 1 y el resto de los elementos son 0.
Matriz nula: Es una matriz en la que todos los elementos son 0.
Matriz triangular superior: Es una matriz cuadrada en la que todos los elementos por debajo de la diagonal principal son 0.
Matriz triangular inferior: Es una matriz cuadrada en la que todos los elementos por encima de la diagonal principal son 0.
"""

# ------------------ Ejercicios básicos (*) ------------------

# TODO: Ejercicio básico 1: Imprimir una matriz en consola 
# Crear una función que reciba una matriz y la imprima en consola.
# Para esto, debe verse como una matriz matemática, es decir, con los corchetes y separados por espacios
# en blanco.
# Ejemplo:
# Si la matriz es [[1, 2], [3, 4]], la función debe imprimir:
# [1 2]
# [3 4]
# https://www.w3schools.com/python/ref_func_print.asp
def print_matrix(matrix: list) -> None:
    
    result = ""
    for i in range(len(matrix)):
        result += "["
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1:
                result += f"{matrix[i][j]}"
            else:
                result += f"{matrix[i][j]} "
        result += "]\n"
    print(result)

# Casos de prueba:
print_matrix([[1, 2], [3, 4]])
    
# Nota 1: Pueden usar la función print_matrix para probar los ejercicios que siguen.
# Nota 2: En python pueden utilizar las type annotations. Esto lo que nos permite es definir el tipo de dato
# que va a recibir la función y el tipo de dato que va a devolver.
# Por ejemplo, en la función print_matrix, el parámetro matrix va a ser una lista y la función no va a devolver nada (None).
# Esto permite a nuestro IDE (entorno de desarrollo) saber si estamos pasando los parámetros correctos a la función y si estamos
# devolviendo el tipo de dato correcto. Además, podemos utilizar las funciones de ayuda de nuestro IDE para saber que métodos
# y atributos tiene un objeto de un tipo específico.


# TODO: Ejercicio básico 2: Crear una matriz de ceros
# Dada una cantidad de filas y columnas, crear una matriz de ceros.
# Ejemplo:
# Si la cantidad de filas es 2 y la cantidad de columnas es 3, la matriz debe ser:
# [[0, 0, 0],
#  [0, 0, 0]]
def zeros_matrix(rows: int, cols: int) -> list:
    ...
    
# Casos de prueba:
# zeros_matrix(2, 3) debe devolver [[0, 0, 0], [0, 0, 0]]
# zeros_matrix(3, 2) debe devolver [[0, 0], [0, 0], [0, 0]]
# zeros_matrix(3, 3) debe devolver [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# TODO: Ejercicio básico 3: Crear una matriz identidad
# Dada una cantidad de filas y columnas, crear una matriz identidad.
# La matriz identidad n x n es una matriz cuadrada de tamaño n x n 
# que tiene 1 en la diagonal principal y 0 en el resto de las posiciones.
# Ejemplo:
# Si la cantidad de filas es 3 y la cantidad de columnas es 3, la matriz debe ser:
# [[1, 0, 0],
#  [0, 1, 0],
#  [0, 0, 1]]

def identity_matrix(n: int) -> list:
    ...
    
# Casos de prueba:
# identity_matrix(2) debe devolver [[1, 0], [0, 1]]
# identity_matrix(3) debe devolver [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# identity_matrix(4) debe devolver [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

# ------------------ Ejercicios intermedios (**) ------------------

# TODO: Ejercicio intermedio 1: Sumar dos matrices
# Dadas dos matrices de la misma dimensión, sumarlas y devolver una nueva matriz con el resultado.
# Ejemplo:
# Si la matriz A es [[1, 2], [3, 4]] y la matriz B es [[5, 6], [7, 8]], la función debe devolver:
# [[6, 8], [10, 12]]

def sum_matrices(matrix_a: list, matrix_b: list) -> list:
    ...
    
# Casos de prueba:
# sum_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]) debe devolver [[6, 8], [10, 12]]
# sum_matrices([[1, 2], [3, 4]], [[1, 1], [1, 1]]) debe devolver [[2, 3], [4, 5]]
# sum_matrices([[1, 1], [1, 1]], [[1, 1], [1, 1]]) debe devolver [[2, 2], [2, 2]]

# TODO Ejercicio intermedio 2: Transponer una matriz
# Dada una matriz, devolver una nueva 
# matriz que sea la transpuesta de la matriz original.
# La matriz transpuesta es aquella en la que las filas de la matriz original
# son las columnas de la matriz transpuesta y viceversa.

# Ejemplo:
# Si la matriz es [[1, 2], [3, 4], [5, 6]], la función debe devolver:
# [[1, 3, 5], [2, 4, 6]]

def transpose_matrix(matrix: list) -> list:
    ...
    
# Casos de prueba:
# transpose_matrix([[1, 2], [3, 4], [5, 6]]) debe devolver [[1, 3, 5], [2, 4, 6]]
# transpose_matrix([[1, 2, 3], [4, 5, 6]]) debe devolver [[1, 4], [2, 5], [3, 6]]
# transpose_matrix([[1, 2], [3, 4], [5, 6], [7, 8]]) debe devolver [[1, 3, 5, 7], [2, 4, 6, 8]]


# TODO Ejercicio intermedio 3: Multiplicar una matriz por un escalar
# Dada una matriz y un escalar, multiplicar la matriz por el escalar y devolver una nueva matriz con el resultado.
# Ejemplo:
# Si la matriz es [[1, 2], [3, 4]] y el escalar es 2, la función debe devolver:
# [[2, 4], [6, 8]]

def multiply_matrix_by_scalar(matrix: list, scalar: int) -> list:
    ...
    
# Casos de prueba:
# multiply_matrix_by_scalar([[1, 2], [3, 4]], 2) debe devolver [[2, 4], [6, 8]]
# multiply_matrix_by_scalar([[1, 2], [3, 4]], 3) debe devolver [[3, 6], [9, 12]]
# multiply_matrix_by_scalar([[1, 2], [3, 4]], 0) debe devolver [[0, 0], [0, 0]]


# TODO Ejercicio intermedio 4: Escriba una función llamada lt_five que reciba una matriz y devuelva True si todos los elementos
# de la matriz son menores a 5 y False en caso contrario.
# Ejemplo:
# Si la matriz es [[1, 2], [3, 4]], la función debe devolver True
# Si la matriz es [[1, 2], [3, 4], [5, 6]], la función debe devolver False

def lt_five(matrix: list) -> bool:
    ...

# Casos de prueba:
# lt_five([[1, 2], [3, 4]]) debe devolver True
# lt_five([[1, 2], [3, 4], [5, 6]]) debe devolver False
# lt_five([[1, 2], [3, 4], [5, 6], [7, 8]]) debe devolver False

# TODO Ejercicio intermedio 5: Escriba una función llamada sum_diagonal que reciba una matriz cuadrada y devuelva la suma de los elementos
# de la diagonal principal de la matriz. 
# Ejemplo:
# Si la matriz es [[1, 2], [3, 4]], la función debe devolver 5

def sum_diagonal(matrix: list) -> int:
    ...

# Casos de prueba:
# sum_diagonal([[1, 2], [3, 4]]) debe devolver 5
# sum_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) debe devolver 15
# sum_diagonal([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) debe devolver 34

# HINT: Recuerda que la diagonal principal de una matriz es aquella en la que la fila y la columna son iguales.

# TODO Ejercicio intermedio 6: Escriba una función llamada sup_triangular_matrix que reciba una matriz cuadrada y devuelva True si la matriz es
# triangular superior y False en caso contrario. Una matriz es triangular superior si todos los elementos por debajo de la diagonal principal
# son 0.

def sup_triangular_matrix(matrix: list) -> bool:
    ...
    
# Casos de prueba:
# sup_triangular_matrix([[1, 2], [0, 4]]) debe devolver True
# sup_triangular_matrix([[1, 2], [3, 4]]) debe devolver False
# sup_triangular_matrix([[1, 2, 3], [0, 4, 5], [0, 0, 6]]) debe devolver True
# sup_triangular_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) debe devolver False


# TODO Ejercicio intermedio 7: Cree una funcion que reciba una matriz de unos y ceros e intercambie los unos 
# por ceros y los ceros por unos. La función debe devolver la matriz modificada.
# Ejemplo:
# Si la matriz es [[1, 0], [0, 1]], la función debe devolver [[0, 1], [1, 0]]

def swap_zeros_ones(matrix: list) -> list:
    ...
    
# Casos de prueba:
# swap_zeros_ones([[1, 0], [0, 1]]) debe devolver [[0, 1], [1, 0]]
# swap_zeros_ones([[1, 1], [0, 0]]) debe devolver [[0, 0], [1, 1]]
# swap_zeros_ones([[0, 0], [0, 0]]) debe devolver [[1, 1], [1, 1]]
# swap_zeros_ones([[1, 1], [3, 2]]) debe devolver error


# ------------------ Ejercicios avanzados (***) ------------------

# TODO: Ejercicio Avanzado 1: Multiplicar dos matrices
# Dadas dos matrices, multiplicarlas y devolver una nueva matriz con el resultado.
# Para poder multiplicar dos matrices, la cantidad de columnas de la primera matriz
# debe ser igual a la cantidad de filas de la segunda matriz. 
# Ejemplo:
# Si la matriz A es [[1, 2], [3, 4]] y la matriz B es [[5, 6], [7, 8]], la función debe devolver:
# [[19, 22], [43, 50]]

"""
¿CÓMO SE MULTIPLICAN MATRICES?
Para multiplicar dos matrices, se multiplica cada elemento de la fila de la primera matriz
por cada elemento de la columna de la segunda matriz. El resultado de esta multiplicación
se suma y se coloca en la posición correspondiente de la matriz resultante. 

Por ejemplo, si queremos multiplicar la matriz A de 2x2 por la matriz B de 2x2, el resultado
de la matriz C será de 2x2.

A = [[a, b],
     [c, d]]
     
B = [[e, f],
     [g, h]]

C = [[a*e + b*g, a*f + b*h],
     [c*e + d*g, c*f + d*h]]
     
     
Pseudocódigo:
1. Crear una matriz de ceros de tamaño len(matrix_a) x len(matrix_b[0])
2. Por cada fila i de la matriz A:
3. Por cada columna j de la matriz B:
4. Por cada fila k de la matriz B:
5. Sumar el producto de matrix_a[i][k] * matrix_b[k][j] a la posición resultado[i][j]
6. Devolver la matriz resultado

Recuerda comprobar que la cantidad de columnas de la matriz A sea igual a la cantidad de filas de la matriz B
(osea, A es de nxm y B es de mxp, entonces la matriz resultante C será de nxp)
"""

def multiply_matrices(matrix_a: list, matrix_b: list) -> list:
    resultado = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]
    ...

# Casos de prueba:
# multiply_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]) debe devolver [[19, 22], [43, 50]]
# multiply_matrices([[1, 2], [3, 4]], [[1, 1], [1, 1]]) debe devolver [[3, 3], [7, 7]]
# multiply_matrices([[1, 1], [1, 1]], [[1, 1], [1, 1]]) debe devolver [[2, 2], [2, 2]]

# ------------------ FIN ------------------
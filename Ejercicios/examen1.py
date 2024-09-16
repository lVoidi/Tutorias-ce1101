"""
Primer ejercicio. De entrada se recibe una matriz de puntos de la forma [(x1, y1), (x2, y2), ..., (xn, yn)].
Esta matriz pertenece al juego Super Pang. Se pide una función que devuelva los pares ordenados que representan
un muro en el juego. Se debe hacer de manera recursiva.

Para esto, la función debe recibir el largo y el ancho de la matriz. Digamos que la matriz es mxn. Entonces, pared
serían los siguientes puntos:
[0, 0], [0, 1], [0, 2], ...[0, n-1],
[1, 0], [2, 0], [3, 0], ...[m-1, 0],
[0, n-1], [1, n-1], [2, n-1], ...[m-1, n-1],
[m-1, 0], [m-1, 1], [m-1, 2], ...[m-1, n-1]

Ejemplo: 
0 1 2 3 ...                                               n-1
############################################################ 0
#..........................................................#.1
#..........................................................#.2
#..........................................................#.3
#..........................................................#.4
#..........................................................#.5
#..........................................................#....
#..........................................................#.
#..........................................................#.
############################################################ m-1
"""


def paredes(muro, largo, ancho):
    if isinstance(muro, list) and isinstance(largo, int) and isinstance(ancho, int):
        return paredes_aux(muro, largo, ancho, 0, 0)
    else:
        return "Error"


def paredes_aux(muro, largo, ancho, i, j):
    if i == largo:
        return []
    elif j == ancho:
        return paredes_aux(muro, largo, ancho, i + 1, 0)
    elif (i == 0 or i == largo - 1) and (j == 0 or j == ancho - 1):
        return [[i, j]] + paredes_aux(muro, largo, ancho, i, j + 1)
    elif (i == 0 or i == largo - 1) or (j == 0 or j == ancho - 1):
        return [[i, j]] + paredes_aux(muro, largo, ancho, i, j + 1)
    else:
        return paredes_aux(muro, largo, ancho, i, j + 1)

# 16 x 16
prueba_1 = [
    [0, 0],
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [0, 5],
    [0, 6],
    [0, 7],
    [0, 8],
    [0, 9],
    [0, 10],
    [0, 11],
    [0, 12],
    [0, 13],
    [0, 14],
    [0, 15],
    [1, 0],
    [2, 0],
    [3, 0],
    [4, 0],
    [5, 0],
    [6, 0],
    [7, 0],
    [8, 0],
    [9, 0],
    [10, 0],
    [11, 0],
    [12, 0],
    [13, 0],
    [14, 0],
    [15, 0],
    [1, 15],
    [2, 15],
    [3, 15],
    [4, 15],
    [5, 15],
    [6, 15],
    [7, 15],
    [8, 15],
    [9, 15],
    [10, 15],
    [11, 15],
    [12, 15],
    [13, 15],
    [14, 15],
    [15, 15],
    [15, 1],
    [15, 2],
    [15, 3],
    [15, 4],
    [15, 5],
    [15, 6],
    [15, 7],
    [15, 8],
    [15, 9],
    [15, 10],
    [15, 11],
    [15, 12],
    [15, 13],
    [15, 14],
]

# 10 x 8
prueba_2 = [
    [0, 0],
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [0, 5],
    [0, 6],
    [0, 7],
    [1, 0],
    [2, 0],
    [3, 0],
    [4, 0],
    [5, 0],
    [6, 0],
    [7, 0],
    [1, 7],
    [2, 7],
    [3, 7],
    [4, 7],
    [5, 7],
    [6, 7],
    [7, 7],
]

# print(paredes(prueba_1, 16, 16))
# print("------------------------------------------------")
# print(paredes(prueba_2, 8, 10))


"""
Ejercicio 2. Trabajemos con listas, como si fueran conjuntos. Carlos quiere encontrar la intersección de dos conjuntos. Para esto, se pide
una función que reciba dos conjuntos y devuelva la intersección de ambos. Se debe hacer de manera recursiva. Para esto,
puede hacer una función recursiva llamada pertenece, que compruebe si un elemento x pertenece a un conjunto. Para esto,
iteramos sobre un solo conjunto. Si x pertenece a ese conjunto, entonces lo agregamos a la intersección. Si no, seguimos
iterando.
"""

def interseccion(A, B):
    if isinstance(A, list) and isinstance(B, list):
        return interseccion_aux(A, B, 0)
    else:
        return "Error"

def pertenece(x, C):
    if C == []:
        return False
    elif x == C[0]:
        return True
    else:
        return pertenece(x, C[1:])

def interseccion_aux(A, B, i):
    if i == len(A):
        return []
    elif pertenece(A[i], B):
        return [A[i]] + interseccion_aux(A, B, i + 1)
    else:
        return interseccion_aux(A, B, i + 1)
    
# print(interseccion([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
# print("------------------------------------------------")
# print(interseccion([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))

"""
Ejercicio 3. Imaginemos que recibimos una matriz que tiene la siguiente forma:
[98, 0] 
Donde 98 es la nota del estudiante de ID 0. Se pide una función recursiva que devuelva una lista de la siguiente
forma: 
[70.52, 33, 2, 5] donde 70.52 es el promedio de las notas, 33 es la cantidad de estudiantes que aprobaron (nota >= 60) 
y 2 es la cantidad de estudiantes que reprobaron (nota < 60). Además, el último elemento será el estudiante con la nota más alta.
"""

def promedio_notas(matriz):
    if isinstance(matriz, list):
        return promedio_notas_aux(matriz, 0, 0, 0, 0, 0, 0)
    else:
        return "Error"

def promedio_notas_aux(matriz, i, suma, aprobados, reprobados, nota_max, estudiante_max):
    if i == len(matriz):
        return [suma / len(matriz), aprobados, reprobados, estudiante_max]
    nota = matriz[i][0]
    if nota >= 60:
        if nota > nota_max:
            nota_max = nota
            estudiante_max = matriz[i][1]
        return promedio_notas_aux(matriz, i + 1, suma + nota, aprobados + 1, reprobados, nota_max, estudiante_max)
    else:
        return promedio_notas_aux(matriz, i + 1, suma + nota, aprobados, reprobados + 1, nota_max, estudiante_max)
    
# print(promedio_notas([[98, 0], [50, 1], [60, 2], [70, 3], [80, 4], [90, 5]]))
# print("------------------------------------------------")
# print(promedio_notas([[98, 0], [50, 1], [60, 2], [70, 3], [80, 4], [90, 5], [100, 6]]))



"""
Ejercicio 4. De repente, odiamos los números impares. Se pide una función recursiva que reciba una lista de números y devuelva
una lista con los números pares. 
"""

def pares(lista):
    if isinstance(lista, list):
        return pares_aux(lista, 0)
    else:
        return "Error"


def pares_aux(lista, i):
    if i == len(lista):
        return []
    elif lista[i] % 2 == 0:
        return [lista[i]] + pares_aux(lista, i + 1)
    else:
        return pares_aux(lista, i + 1)
    

# print(pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print("------------------------------------------------")
# print(pares([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))

"""
Ejercicio 5. Se recibe una matriz de cualquier tamaño y se pide una función recursiva que compruebe si todos 
los elementos de la matriz son cero o uno.
"""

def ceros_unos(matriz):
    if isinstance(matriz, list):
        return ceros_unos_aux(matriz, 0, 0)
    else:
        return "Error"
    
def ceros_unos_aux(matriz, i, j):
    if i == len(matriz):
        return True
    elif j == len(matriz[i]):
        return ceros_unos_aux(matriz, i + 1, 0)
    elif matriz[i][j] != 0 and matriz[i][j] != 1:
        return False
    else:
        return ceros_unos_aux(matriz, i, j + 1)
    
# print(ceros_unos([[0, 1, 0], [1, 0, 1], [0, 1, 0]]))
# print("------------------------------------------------")
# print(ceros_unos([[0, 1, 0], [1, 0, 1], [0, 1, 2]]))


"""
Ejercicio 6. Recibe una matriz de cualquier tamaño y se pide una función recursiva que devuelva las posiciones 
donde se encuentran numeros pares.
"""

def pares_posiciones(matriz):
    if isinstance(matriz, list):
        return pares_posiciones_aux(matriz, 0, 0)
    else:
        return "Error"

def pares_posiciones_aux(matriz, i, j):
    if i == len(matriz):
        return []
    elif j == len(matriz[i]):
        return pares_posiciones_aux(matriz, i + 1, 0)
    elif matriz[i][j] % 2 == 0:
        return [[i, j]] + pares_posiciones_aux(matriz, i, j + 1)
    else:
        return pares_posiciones_aux(matriz, i, j + 1)


# print(pares_posiciones([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print("------------------------------------------------")
# print(pares_posiciones([[1, 2, 3], [4, 5, 6], [7, 8, 10]]))


"""
Ejercicio 7. Toma una matriz de cualquier tamaño y elimina las filas de posición par
"""

def filas_pares(matriz):
    if isinstance(matriz, list):
        return filas_pares_aux(matriz, 0)
    else:
        return "Error"
    

def filas_pares_aux(matriz, i):
    if i == len(matriz):
        return []
    elif i % 2 == 0:
        return filas_pares_aux(matriz, i + 1)
    else:
        return [matriz[i]] + filas_pares_aux(matriz, i + 1)
    

# print(filas_pares([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print("------------------------------------------------")
# print(filas_pares([[1, 2, 3], [4, 5, 6], [7, 8, 10], [11, 12, 13]]))





"""
En este archivo se encuentran los ejercicios relacionados a vectores.

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
"""

# ------------------- Ejercicios básicos (*) -------------------
# TODO Ejericio 1: Crear una función que reciba como parámetros dos vectores y devuelva la suma de estos dos.
# La suma de dos vectores se realiza componente a componente.
# Ejemplo:
# v1 = [1, 2, 3]
# v2 = [4, 5, 6]
# suma_vectores(v1, v2) => [5, 7, 9]
def suma_vectores(v1: list, v2: list) -> list:
    result = []
    for i in range(len(v1)):
        result.append(v1[i] + v2[i])
    return result
    
# Casos de prueba
# v1 = [1, 2, 3]
# v2 = [4, 5, 6]
# print(suma_vectores(v1, v2)) # [5, 7, 9]

# TODO Ejericio 2: Crear una función que reciba como parámetros dos vectores y devuelva el producto punto de estos dos.
# El producto punto de dos vectores se realiza componente a componente y luego se suman los resultados.
# Ejemplo:
# v1 = [1, 2, 3]
# v2 = [4, 5, 6]
# producto_punto(v1, v2) => 32

def producto_punto(v1: list, v2: list) -> list:
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result
    

# Casos de prueba
# v1 = [1, 2, 3]
# v2 = [4, 5, 6]
# print(producto_punto(v1, v2)) # 32

# TODO Ejericio 3: Crear una función que reciba como parámetros un vector y un escalar y devuelva el producto de estos dos.
# El producto de un vector por un escalar se realiza multiplicando cada componente del vector por el escalar.
# Ejemplo:
# v = [1, 2, 3]
# escalar = 2
# producto_vector_escalar(v, escalar) => [2, 4, 6]

def producto_vector_escalar(v: list, escalar: int) -> list:
    result = []
    for i in range(len(v)):
        result.append(v[i] * escalar)
    return result
    
# Casos de prueba
# v = [1, 2, 3]
# escalar = 2
# print(producto_vector_escalar(v, escalar)) # [2, 4, 6]

# ------------------- Ejercicios intermedios (**) -------------------

# TODO Ejercicio 4: Sacar la magnitud de un vector. 
# La magnitud de un vector se obtiene a partir de la raíz cuadrada de la suma de los cuadrados de sus componentes.
# Ejemplo:
# v = [1, 2, 3]
# magnitud_vector(v) => 3.74 = sqrt(1^2 + 2^2 + 3^2)

def magnitud_vector(v: list) -> float:
    result = 0
    for i in range(len(v)):
        result += v[i] ** 2
    return result ** 0.5

# Casos de prueba
# v = [1, 2, 3]
# print(magnitud_vector(v)) # 3.74

# TODO Ejercicio 5: Para cada numero en posicion par, multiplicar por 2 y para cada numero en posicion impar multiplicar por 3

def multiplicar_posicion(v: list) -> list:
    result = []
    for i in range(len(v)):
        if i % 2 == 0:
            result.append(v[i] * 2)
        else:
            result.append(v[i] * 3)
    return result
    
# Casos de prueba
# v = [1, 2, 3, 4, 5]
# print(multiplicar_posicion(v)) # [3, 4, 9, 8, 15]

# TODO Ejercicio 6. A partir de un vector de números enteros, devolver un vector con solo los números pares.
def numeros_pares(v: list) -> list:
    result = []
    for i in v:
        if i % 2 == 0:
            result.append(i)
    return result

# Casos de prueba
# v = [1, 2, 3, 4, 5]
# print(numeros_pares(v)) # [2, 4]

# TODO Ejercicio 7. A partir de un vector de números enteros, devolver un vector con:
# 1. Media de los números
# 2. Menor número
# 3. Mayor número
def estadisticas(v: list) -> list:
    
    suma = 0 
    for i in v:
        suma += i
    
    media = suma / len(v)
    menor = v[0]
    mayor = v[0]
    
    for i in v:
        if i < menor:
            menor = i
        if i > mayor:
            mayor = i
            
    return [media, menor, mayor]
    
# Casos de prueba
# v = [1, 2, 3, 4, 5]
# print(estadisticas(v)) # [3.0, 1, 5]

# ------------------- Ejercicios avanzados (***) -------------------

# TODO Ejercicio 8: Haga las siguientes funciones: 
# 1. Menor elemento
# 2. Mayor elemento
# 3. Una función llamada swap_max_min, que va a intercambiar el menor valor del vector con el mayor valor del vector.

def menor_elemento(v: list) -> int:
    menor = v[0]
    for i in v:
        if i < menor:
            menor = i
    return menor

def mayor_elemento(v: list) -> int:
    mayor = v[0]
    for i in v:
        if i > mayor:
            mayor = i
    return mayor

def swap_max_min(v: list) -> list:
    result = v.copy() # hay que hacer una copia para no modificar el vector original
    min_idx = v.index(menor_elemento(v))
    max_idx = v.index(mayor_elemento(v))
    result[min_idx], result[max_idx] = result[max_idx], result[min_idx]
    return result

# Casos de prueba
# v = [1, 2, 3, 4, 5]
# print(menor_elemento(v)) # 1
# print(mayor_elemento(v)) # 5
# print(swap(1, 2)) # [2, 1, 3, 4, 5]
# print(swap_max_min(v)) # [5, 2, 3, 4, 1]

# TODO Ejercicio 9: Hacer una función que tome un vector y devuelva True si es simétrico y False si no lo es.
# Un vector es simétrico si es igual al vector invertido.
# 1. Invertir un vector
# 2. Verificar si un vector es simétrico
def invertir_vector(v: list) -> list:
    result = []
    for i in range(len(v) - 1, -1, -1):
        result.append(v[i])
    return result

def simetrico(v: list) -> bool:
    return v == invertir_vector(v)
    
# Casos de prueba
# v = [1, 2, 3, 2, 1]
# print(invertir_vector(v)) # [1, 2, 3, 2, 1]
# print(simetrico(v)) # True

# ------------------- Ejercicios extra (*****) -------------------

# TODO Ejercicio 10: Hacer una función que reciba dos vectores y devuelva True si son ortogonales y False si no lo son.
# Dos vectores son ortogonales si su producto punto es igual a 0.
def ortogonales(v1: list, v2: list) -> bool:
    return producto_punto(v1, v2) == 0
    
# Casos de prueba
# v1 = [1, 0]
# v2 = [0, 1]
# print(ortogonales(v1, v2)) # True

# TODO Ejercicio 11: Hacer una función que reciba dos vectores y devuelva True si son paralelos y False si no lo son.
# Dos vectores son paralelos si uno es múltiplo escalar del otro.
# Ejemplo:
# v1 = [1, 2, 3]
# v2 = [2, 4, 6]
# paralelos(v1, v2) => True

def paralelos(v1: list, v2: list) -> bool:
    for i in range(len(v1)):
        if v1[i] == 0 or v2[i] == 0:
            continue
        if v1[i] / v2[i] != v1[0] / v2[0]:
            return False
    return True

# Casos de prueba
# v1 = [1, 2, 3]
# v2 = [2, 4, 6]
# print(paralelos(v1, v2)) # True


# TODO Ejercicio 12: Haga una función que compruebe que todos los elementos de un vector son primos.
def es_primo(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
def primos(v: list) -> bool:
    for i in v:
        if not es_primo(i):
            return False
    return True
    
# Casos de prueba
# v = [2, 3, 5, 7, 11]
# print(primos(v)) # True

"""
Hacer una función que pase los numeros de decimal a binario 
"""

# Reto
def decimal_a_binario(num):
    if isinstance(num, int) and num > 0:
        return decimal_a_binario_aux(num, 0)
    
    else:
        return -1 


def decimal_a_binario_aux(num, exp):
    # if not num 
    if not num: 
        return 0 
    
    return (num % 2) * (10**exp) + decimal_a_binario_aux(num // 2, exp + 1)


print(decimal_a_binario(10)) # 1010


# Fibonacci de pila 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 
# Fn = Fn-1 + Fn-2

def fibonacci_pila(n):
    if isinstance(n, int) and n >= 0:
        return fibonacci_pila_aux(n)
    else:
        return -1

def fibonacci_pila_aux(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci_pila_aux(n-1) + fibonacci_pila_aux(n-2)


# Fibonacci cola 
def fibonacci_cola(n):
    if isinstance(n, int) and n >= 0:
        return fibonacci_cola_aux(n, 0, 1)
    else:
        return -1


def fibonacci_cola_aux(n, a, b):
    if n == 0:
        return a
    if n == 1:
        return b
    
    return fibonacci_cola_aux(n-1, b, a+b)



# Hacer una funcion factorial de pila
# n! = n*(n-1)*(n-2)*...*1
# 0! = 1
def factorial_pila(n):
    if isinstance(n, int) and n >= 0:
        return factorial_pila_aux(n)
    else:
        return -1

def factorial_pila_aux(n):
    if n <= 1:
        return 1
    
    return n * factorial_pila_aux(n-1)


# Versión de cola 
def factorial_cola(n):
    if isinstance(n, int) and n >= 0:
        return factorial_cola_aux(n, 1)
    else:
        return -1


def factorial_cola_aux(n, acc):
    if n <= 1:
        return acc
    
    return factorial_cola_aux(n-1, acc*n)



# Sumatoria que empieza en i = m hasta n en pila 

def sumatoria_pila(m, n):
    if isinstance(m, int) and isinstance(n, int) and m >= 0 and n >= 0:
        return sumatoria_pila_aux(m, n)
    else:
        return -1


def sumatoria_pila_aux(m, n):
    if m == n:
        return m
    
    return m + sumatoria_pila_aux(m+1, n)


# Sumatoria que empieza en i = m hasta n en cola
def sumatoria_cola(m, n):
    if isinstance(m, int) and isinstance(n, int) and m >= 0 and n >= 0:
        return sumatoria_cola_aux(m, n, 0)
    else:
        return -1
    
def sumatoria_cola_aux(m, n, acc):
    if m > n:
        return acc
    
    return sumatoria_cola_aux(m+1, n, acc+m)


# Formula recursiva sqrt(2 + sqrt(2 + sqrt(2 + ...))) en pila 

def raiz_cuadrada_pila(n):
    if isinstance(n, int) and n >= 0:
        return raiz_cuadrada_pila_aux(n)
    else:
        return -1

def raiz_cuadrada_pila_aux(k):
    if k == 0:
        return 0
    
    return (2 + raiz_cuadrada_pila_aux(k-1))**0.5


# Formula recursiva sqrt(2 + sqrt(2 + sqrt(2 + ...))) en cola

def raiz_cuadrada_cola(n):
    if isinstance(n, int) and n >= 0:
        return raiz_cuadrada_cola_aux(n, 0)
    else:
        return -1
    
def raiz_cuadrada_cola_aux(k, acc):
    if k == 0:
        return acc
    
    return raiz_cuadrada_cola_aux(k-1, (2 + acc)**0.5)



def decimal_a_octal(num):
    if isinstance(num, int) and num > 0:
        return decimal_a_octal_aux(num, 0)
    
    else:
        return -1 


def decimal_a_octal_aux(num, exp):
    # if not num 
    if not num: 
        return 0 
    
    return (num % 8) * (10**exp) + decimal_a_octal_aux(num // 8, exp + 1)



# Averiguar si un numero es primo o no 
# Un numero primo es aquel que solo es divisible por 1 y por si mismo

def es_primo(num):
    if isinstance(num, int) and num > 0:
        return es_primo_aux(num, 2)
    else:
        return -1


# 10 
# 5   
# 10/6 tiene residuo 
# 10/7 tiene residuo 
# 10/8 tiene residuo
# 10/9 tiene residuo
def es_primo_aux(num, i):
    if i == num // 2 + 1:
        return True

    if num % i == 0:
        return False
    
    return es_primo_aux(num, i+1)


# Hacer una función que aproxime euler para cualquier exponente x, utilizando 
# las series de maclaurin 
# e^x = 1 + x + x^2/2! + x^3/3! + x^4/4! + ... + x^n/n!
def euler(x, n):
    if isinstance(x, int) and x >= 0 and isinstance(n, int) and n >= 0:
        return euler_aux(x, n)
    else:
        return -1

def euler_aux(x, n):
    if n == 0:
        return 1
    
    return (x**n) / factorial_pila(n) + euler_aux(x, n-1)


def largo(num, resultado):
    if not num:
        return resultado 
    
    return largo(num // 10, resultado + 1)

def reto_2(num):
    if isinstance(num, int) and num >= 0 and largo(num, 0) % 2 == 0:
        return reto_2_aux(num)
    else:
        return -1


def reto_2_aux(num):
    if num == 0:
        return True
    
    primero = num % 10  # 100 % 10 = 0
    segundo = (num // 10) % 10

    if segundo == 0:
        return reto_2_aux(num // 100)

    if primero % segundo == 0:
        return reto_2_aux(num // 100)

    return False 


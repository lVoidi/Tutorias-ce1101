

# Sumar los digitos de un numero utilizando recursividad

def sumar_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumar_digitos(n // 10)

        
def sumar_digitos_iterativo(n):
    suma = 0

    while n > 0:
        suma += n % 10
        n //= 10

    return suma


def sumar_digitos_lista(lista):
    suma = 0

    for n in lista:
        suma += n

    return suma


# Pasar decimal a binario utilizando iteracion
def decimal_a_binario_iterativo(num):
    if isinstance(num, int) and num > 0:
        binario = 0
        exp = 0

        while num > 0:
            binario += (num % 2) * (10**exp)
            num //= 2
            exp += 1

        return binario
    else:
        return -1


# Funcion que comprueba si el numero es primo utilizando iteracion
def es_primo(num):
    if isinstance(num, int) and num > 0:
        if num == 1:
            return False

        # range(a, b)
        for i in range(2, num//2 + 1):
            if num % i == 0:
                return False

        return True
    else:
        return -1



print(decimal_a_binario_iterativo(10)) 

print(es_primo(10000001020201099999999999)) 


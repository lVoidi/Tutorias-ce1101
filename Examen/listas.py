"""
En este archivo encontrarás ejercicios relacionados con listas enlazadas.

Los ejercicios están categorizados por estrellas:
* Ejercicios básicos
** Ejercicios intermedios
*** Ejercicios avanzados

Instrucciones:
- Hacer un fork del repositorio de Github
- Clonar el repositorio (fork) en su computadora
- Crear una rama con su nombre
- Hacer un commit por cada ejercicio resuelto 
- Hacer un push de la rama al repositorio fork
- Crear un pull request al repositorio original 
- En el mensaje del pull request, poner su nombre completo y carné
"""


# Implementación básica de una lista enlazada
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.tail = None
        
    
    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.tail is None:
            self.cabeza = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.siguiente = nuevo_nodo
            self.tail = nuevo_nodo
    

    def esta_vacia(self):
        return self.cabeza is None


    def agregar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo


    def imprimir(self):
        actual = self.cabeza
        while actual != None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")
        
        
    def __str__(self) -> str:
        result = ""
        actual = self.cabeza
        while actual:
            result += str(actual.dato) + " -> "
            actual = actual.siguiente
        result += "None"
        return result


# ------------------- Ejercicios básicos (*) -------------------
"""
Ejercicio 1: Contar elementos
Implemente una función que cuente cuántos elementos hay en una lista enlazada.
Ejemplo:
1 -> 2 -> 3 -> None
Resultado: 3
"""


def contar_elementos(lista: ListaEnlazada) -> int:
    contador = 0
    actual = lista.cabeza

    while actual:
        contador += 1
        actual = actual.siguiente

    return contador



"""
Ejercicio 2: Buscar elemento
Implemente una función que determine si un elemento existe en la lista enlazada.
Retorna True si existe, False en caso contrario.
"""

def buscar_elemento(lista: ListaEnlazada, dato) -> bool:
    actual = lista.cabeza
    while actual:
        if actual.dato == dato:
            return True
        actual = actual.siguiente
    return False

# ------------------- Ejercicios intermedios (**) -------------------
"""
Ejercicio 3: Invertir lista
Implemente una función que invierta el orden de los elementos en la lista enlazada.
Ejemplo:
1 -> 2 -> 3 -> None
Resultado: 3 -> 2 -> 1 -> None
"""

def invertir_lista(lista: ListaEnlazada) -> ListaEnlazada:
    prev = None
    actual = lista.cabeza
    while actual:
        siguiente = actual.siguiente
        
        
        actual.siguiente = prev
        
        prev = actual
        actual = siguiente
        
        
    lista.cabeza = prev
    return lista



"""
Ejercicio 4: Eliminar duplicados
Implemente una función que elimine los elementos duplicados de una lista enlazada.
Ejemplo:
1 -> 2 -> 2 -> 3 -> 3 -> None
Resultado: 1 -> 2 -> 3 -> None
"""

def eliminar_duplicados(lista: ListaEnlazada) -> ListaEnlazada:
    actual = lista.cabeza
    
    while actual:
        runner = actual
        
        while runner.siguiente:
            
            if runner.siguiente.dato == actual.dato:
                runner.siguiente = runner.siguiente.siguiente
            else:
                runner = runner.siguiente
                
        actual = actual.siguiente
        
    
    return lista


# ------------------- Ejercicios avanzados (***) -------------------
"""
Ejercicio 5: Detectar ciclo
Implemente una función que determine si una lista enlazada tiene un ciclo.
Un ciclo ocurre cuando un nodo apunta a un nodo anterior en la lista.
"""

def detectar_ciclo(lista: ListaEnlazada) -> bool:
    actual = lista.cabeza
    
    while actual:
        runner = actual
        
        while runner.siguiente:
            if runner.siguiente == actual:
                return True
            else:
                runner = runner.siguiente
                
        actual = actual.siguiente
    
    return False


"""
Ejercicio 6: Encontrar intersección
Implemente una función que encuentre el punto de intersección de dos listas enlazadas.
Si no hay intersección, retornar None.
"""

def interseccion(lista1: ListaEnlazada, lista2: ListaEnlazada) -> Nodo:
    actual_1 = lista1.cabeza
    actual_2 = lista2.cabeza
    
    while actual_1 != None and actual_2 != None:
        if actual_1.dato == actual_2.dato:
            return actual_1.dato
        
        actual_1 = actual_1.siguiente
        actual_2 = actual_2.siguiente
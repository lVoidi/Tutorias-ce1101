import random


"""
Nota: Asi podemos crear nuestros errores personalizados en python.
Hacemos una clase que se llame como quiera y simplemente hereda
Exception.

Para llamar a este error y que el programa termine, utilizamos
raise.

Por ejemplo: raise MatrixOperationError


Si queremos nuestro propio mensaje de error:
raise MatrixOperationError("Este es nuestro mensaje de error")

"""


class MatrixOperationError(Exception): ...


class Matriz:
    def __init__(self, dimension: tuple, llenar: bool = True):
        self.dimension = dimension
        self.matriz = []
        self.historial = []
        # Si quiere llenarlo de numeros aleatorios...
        if llenar:
            self.llenar_matriz()
        # Si no...
        else:
            for i in range(dimension[0]):
                self.matriz.append([0] * dimension[1])

    def __repr__(self) -> str:
        """
        Esta funcion se encarga de retornar una representacion
        de la matriz en forma de string. Puede utilizar
        f-strings para hacer esto.
        """
        representacion = ""
        for fila in self.matriz:
            for elemento in fila:
                representacion += f"{elemento}\t"

            representacion += "\n"

        return representacion

    def llenar_matriz(self) -> None:
        """
        Esta funcion se encarga de llenar self.matriz de
        numeros aleatorios entre 0 y 100. Puede utilizar
        random.randint(0, 100) para hacer esto.
        """
        for i in range(self.dimension[0]):
            self.matriz.append(
                [random.randint(0, 100) for _ in range(self.dimension[1])]
            )

        self.historial.append("llenar")

    def suma(self, matriz_2: "Matriz") -> None:
        """
        Esta funcion toma otro objeto Matriz de argumento y
        suma su matriz con la matriz actual. Esto se modifica
        directamente en la propiedad, asi que no devuelve nada
        esta funcion.

        Hice la funcion para tener un ejemplo.
        """
        A, B = self.matriz, matriz_2.matriz

        if self.matriz.dimension != matriz_2.dimension:
            # Salta nuestro error personalizado que creamos
            # antes
            raise MatrixOperationError(
                "Las matrices deben tener las mismas dimensiones"
            )

        for i in range(len(A)):
            for j in range(len(A[0])):
                self.matriz[i][j] = A[i][j] + B[i][j]

        # Agregamos al historial de operaciones un
        # string que contiene suma
        self.historial.append("suma")

    def resta(self, matriz_2: "Matriz") -> None:
        """
        Esta funcion toma otro objeto Matriz de argumento y
        resta su matriz con la matriz actual.
        """
        A, B = self.matriz, matriz_2.matriz

        if self.matriz.dimension != matriz_2.dimension:
            raise MatrixOperationError(
                "Las matrices deben tener las mismas dimensiones"
            )

        for i in range(len(A)):
            for j in range(len(A[0])):
                self.matriz[i][j] = A[i][j] - B[i][j]

        self.historial.append("resta")

    def total(self) -> int:
        """
        Esta funcion suma todos los elementos de la
        matriz y los devuelve como un numero entero
        """
        suma = 0
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):
                suma += self.matriz[i][j]
        self.historial.append("total")
        return suma

    def promedio(self) -> float:
        """
        Esta funcion toma la suma total y devuelve su promedio.
        Tip: Puede multiplicar las dimensiones para obtener la
        cantidad de elementos de la matriz
        """
        self.historial.append("promedio")
        return self.total() / (self.dimension[0] * self.dimension[1])

    def mayor(self) -> int:
        """
        Recorre toda la matriz y devuelve el elemento mayor
        """
        mayor = self.matriz[0][0]
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):
                if self.matriz[i][j] > mayor:
                    mayor = self.matriz[i][j]
        self.historial.append("mayor")
        return mayor

    def menor(self) -> int:
        """
        Recorre toda la matriz y devuelve el elemento menor
        """
        menor = self.matriz[0][0]
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):
                if self.matriz[i][j] < menor:
                    menor = self.matriz[i][j]
        self.historial.append("menor")
        return menor

    def transpuesta(self) -> None:
        """
        Convierte la matriz en su transpuesta, osea, intercambia
        las filas con las columnas. Recuerde cambiar las dimensiones.
        """
        # Creamos una matriz transpuesta
        transpuesta = []
        for i in range(self.dimension[0]):
            fila = []
            for j in range(self.dimension[1]):
                fila.append(self.matriz[j][i])

            transpuesta.append(fila)

        # Cambiamos las dimensiones
        self.dimension = (self.dimension[1], self.dimension[0])
        self.matriz = transpuesta
        self.historial.append("transpuesta")

    """
    A partir de aqui, vienen algunos ejercicios adicionales 
    de mayor dificultad. Es muy recomendable hacerlos.
    """

    def reversa(self, lista: list) -> list:
        """
        Revierte una lista de elementos.
        """
        nueva_lista = []
        for i in range(len(lista) - 1, -1, -1):
            nueva_lista.append(lista[i])

        return nueva_lista

    def reflexion_vertical(self) -> None:
        """
        Esta funcion hace una reflexion vertical, lo que significa
        intercambiar las filas finales por las iniciales.
        Ejemplo:

        [[1, 2],
         [3, 4]]
        -> [[3, 4],
            [1, 2]]

        (*) Los cambios se realizan sobre la propia matriz. Evite usar
        la funcion reversed para cualquier funcion. Puede escribir
        su propia funcion llamada reversa, que obtenga una lista y
        pase su version reversa.
        """

        nueva_matriz = self.reversa(self.matriz)
        self.matriz = nueva_matriz
        self.historial.append("reflexion_vertical")

    def reflexion_horizontal(self) -> None:
        """
        Esta funcion hace una reflexion horizontal, lo que significa
        intercambiar las columnas iniciales con las finales.
        [[1, 2],
         [3, 4]]
        -> [[2, 1],
            [4, 3]]
        (*)
        """
        nueva_matriz = []
        for i in range(len(self.matriz)):
            nueva_matriz.append(self.reversa(self.matriz[i]))

        self.matriz = nueva_matriz
        self.historial.append("reflexion_horizontal")

    def rotacion_izquierda(self) -> None:
        """
        Esta funcion hace una rotacion a la izquierda.
        [[1, 2],
         [3, 4]]
        -> [[2, 4],
            [1, 3]]
        """
        self.transpuesta()
        self.reflexion_vertical()
        self.historial.append("rotacion_izquierda")

    def rotacion_derecha(self) -> None:
        """
        Esta funcion hace una rotacion a la derecha.
        [[1, 2],
         [3, 4]]
        -> [[3, 1],
            [4, 2]]
        """
        self.transpuesta()
        self.reflexion_horizontal()
        self.historial.append("rotacion_derecha")

    def acotar(self, acote: tuple) -> None:
        """
        Esta funcion acota a la matriz principal en base a
        acote, una tupla que su primer elemento es el indice
        en el que se acotan las filas y el segundo es el indice
        donde se acotan las columnas

        Ejemplo: acote((1, 1))
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

        -> [[5, 6],
            [8, 9]]

        """

        nueva_matriz = []
        for i in range(acote[0], self.dimension[0]):
            fila = []
            for j in range(acote[1], self.dimension[1]):
                fila.append(self.matriz[i][j])

            nueva_matriz.append(fila)

        self.matriz = nueva_matriz
        self.dimension = (self.dimension[0] - acote[0], self.dimension[1] - acote[1])
        self.historial.append("acotar")

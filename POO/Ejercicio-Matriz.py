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
            ...

    def llenar_matriz(self) -> None:
        """
        Esta funcion se encarga de llenar self.matriz de
        numeros aleatorios entre 0 y 100. Puede utilizar
        random.randint(0, 100) para hacer esto.
        """
        ...

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
        ...

    def total(self) -> int:
        """
        Esta funcion suma todos los elementos de la 
        matriz y los devuelve como un numero entero
        """

    def promedio(self) -> float:
        """
        Esta funcion toma la suma total y devuelve su promedio. 
        Tip: Puede multiplicar las dimensiones para obtener la 
        cantidad de elementos de la matriz
        """
        ...

    def mayor(self) -> int:
        """
        Recorre toda la matriz y devuelve el elemento mayor 
        """
        ...

    def menor(self) -> int:
        """
        Recorre toda la matriz y devuelve el elemento menor 
        """

    def transpuesta(self) -> None:
        """
        Convierte la matriz en su transpuesta, osea, intercambia
        las filas con las columnas. Recuerde cambiar las dimensiones.
        """

    """
    A partir de aqui, vienen algunos ejercicios adicionales 
    de mayor dificultad. Es muy recomendable hacerlos.
    """

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
        ...

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
        ...

    def rotacion_izquierda(self) -> None:
        """
        Esta funcion hace una rotacion a la izquierda. 
        [[1, 2],
         [3, 4]]
        -> [[2, 4],
            [1, 3]]
        """
        ...

    def rotacion_derecha(self) -> None:
        """
        Esta funcion hace una rotacion a la derecha.
        [[1, 2],
         [3, 4]]
        -> [[3, 1],
            [4, 2]]
        """

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

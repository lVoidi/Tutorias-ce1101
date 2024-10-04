class Entidad:
    def __init__(self, vidas: int, velocidad: tuple, coordenadas: tuple):
        self.vidas = vidas
        self.velocidad = velocidad
        self.coordenadas = coordenadas

    def mover(self):
        self.coordenadas = (
            self.coordenadas[0] + self.velocidad[0],
            self.coordenadas[1] + self.velocidad[1],
        )

    def quitar_vida(self):
        self.vidas -= 1
        if self.vidas == 0:
            print(f"Se ha muerto {self.nombre}")

    def nueva_velocidad(self, velocidad: tuple):
        self.velocidad = velocidad

    def mostrar_informacion(self):
        print(
            f"""
Vida -> {self.vidas}
Velocidad -> {self.velocidad[0]}î + {self.velocidad[1]}ĵ
Posición -> ({self.coordenadas[0]}, {self.coordenadas[1]})
    """
        )


class Jugador(Entidad):
    def __init__(self, vidas: int, velocidad: tuple, coordenadas: tuple, nombre: str):
        # Llama a la función init de la clase Entidad, con los argumentos que reciba
        super().__init__(vidas, velocidad, coordenadas)
        self.nombre = nombre

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(
            f"""
---- Información específica ----
Nombre -> {self.nombre}
"""
        )


class Enemigo(Entidad):
    def __init__(self, vidas: int, velocidad: tuple, coordenadas: tuple, tipo: str):
        super().__init__(vidas, velocidad, coordenadas)
        self.tipo = tipo

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(
            f"""
---- Información específica ----
Tipo -> {self.tipo}
            """
        )


class Mapa:
    def __init__(self, dimensiones: tuple):
        self.dimensiones = dimensiones
        self.entidades = []

    def mover_entidades(self):
        for entidad in self.entidades:
            entidad.mover()

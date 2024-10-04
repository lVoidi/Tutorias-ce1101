# Introducción a la Programación Orientada a Objetos 
La Programación Orientada a Objetos, abreviada POO (OOP en inglés), es un paradigma de programación. Paradigma de programación 
se puede entender como un punto de vista del código. Anteriormente, la programación se solía ver totalmente funcional. Recursividad, 
por ejemplo, nació a partir de la programación funcional. ¿Qué es la programación funcional? Ver todo como funciones matemáticas puras,
prácticamente.  
Esto cambió con la llegada de POO. Investigadores del MIT, como Ivan Sutherland en 1960, empezaron a adoptar el concepto de objeto y el 
objeto de instancia. Como el nombre del paradigma lo indica, la programación empezó a orientarse a estos llamados objetos, con el fin 
de implementtar entidades de la vida real (como, por ejemplo, un carro) y abstraerlo a nivel de código.
Algunos conceptos de la programación orientada a objetos son los siguientes:
1. [Clase](#clase)
2. [Instancias](#instancias)
3. [Herencia](#herencia)
4. [Polimorfismo](#polimorfismo)

# Clase 
Esta es la plantilla o modelo que va a seguir nuestro objeto. Una clase tiene sus atributos y sus comportamientos, o métodos, que puede seguir.  
Veamos un ejemplo en Python. Imaginemos que queremos hacer un juego, y queremos crear un jugador. Primero pensamos en qué características 
debe tener. En vez de crear 30 mil funciones y variables globales, podemos crear una clase. Veamos los atributos de un jugador, de manera simple.
1. vidas: int 
2. nombre: string 
3. velocidad = tuple(int)  
4. coordenadas: tuple(int) 
A su vez, debemos definir un comportamiento. 
1. mover()
2. quitar_vida()
3. nueva_velocidad(velocidad)

Vamos a ver como implementar esto en python 

```py 

class Jugador: 
    def __init__(self, vidas: int, nombre: str, velocidad: tuple, coordenadas: tuple):
        self.vidas = vidas 
        self.nombre = nombre 
        self.velocidad = velocidad
        self.coordenadas = coordenadas
    

    def mover(self):
        self.coordenadas = (
            self.coordenadas[0] + self.velocidad[0],
            self.coordenadas[1] + self.velocidad[1]
        )
    

    def quitar_vida(self):
        self.vidas -= 1 
        if self.vidas == 0:
            print(f"Se ha muerto {self.nombre}")
    

    def nueva_velocidad(self, velocidad: tuple):
        self.velocidad = velocidad
```
Hablemos de ese código. La sintaxis en Python, y en cualquier lenguaje, es utilizar *class* para definir las clases. Aquí es donde empiezan a 
aparecer conceptos nuevos. Cada clase tien su función constructora. Esta función crea una instancia de esa clase Jugador, osea, podemos crear 
un jugador nuevo y diferente haciendo uso de este modelo gracias a la función constructora. Si se fijan, la función recibe un parametro llamado 
*self*. Este hace referencia a la clase, entonces, siempre que queremos acceder a un método o atributo de la clase dentro de la misma, hay que 
utilizar *self.atributo* o *self.metodo()*. Los metodos en esta clase son: \_\_init\_\_, mover, quitar_vida y nueva_velocidad. Si se fijan, cada 
uno de los métodos de una clase deben recibir como parámetro self. Esa es nuestra primera clase!

# Instancias
Ahora, ¿cómo creamos un jugador nuevo? La sintaxis es simple. Tomando el código anterior, podemos crear un objeto de la siguiente manera.
```py
jugador_1 = Jugador(3, "carlos", (-1, 1), (150, 150))
```
Es como llamar una función, en este caso, la "función" que llamamos tiene como nombre Jugador, pero en realidad la que estamos llamando es 
la función constructora, la cual recibe cuatro argumentos aparte del self: vidas, nombre, velocidad y coordenadas. Gracias a esta instancia,
podemos acceder a todas las funciones que queramos de este jugador llamado carlos. Si queremos mover a carlos, hacemos: 
```py
jugador_1.mover()
```
Así de simple!

## Tips y convenciones para las clases 
### Formato
Según el PEP8, las clases deben ser creadas con mayúsculas (en este caso, Jugador). Si tuviera más palabras, entonces empezamos todas las palabras
con mayúscula para separarlas (ClaseConVariasPalabras). 

```py 
class Carro:
    ...
```
Cuando queremos crear instancias, atributos o métodos, usamos el snake case. Veamos este ejemplo para los métodos:

```py 
class Carro:
    def __init__(self, marca):
        self.marca = marca


    def mostrar_marca():
        print(self.marca)

```

Como podemos ver, las palabras siempre están en minúscula y separadas por barra baja. A su vez, debe haber una separación de dos lineas entre cada 
función, para que el código sea más legible. En el caso de las instancias, también se debe usar snake case 
```py
toyota = Carro("toyota")
toyota.mostrar_marca()
```

#### Type annotations 
Si se fijan en el ejemplo de Jugador, hice algo extraño en la función constructora.

```py
#                                           ¿por qué?
#                         vvv          vvv             vvvvv               vvvvv
def __init__(self, vidas: int, nombre: str, velocidad: tuple, coordenadas: tuple):
    self.vidas = vidas 
    self.nombre = nombre 
    self.velocidad = velocidad
    self.coordenadas = coordenadas
```
Si recuerdan bien, en Python no es necesario definir los tipos de datos de un argumento de una función. Pero yo lo estoy haciendo aquí. Normalmente,
los linters y LS (language servers) son los encargados de decirnos los errores que tenemos en nuestro código, o cuando queremos acceder a una función
de una librería, utilizamos el punto (.) para acceder a ellos, y a su vez, el editor de texto nos va guiando. Si nosotros escribimos una función, sea

```py
# Incorrecto
def f(palabra):
    return palabra.upper()
```
¿Cómo sabe el LS que palabra es un string? Es simple, no lo sabe. Entonces, no tira error porque esa funcion f recibe un argumento que no sabe qué es,
así que esa función upper puede o estar bien o estar mal y no lo podemos saber a menos que llamemos esa función con un parámetro equivocado.
```sh
>>> f(12)
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    f(12)
    ~^^^^
  File "<python-input-0>", line 1, in f
    def f(p): return p.upper()
                     ^^^^^^^
AttributeError: 'int' object has no attribute 'upper'
```
Entonces, para evitar equivocarnos a la hora de escribir una función, o a la hora de llamar una, es mejor documentar bien bien qué tipo de datos 
va a recibir y qué tipo de datos va a retornar.
```py 
# Correcto
def f(palabra: str) -> str: 
    """
    Esta función recibe una palabra y devuelve su versión en mayúsculas. 
    """
    return palabra.upper()
```
```
>>> f("hola")
'HOLA'
```
Ahora, si escribimos *f(* en un IDE o un editor de texto con LSP, entonces podremos ver una preview de lo que hace la función f y nos puede 
ayudar a recordar en qué orden iban los parámetros y sus tipos de datos.

### Nivel de acceso
En otros lenguajes, como Java o C#, hay que definir el nivel de acceso de una variable (public, private, internal, etc), pero esto no existe en 
Python. El nivel de acceso es como decir: quiero que tal método sea accesible solo desde la propia clase y no desde una instancia. A esto se le 
llama encapsulación. 

En Python, como tal, no existe, pero si hay una convención. Si queremos que un atributo o un método sea accesible solo desde
la clase, se puede crear con una doble barra baja y luego el nombre.
```py
class Cuadrado:
    def __init__(self, lado):
        self.__lado = lado

    def set_lado(self, nuevo_lado):
        self.__lado = nuevo_lado
    
    def get_lado(self):
        return self.__lado
```
> Nota: Los métodos getters y setters son una una convención, que nos permiten, desde fuera, obtener o modificar un atributo de nuestra clase.  
> En este caso, definimos set_lado, para cambiar el lado, y get_lado, para  obtener el lado de nuestro cuadrado
> Puede parecer inútil, pero esto es obligatorio en lenguajes como Java. Además, a veces queremos que algun dato no sea modificado desde fuera simplemente

# Herencia 
Usando el ejemplo de jugador, imagina que ahora quieres agregar el resto de clases. Para esto, creamos una clase que sea para los enemigos y otra para el 
mapa.
```py

class Jugador: 
    def __init__(self, vidas: int, nombre: str, velocidad: tuple, coordenadas: tuple):
        self.vidas = vidas 
        self.nombre = nombre 
        self.velocidad = velocidad
        self.coordenadas = coordenadas
    

    def mover(self):
        self.coordenadas = (
            self.coordenadas[0] + self.velocidad[0],
            self.coordenadas[1] + self.velocidad[1]
        )
    

    def quitar_vida(self):
        self.vidas -= 1 
        if self.vidas == 0:
            print(f"Se ha muerto {self.nombre}")
    

    def nueva_velocidad(self, velocidad: tuple):
        self.velocidad = velocidad



class Enemigo: 
    def __init__(self, tipo: string, vidas: int, velocidad: tuple, coordenadas: tuple):
        self.vidas = vidas 
        self.velocidad = velocidad
        self.tipo = tipo
        self.coordenadas = coordenadas
    

    def mover(self):
        self.coordenadas = (
            self.coordenadas[0] + self.velocidad[0],
            self.coordenadas[1] + self.velocidad[1]
        )
    

    def quitar_vida(self):
        self.vidas -= 1 
        if self.vidas == 0:
            print(f"Se ha muerto {self.nombre}")
    

    def nueva_velocidad(self, velocidad: tuple):
        self.velocidad = velocidad


    def mostrar_tipo(self):
        print(f"¡Es un enemigo de tipo {self.tipo}!")



class Mapa:
    def __init__(self, dimensiones: tuple):
        self.dimensiones = dimensiones 
        self.enemigos = []
        self.jugadores = []
    

    def mover_entidades(self):
        for enemigo in self.enemigos:
            enemigo.mover()
        
        for jugador in self.jugadores:
            jugador.mover()

```
Si se fijan, el código quedó muy largo y hay como un sentimiento de que hay una mejor forma de hacer esto. Y en efecto, la hay. Se llama herencia. 
Si se fijan, las clases de enemigo y jugador, comparten 3 atributos y 4 métodos. Para esto, podemos crear una clase padre llamada Entidad, la cual 
puede heredar los métodos y atributos de la misma. 

```py
class Entidad: 
    def __init__(self, vidas: int, velocidad: tuple, coordenadas: tuple):
        self.vidas = vidas 
        self.velocidad = velocidad
        self.coordenadas = coordenadas
    

    def mover(self):
        self.coordenadas = (
            self.coordenadas[0] + self.velocidad[0],
            self.coordenadas[1] + self.velocidad[1]
        )
    

    def quitar_vida(self):
        self.vidas -= 1 
        if self.vidas == 0:
            print(f"Se ha muerto {self.nombre}")
    

    def nueva_velocidad(self, velocidad: tuple):
        self.velocidad = velocidad
    
    def mostrar_informacion(self):
        print(f"""
Vida -> {self.vidas}
Velocidad -> {self.velocidad[0]}î + {self.velocidad[1]}ĵ
Posición -> ({self.coordenadas[0]}, {self.coordenadas[1]})
    """)
```

Agregué un método adicional llamado mostrar_información para el capítulo de polimorfismo. Ahora, para hacer que las clases hereden a Entidad, lo hacemos de la siguiente manera 
```py
# Hereda Entidad
class Jugador(Entidad):
    def __init__(self, vidas: int, velocidad: tuple, coordenadas: tuple, nombre: str):
        # Llama a la función init de la clase Entidad, con los argumentos que reciba
        super().__init__(vidas, velocidad, coordenadas)
        self.nombre = nombre 


class Enemigo(Entidad):
    def __init__(self, vidas: int, velocidad: tuple, coordenadas: tuple, tipo: str):
        super().__init__(vidas, velocidad, coordenadas)
        self.tipo = tipo 
```
Si se fijan, nos ahorramos muchas líneas de código de por sí, pero ahora podemos ahorrarnos más líneas de código en la clase mapa.
```py
class Mapa:
    def __init__(self, dimensiones: tuple):
        self.dimensiones = dimensiones 
        self.entidades = []
    

    def mover_entidades(self):
        for entidad in self.entidades:
            entidad.mover()
```
Esta es la gran utilidad de herencia!

# Polimorfismo 
Polimorfismo es una palabra que puede parecer complicada, pero simplemente significa que nuestra clase puede tomar varias formas.
Véase entidades, en el método que agregué: 
```py
def mostrar_informacion(self):
    print(f"""
Vida -> {self.vidas}
Velocidad -> {self.velocidad[0]}î + {self.velocidad[1]}ĵ
Posición -> ({self.coordenadas[0]}, {self.coordenadas[1]})
""")
```
¿Cómo hacemos que esta función, aparte de mostrar la información general, también muestre la información específica de cada clase que herede? No vamos a 
reescribir la función desde cero otra vez, para eso, hacemos uso del polimorfismo, con la función super(). 

```py 
class Jugador(Entidad):
    def __init__(self, vidas: int, velocidad: tuple, coordenadas: tuple, nombre: str):
        # Llama a la función init de la clase Entidad, con los argumentos que reciba
        super().__init__(vidas, velocidad, coordenadas)
        self.nombre = nombre 
    

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"""
---- Información específica ----  
Nombre -> {self.nombre}
""")


class Enemigo(Entidad):
    def __init__(self, vidas: int, velocidad: tuple, coordenadas: tuple, tipo: str):
        super().__init__(vidas, velocidad, coordenadas)
        self.tipo = tipo 


    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"""
---- Información específica ----  
Tipo -> {self.tipo}
""")
```
# Conclusiones 
La programación orientada a objetos es muy útil para ver escenarios de la vida real o incluso objetos abstractos, como pueden ser listas enlazadas o 
árboles. Esta mejora la legibilidad y facilita la mantenibilidad de un código mediante su modularidad y reutilización de código. Si se fijan, el código en python es prácticamente como leer inglés. 
> Si puedes imaginarlo, puedes programarlo - Alejandro Taboada "ProgramacionATS"


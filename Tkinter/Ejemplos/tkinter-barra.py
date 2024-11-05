"""
Este archivo ejemplifica un rectángulo que cambia de tamaño en tkinter.
Esto permite simular el efecto del gancho de Super Pang.

¿Cómo lo hacemos?
1. Creamos una ventana de tkinter.
2. Creamos un canvas dentro de la ventana.
3. Creamos un rectángulo en el canvas.
4. Cambiamos el tamaño del rectángulo.


Creacion de rectángulos
-----------------------
Para crear un rectángulo en tkinter, utilizamos el método create_rectangle del canvas.
Este método recibe 4 argumentos:
1. x0: Coordenada x del punto superior izquierdo.
2. y0: Coordenada y del punto superior izquierdo.
3. x1: Coordenada x del punto inferior derecho.
4. y1: Coordenada y del punto inferior derecho.


           x0, y0        x1, y0
              ____________
              |          |
              |          |
              |          |
              |          |
              ------------
            x0, y1      x1, y1

El efecto que quiero lograr es un rectángulo que empieze siendo 50,50 
y que cuando llegue a ser 50, 400 vuelva a ser 50,50 y así sucesivamente.

Para subir en y, debemos restar.
Para bajar en y, debemos sumar y.
"""

import tkinter as tk
import time

# Definimos constantes
WIDTH, HEIGHT = 800, 600

# Definimos variables globales
x, y = 400, 500
largo = 50
ancho = 50
shooting = True

# Creamos la ventana principal
window = tk.Tk()
window.title("Barra")
window.geometry(f"{WIDTH}x{HEIGHT}")
window.resizable(False, False)

# Creamos un canvas en la misma ventana, con el mismo largo y el mismo ancho
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

# Creamos el rectángulo en el canvas
rect = canvas.create_rectangle(
    # Coordenadas del rectángulo
    # x0, y0, x1, y1
    x, y, x + largo, y + ancho, # Coordenadas
    fill="black" # Color
)

def update_bullet():
    global ancho
    if ancho >= 400:
        ancho = 0

    canvas.coords(rect, x, y, x + largo, y - ancho)
    
    ancho += 1

# Una funcion que actualiza el canvas  
def update():
    global ancho

    # Mientras la ventana esté abierta
    while True:
        
        # En el super pang, esto depende de si se presiona el botón de disparo
        # También, en el super pang, el x no sería una posición fija, sino la posición
        # del jugador!! cuidado
        if shooting:
            update_bullet()
        
        # Actualizamos el canvas
        window.update()
        time.sleep(0.005)

# Llamamos a la función update
window.after(0, update)
window.mainloop()
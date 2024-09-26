"""
Instalar Pillow para mejor manejo de las imagenes
En la terminal / powershell:
pip install Pillow

¿Cómo funcionan las coordenadas en Tkinter?
En Tkinter, las coordenadas de la ventana se miden desde la esquina superior izquierda.
Por ejemplo, si queremos posicionar un objeto en la esquina superior izquierda, las coordenadas serían (0, 0).
Si queremos posicionar un objeto en la esquina inferior derecha, las coordenadas serían (ancho, alto).
En este caso, el ancho y el alto son las dimensiones de la ventana.

     0 1 2 3 4 5 6 7 8 9 ...       n
0    # # # # # # # # # # # # # # # #
1    #.............................#
2    #.............................#
.    #.............................#
.    #.............................#
.    #.............................#
m    # # # # # # # # # # # # # # # #

"""
from PIL import Image, ImageTk
import tkinter as tk
import time 

# Definimos constantes (no es necesario, pero es buena práctica)
WIDTH, HEIGHT = 800, 600
BALL_SIZE = 50

# Definimos variables globales (posicion de la bola)
x, y = 0, 0

# Creamos la ventana principal
window = tk.Tk()
window.title("Movimiento")
window.geometry(f"{WIDTH}x{HEIGHT}")
window.resizable(False, False)

# Creamos un canvas en la misma ventana, con el mismo largo y el mismo ancho
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

# Cargamos la imagen de la bola
img = Image.open("Ejemplos/ball.jpg").resize( (BALL_SIZE, BALL_SIZE) )
img = ImageTk.PhotoImage(img)

# Guardamos la imagen en una variable dentro de la ventana Root, para evitar que sea eliminada por el garbage collector
window.loquesea = img

# Creamos la bola en el canvas
bola = canvas.create_image(
    x, y, # Coordenadas
    anchor="nw", # Esto es para que la imagen se posicione con respecto a la esquina superior izquierda
    image=img # La imagen que queremos mostrar
)

def update_image():
    global x, y 
    # Si la bola se sale de la ventana, la regresamos al inicio
    if x > 800:
        x = 0
    if y > 600:
        y = 0
        
    # Avanzamos la bola
    x += 1
    y += 1

    # Cambia las coordenadas dentro del canvas
    canvas.coords(bola, x, y)

# Una funcion que actualiza el canvas
# Recuerden que solo se puede utilizar un bucle while en un hilo, por eso utilizamos la funcion after
def update():
    global x, y

    # Mientras la ventana esté abierta
    while True:
        update_image()
        window.update()
        time.sleep(0.01)
        
# la funcion after llama a la funcion update cada vez que se actualiza la ventana
window.after(0, update)

# Iniciamos el bucle principal
window.mainloop()
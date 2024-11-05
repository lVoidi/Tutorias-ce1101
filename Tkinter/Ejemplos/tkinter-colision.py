"""
Este programa busca ejemplificar cómo se detectan las colisiones en tkinter.
Para esto, el objetivo es tener una bola moviendose en la pantalla y que rebote
en los bordes de la ventana. Esto se logra con la función move del canvas, que
mueve un objeto en el canvas. Para detectar las colisiones, podemos utilizar
bbox, que nos da las coordenadas del objeto en el canvas. Con esto, podemos
detectar si el objeto se sale de la ventana y hacer que rebote.

Para hacer que la bola rebote, podemos utilizar un vector direccion que nos
diga en qué dirección se mueve la bola. Si la bola choca con un borde, podemos
cambiar la dirección en la que se mueve la bola. 

Direcion: (1, 1) -> Abajo y a la derecha
Dirección: (1, -1) -> Arriba y a la derecha
Dirección: (-1, 1) -> Abajo y a la izquierda
Dirección: (-1, -1) -> Arriba y a la izquierda

A su vez, tendremos un rectángulo que se extenderá desde la parte inferior
de la ventana hasta la parte superior. Este rectangulo siempre se extiende 
desde el centro, pero en el juego es desde el x del jugador. 
Si la bola choca con el rectángulo,la bola será borrada del canvas.
En el caso del super pang, la bola se divide
pero en este caso, la bola simplemente desaparece.
"""
from PIL import Image, ImageTk
import tkinter as tk
import time

# Definimos constantes
WIDTH, HEIGHT = 800, 600
end = False
puntaje = 0



# Definimos variables globales
ball_coords = [400, 500]
dir = [1, 1]
size = 50

# rectangulo
rect_coords = [400, 500]
rect_height = 0
rect_width = 50
shooting = False


window = tk.Tk()
window.title("Colisión")
window.geometry(f"{WIDTH}x{HEIGHT}")
window.resizable(False, False)

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

instructions = canvas.create_text(
    WIDTH // 2, HEIGHT // 2,
    text="Presiona la barra espaciadora para disparar",
    font=("Arial", 20)
)

puntaje_text = canvas.create_text(
    WIDTH // 4, HEIGHT // 2 + 50,
    text=f"Puntaje: {puntaje}",
    font=("Arial", 20)
)

img = Image.open("Ejemplos/ball.jpg").resize( (size, size) )
img = ImageTk.PhotoImage(img)

ball = canvas.create_image(
    ball_coords[0], ball_coords[1],
    anchor="nw",
    image=img
)

rect = canvas.create_rectangle(
    rect_coords[0], rect_coords[1], rect_coords[0] + rect_width, rect_coords[1], # En un inicio notiene altura
    fill="black"
)

def update_ball():
    """
    Esta funcion actualiza la posición de la bola en el canvas.
    Si la bola choca con un borde, cambia la dirección en la que se mueve.
    """
    global ball_coords, dir
    if ball_coords[0] >= WIDTH or ball_coords[0] <= 0:
        dir[0] *= -1
    if ball_coords[1] >= HEIGHT or ball_coords[1] <= 0:
        dir[1] *= -1

    ball_coords[0] += dir[0]
    ball_coords[1] += dir[1]

    canvas.coords(ball, ball_coords[0], ball_coords[1])
    
def update_rect():
    """
    Esta funcion se activa cuando el jugador dispara.
    Mueve el rectángulo hacia arriba hasta que llega a la parte superior o choca con la bola.
    """
    global rect_height, shooting, end
    if rect_height >= HEIGHT:
        rect_height = 0
        shooting = False
        
    # Detecta las colisiones con la bola utilizando bbox
    # Esto nos da las coordenadas del objeto en el canvas
    # como un rectángulo (x0, y0, x1, y1)

    ball_bbox = canvas.bbox(ball)
    rect_bbox = canvas.bbox(rect)

    if (ball_bbox[2] >= rect_bbox[0]
        and ball_bbox[0] <= rect_bbox[2] 
        and ball_bbox[3] >= rect_bbox[1] 
        and ball_bbox[1] <= rect_bbox[3]):
        canvas.delete(ball)
        
        puntaje = 100
        canvas.itemconfig(puntaje_text, text=f"Puntaje: {puntaje}")

        # Reinicia variables
        rect_height = 0
        shooting = False
        end = True
    else:
        print(rect_height)
        rect_height += 1

    canvas.coords(rect, rect_coords[0], rect_coords[1], rect_coords[0] + rect_width, rect_coords[1] - rect_height)


def update():
    while True:
        if end:
            canvas.delete(instructions)
            canvas.create_text(
                WIDTH // 2, HEIGHT // 2,
                text="Simulación terminada",
                font=("Arial", 20)
            )
            window.after(2000, window.destroy)
        update_ball()

        if shooting:
            update_rect()
            
        window.update()
        time.sleep(0.005)

def shoot(event):
    """
    Esta función se llama cuando se presiona cualquier boton. 
    Si el botón presionado es la barra espaciadora, se cambia la variable
    shooting a True, lo que comienza el "disparo" de la barra.
    """
    global shooting
    if event.keysym == "space":
        shooting = True
        
window.bind("<KeyPress>", shoot)
window.after(1, update)
window.mainloop()


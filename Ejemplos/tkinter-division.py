"""
En este ejemplo, vamos a hacer una barra, como la de tkinter-colision, que
puede dispararse cuando quiera. En el mapa, hay una esfera de radio 50 que se
mueve en diagonal. La barra puede disparar hacia arriba y si la esfera choca
con el proyectil, la bola se divide en dos bolas de radio 25. Luego de esto,
las bolas se mueven en direcciones opuestas. Por ultimo, si la barra choca
con una bola de radio 25, estas se dividen en dos bolas de radio 12.5 y luego
de esto, si esas bolas chocan con la barra, son eliminadas y ya no se dividen
mas esferas.
"""

import tkinter as tk
import time

# Definimos constantes
WIDTH, HEIGHT = 800, 600
end = False
puntaje = 0

# [id, coords, dir, size]
bolas = []

# Definimos variables globales
rect_coords = [400, 500]
rect_height = 0
rect_width = 50
shooting = False

window = tk.Tk()
window.title("División")
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

rect = canvas.create_rectangle(
    rect_coords[0], rect_coords[1], rect_coords[0] + rect_width, rect_coords[1], # En un inicio notiene altura
    fill="black"
)

bolas.append([canvas.create_oval(400, 100, 450, 150), [400, 100], [1, 1], 50])

def update_rect():
    global rect_height, shooting
    if rect_height >= 400:
        rect_height = 0
        canvas.coords(rect, rect_coords[0], rect_coords[1], rect_coords[0] + rect_width, rect_coords[1] - rect_height)
        shooting = False
        return

    canvas.coords(rect, rect_coords[0], rect_coords[1], rect_coords[0] + rect_width, rect_coords[1] - rect_height)
    
    rect_height += 10

def update_balls(b, result):
    global puntaje, shooting, bolas, end

    if not bolas:
        end = True
        return
    
    if not b:
        print(result)
        return result
    
    if is_collision(b) and shooting:
        id, coords, dir, size = b[0]
        if b[0] in result:
            result.remove(b[0])
        canvas.delete(id)
        
        # Actualiza el rectangulo
        rect_height = 0
        canvas.coords(rect, rect_coords[0], rect_coords[1], rect_coords[0] + rect_width, rect_coords[1] - rect_height)
        shooting = False

        # Actualiza el puntaje
        puntaje += size
        canvas.itemconfig(puntaje_text, text=f"Puntaje: {puntaje}")

        if size == 50:
            ball_left = canvas.create_oval(coords[0], coords[1], coords[0] + 25, coords[1]+25, fill="red")
            ball_right = canvas.create_oval(coords[0], coords[1], coords[0]+25, coords[1]+25, fill="blue")
            result.append([ball_right, coords, [1, 1], 25])
            result.append([ball_left, coords, [-1, 1], 25])
        elif size == 25:
            ball_left = canvas.create_oval(coords[0], coords[1], coords[0] + 12.5, coords[1] + 12.5, fill="red")
            ball_right = canvas.create_oval(coords[0], coords[1], coords[0] + 12.5, coords[1] + 12.5, fill="blue")
            result.append([ball_right, coords, [1, 1], 12.5])
            result.append([ball_left, coords, [-1, 1], 12.5])
            
        print(result)
        return result + b[1:]
    
    id, coords, dir, size = b[0]
    new_coords = [coords[0], coords[1]]
    new_dir = [dir[0], dir[1]]
    new_coords[0] += dir[0]
    new_coords[1] += dir[1]

    if new_coords[0] > 800 or new_coords[0] < 0:
        new_dir[0] *= -1
    
    if new_coords[1] > 600 or new_coords[1] < 0:
        new_dir[1] *= -1    
    
    canvas.coords(id, new_coords[0], new_coords[1], new_coords[0] + size, new_coords[1] + size)
    result.append([id, new_coords, new_dir, size])
    
    return update_balls(b[1:], result)
    
def is_collision(b):
    if not b:
        return False
    
    id, coords, dir, size = b[0]
    rect_box = canvas.bbox(rect)
    
    if rect_box[0] < coords[0] + size < rect_box[2] and rect_box[1] < coords[1] + size < rect_box[3]:
        return True
    
    return is_collision(b[1:])

def update():
    global bolas, end
    while True:
        if end:
            canvas.delete(instructions)
            canvas.create_text(
                WIDTH // 2, HEIGHT // 2,
                text="Simulación terminada",
                font=("Arial", 20)
            )
            window.after(2000, window.destroy)
        if shooting:
            update_rect()
        bolas = update_balls(bolas, [])
        window.update()
        time.sleep(0.005)
    

def on_key_press(event):
    global rect_height, shooting
    if event.keysym == "space" and not shooting:
        rect_height = 0
        canvas.coords(rect, rect_coords[0], rect_coords[1], rect_coords[0] + rect_width, rect_coords[1] - rect_height)
        shooting = True


window.bind("<KeyPress>", on_key_press)
window.after(10, update)
window.mainloop()
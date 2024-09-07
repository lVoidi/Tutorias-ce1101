from tkinter import messagebox
from threading import Thread
from tkinter import ttk
import tkinter as tk
import random
import time

WIDTH = 500
HEIGHT = 500
_state = False

colors = [
    "#cc241d",
    "#98971a",
    "#d79921",
    "#458588",
    "#b16286"
]

velocity_multiplier = 0.0


class Ball:
    def __init__(self, canvas: tk.Canvas, x, height):
        self.canvas = canvas
        self.x = x
        self.height = height
        self.updating_height = 0
        self.acceleration = 9.8
        self.change_once = False
        self.image = self.create_circle(x, height, 50)

    def create_circle(self, x, y, radio):
        return self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill=random.choice(colors))

    def move(self, seconds):
        coords = self.canvas.coords(self.image)
        self.updating_height = self.updating_height + (velocity_multiplier / 100) * (
                0.5 * self.acceleration * seconds ** 2)
        if coords[1] > 550 or coords[3] > 550:
            self.canvas.move(self.image, 0, -550)
            self.updating_height = 0

        self.canvas.move(self.image, 0, self.updating_height)


def ball_loop(root: tk.Toplevel, ball: Ball):
    seconds = 0
    while True:
        ball.move(seconds)
        root.update()
        seconds += 1
        time.sleep(0.05)


def add_ball(root: tk.Toplevel, canvas: tk.Canvas, entry: tk.Entry):
    update_velocity(entry)
    ball = Ball(canvas, random.randint(0, 500), random.randint(0, 500))
    thread = Thread(target=ball_loop, args=(root, ball,))
    thread.start()


def on_closing(root: tk.Toplevel):
    global _state
    if messagebox.askokcancel("Salir", "¿Salir de ?"):
        _state = False
        root.destroy()


def on_slider_move(pos, var: tk.StringVar):
    global velocity_multiplier
    velocity_multiplier = float(pos)
    var.set(str(velocity_multiplier))


def update_velocity(entry: tk.Entry):
    global velocity_multiplier
    try:
        entry = float(entry.get())
    except (ValueError, TypeError):
        messagebox.showerror("Error", "Debe ser un número entero flotante")
    velocity_multiplier = float(entry)


def open_animation_prompt(root: tk.Tk):
    global velocity_multiplier
    global _state
    if _state:
        messagebox.showerror("Error", "Esta ventana ya está corriendo")
        return -1

    _state = True

    animation_window = tk.Toplevel(root)
    animation_window.resizable(width=False, height=False)
    animation_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(animation_window))
    animation_window.config(
        bg="#282828"
    )
    title = tk.Label(
        master=animation_window,
        bg="#1d2021",
        fg="#ebdbb2",
        font=("Times New Roman", 15, "italic"),
        text="Simulación de la gravedad de la tierra",

    )

    canvas = tk.Canvas(animation_window, width=WIDTH, height=HEIGHT, bg="#282828")
    vel_var = tk.StringVar(master=animation_window, name="1.0")
    vel_entry = tk.Entry(
        master=animation_window,
        bg="#3c3836",
        fg="#d5c4a1",
        justify="center",
        textvariable=vel_var,
        font=("Times New Roman", 14)
    )
    slider = ttk.Scale(
        master=animation_window,
        command=lambda pos: on_slider_move(pos, vel_var),
    )
    add_ball_button = tk.Button(
        master=animation_window,
        text="Añadir bola",
        bg="#8ec08c",
        fg="#3c3836",
        font=("Times New Roman", 14, "bold"),
        relief="flat",
        command=lambda: add_ball(animation_window, canvas, vel_entry)
    )
    update_velocity_button = tk.Button(
        master=animation_window,
        text="Actualizar velocidad",
        bg="#689d6a",
        fg="#3c3836",
        font=("Times New Roman", 14, "bold"),
        relief="flat",
        command=lambda: update_velocity(vel_entry)
    )
    get_back_button = tk.Button(
        text="Volver al menú",
        relief="flat",
        master=animation_window,
        bg="#5b895c",
        fg="#ebdbb2",
        activebackground=colors[2],
        activeforeground="#ebdbb2",
        font=("Times New Roman", 14),
        command=lambda: on_closing(animation_window)
    )
    title.grid(row=0, column=0, sticky="nsew")
    canvas.grid(row=1, column=0, sticky="nsew")
    slider.grid(row=2, column=0, sticky="nsew")
    vel_entry.grid(row=3, column=0, sticky="nsew")
    add_ball_button.grid(row=4, column=0, sticky="nsew")
    update_velocity_button.grid(row=5, column=0, sticky="nsew")
    get_back_button.grid(row=6, column=0, sticky="nsew")

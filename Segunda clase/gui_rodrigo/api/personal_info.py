from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import pygame

_state = False
_state_music = False
colorscheme = [
    "#282a36",  # bg
    "#f8f8f2",  # fg
    "#44475a",  # gray
    "#6272a4",  # gray_2,
    "#ffb86c",  # orange
    "#ff79c6",  # pink
    "#bd93f9",  # purple
    "#ff5555",  # red
    "#f1fa8c"  # yellow
]


def on_closing(root: tk.Toplevel):
    global _state
    if messagebox.askokcancel("Salir", "¿Salir de ficha personal?"):
        _state = False
        root.destroy()


pygame.mixer.init()


def play_music():
    pygame.mixer.music.load("api/assets/dogs.mp3")
    pygame.mixer.music.play(loops=0)


def on_closing_music(root: tk.Toplevel):
    global _state_music
    if messagebox.askokcancel("Salir", "¿Salir del panel de música?"):
        _state_music = False
        root.destroy()


def music_popup(root: tk.Toplevel):
    global _state_music
    if _state_music:
        messagebox.showerror("Error", "Esta ventana ya está corriendo")
        return -1

    _state_music = True
    music_window = tk.Toplevel()
    music_window.protocol("WM_DELETE_WINDOW", lambda: on_closing_music(music_window))
    music_window.resizable(width=False, height=False)

    music_type = tk.Label(
        master=music_window,
        text="Rock Progresivo",
        bg=colorscheme[2],
        fg=colorscheme[1],
        font=("Times New Roman", "30", "italic")
    )
    music_play_button = tk.Button(
        master=music_window,
        text="Tocar la canción",
        bg=colorscheme[0],
        fg=colorscheme[1],
        activebackground=colorscheme[3],
        activeforeground=colorscheme[1],
        font=("Times New Roman", "30", "italic"),
        command=play_music
    )

    pink_floyd_image = Image.open("api/assets/grupo.png")
    pink_floyd_image_tk = ImageTk.PhotoImage(image=pink_floyd_image)
    pink_floyd_widget = tk.Label(music_window, image=pink_floyd_image_tk)
    pink_floyd_widget.photo = pink_floyd_image_tk
    music_type.grid(row=0, column=0, sticky="nsew")
    pink_floyd_widget.grid(row=1, column=0, sticky="nsew")
    music_play_button.grid(row=2, column=0, sticky="nsew")


def open_pi_prompt(root: tk.Tk):
    global _state
    if _state:
        messagebox.showerror("Error", "Esta ventana ya está corriendo")
        return -1

    _state = True
    # Dracula theme | https://github.com/dracula/dracula-theme

    pi_window = tk.Toplevel(root)
    pi_window.config(
        bg=colorscheme[0]
    )
    pi_window.resizable(width=False, height=False)
    pi_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(pi_window))

    result_title = tk.Label(
        master=pi_window,
        text="Rodrigo Arce Bastos",
        bg=colorscheme[2],
        fg=colorscheme[1],
        padx=30,
        pady=5,
        relief="flat",
        font=("Times New Roman", 20),
    )

    carne_title = tk.Label(
        relief="flat",
        master=pi_window,
        text="2024115582",
        bg=colorscheme[0],
        fg=colorscheme[1],
        font=("Times New Roman", 20),
    )

    biography_label = tk.Label(
        text="""
Soy Rodri, tengo 18 años, cumplo años el 7 de
enero y tengo afición por la informática y la
investigación.
Mi sueño es trabajar en la investigación de
máquinas cuánticas. Me gusta el software libre
y el Open Source. 

        """,
        relief="flat",
        master=pi_window,
        bg=colorscheme[2],
        fg=colorscheme[1],
        font=("Times New Roman", 14),
    )

    music_button = tk.Button(
        text="Música",
        relief="flat",
        master=pi_window,
        bg=colorscheme[3],
        fg=colorscheme[1],
        activebackground=colorscheme[0],
        activeforeground=colorscheme[1],
        padx=10,
        pady=10,
        font=("Times New Roman", 25),
        command=lambda: music_popup(pi_window)
    )
    get_back_button = tk.Button(
        text="Volver al menú",
        relief="flat",
        master=pi_window,
        bg=colorscheme[2],
        fg=colorscheme[1],
        activebackground=colorscheme[3],
        activeforeground=colorscheme[1],
        font=("Times New Roman", 14),
        command=lambda: on_closing(pi_window)
    )

    image_of_myself = Image.open("api/assets/yo.jpg").resize((300, 300))
    image_of_myself_tk = ImageTk.PhotoImage(image=image_of_myself)
    me_image = tk.Label(pi_window, image=image_of_myself_tk, bg="#171925")
    me_image.photo = image_of_myself_tk

    image_of_place = Image.open("api/assets/mapa.png").resize((300, 300))
    image_of_place_tk = ImageTk.PhotoImage(image=image_of_place)
    place = tk.Label(pi_window, image=image_of_place_tk, bg=colorscheme[0])
    place.photo = image_of_place_tk

    image_of_desktop = Image.open("api/assets/desktop.png").resize((300, 150))
    image_of_desktop_tk = ImageTk.PhotoImage(image=image_of_desktop)
    desktop = tk.Label(pi_window, image=image_of_desktop_tk, bg=colorscheme[0])
    desktop.photo = image_of_desktop_tk

    me_image.grid(row=0, column=0, rowspan=2, sticky="nsew")
    result_title.grid(row=0, column=1, sticky="nsew")
    carne_title.grid(row=1, column=1, sticky="nsew")
    ttk.Separator(pi_window, orient="horizontal").grid(row=2, column=0, columnspan=2, sticky="nsew")
    place.grid(row=3, column=1, sticky="nsew")
    music_button.grid(row=4, column=1, sticky="nsew")
    desktop.grid(row=4, column=0, sticky="nsew")
    biography_label.grid(row=3, column=0, sticky="nsew")
    get_back_button.grid(row=5, column=0, columnspan=2, sticky="nsew")

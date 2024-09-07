from tkinter import *
import api

root = Tk()

color_palette = [
    "#001C30",
    "#176B87",
    "#64CCC5",
    "#DAFFFB"
]

color_buttons = [
    "#0C134F",
    "#1D267D",
    "#5C469C",
    "#D4ADFC"
]

# Definicion de la ventana
root.title("Introducción a la programación - CE1101")
root.resizable(width=False, height=False)

root.config(
    bg=color_palette[0]
)

fibonacci_button = Button(
    text="Análisis de números",
    justify="left",
    width=30,
    compound="left",
    pady=15,
    bg=color_buttons[0],
    fg=color_palette[3],
    activebackground=color_palette[0],
    activeforeground=color_buttons[3],
    relief="flat",
    overrelief="flat",
    font=("Times New Roman", 40),
    command=lambda: api.open_fibonacci_prompt(root=root, palette=color_palette)
)
personal_info_button = Button(
    width=30,
    text="Información del programador",
    justify="left",
    pady=15,
    compound="left",
    bg=color_buttons[1],
    fg=color_palette[3],
    activebackground=color_palette[0],
    activeforeground=color_buttons[3],
    command=lambda: api.open_pi_prompt(root),
    relief="flat",
    overrelief="flat",
    font=("Times New Roman", 40)
)
animation_button = Button(
    justify="left",
    compound="left",
    width=30,
    pady=15,
    text="Animación",
    bg=color_buttons[2],
    fg=color_palette[3],
    activebackground=color_palette[0],
    activeforeground=color_buttons[3],
    relief="flat",
    overrelief="flat",
    command=lambda: api.open_animation_prompt(root),
    font=("Times New Roman", 40)
)
title = Label(
    text="Opciones del programa",
    font=("Times New Roman", 60),
    bg=color_palette[0],
    fg=color_palette[3],
    pady=20,
)
title.pack()
fibonacci_button.pack()
personal_info_button.pack()
animation_button.pack()

root.mainloop()

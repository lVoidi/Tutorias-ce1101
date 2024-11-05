from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk
import time

calls_pila = 0
calls_cola = 0


def fib_pila(n):
    global calls_pila
    calls_pila += 1
    if n <= 1:
        return n

    return fib_pila(n - 1) + fib_pila((n - 2))


def fib_cola(n, num1=0, num2=1):
    global calls_cola
    calls_cola += 1
    if n == 0:
        return num1
    if n == 1:
        return num2

    return fib_cola(n - 1, num2, num1 + num2)


def get_results(f, n):
    global fn
    # Retorna el ∆t, dada una función f
    initial = time.time()
    result = f(n)
    final = time.time()
    return final - initial, result


def on_entry_input(n, output_entry):
    global calls_pila, calls_cola
    try:
        n = int(n)
        if n <= 0:
            raise TypeError
    except (TypeError, ValueError):
        messagebox.showerror("Error", "El número debe ser un número natural distinto a cero")
        return
    n = int(n)

    t_pila, r_pila = get_results(fib_pila, n)
    t_cola, r_cola = get_results(fib_cola, n)

    output_entry.config(text=f"""
 Recursividad de cola    
∆t = {t_cola}           
Fɴ = {r_cola} 
Llamadas = {calls_cola}
---------------------   
 Recursividad de pila
∆t = {t_pila}
Fɴ = {r_pila}
Llamadas = {calls_pila}
""")
    calls_cola = 0
    calls_pila = 0


_state = False


def on_closing(root: tk.Toplevel):
    global _state
    if messagebox.askokcancel("Salir", "¿Salir de análisis de número?"):
        _state = False
        root.destroy()


def open_fibonacci_prompt(root: tk.Tk, palette: list):
    global _state
    if _state:
        messagebox.showerror("Error", "Esta ventana ya está corriendo")
        return -1

    _state = True

    result_color = "#1B1A55"

    fibonacci_window = tk.Toplevel(root)
    fibonacci_window.resizable(width=False, height=False)
    fibonacci_window.config(
        bg=result_color
    )
    title = tk.Label(
        master=fibonacci_window,
        text="Cálculo de la secuencia de fibonacci,\n dado un número n ∈ N*",
        font=("Times New Roman", 25),
        bg=palette[0],
        fg=palette[3]
    )

    entry_output = tk.Label(
        master=fibonacci_window,
        bg=result_color,
        fg=palette[3],
        relief="flat",
        font=("Times New Roman", 13),
    )
    result_title = tk.Label(
        master=fibonacci_window,
        text="Resultados",
        width=30,
        bg=result_color,
        fg=palette[3],
        relief="flat",
        font=("Times New Roman", 20),
    )

    entry_input = tk.Entry(
        master=fibonacci_window,
        bg=palette[1],
        fg=palette[3],
        justify="center",
        relief="flat",
        font=("Times New Roman", 20)
    )
    calculate_button = tk.Button(
        master=fibonacci_window,
        text="Presione para utilizar el número digitado",
        relief="flat",
        bg="#0C134F",
        fg=palette[3],
        activebackground=palette[0],
        activeforeground=palette[3],
        font=("Times New Roman", 20),
        command=lambda: on_entry_input(entry_input.get(), entry_output)
    )
    get_back_button = tk.Button(
        text="Volver al menú",
        relief="flat",
        master=fibonacci_window,
        bg=palette[0],
        fg=palette[1],
        activebackground=palette[3],
        activeforeground=palette[1],
        font=("Times New Roman", 14),
        command=lambda: on_closing(fibonacci_window)
    )

    fibonacci_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(fibonacci_window))

    fibonacci_window.title("Calcule la secuencia de fibonacci para un número natural n")
    title.grid(row=0, column=0, columnspan=2, sticky="nsew")
    entry_input.grid(row=1, column=0, columnspan=2, sticky="nsew")
    calculate_button.grid(row=3, column=0, columnspan=2, sticky="nsew")

    result_title.grid(row=0, column=2, sticky="nsew")
    entry_output.grid(row=1, column=2, rowspan=5, sticky="nsew")
    # Imagen de fibonacci
    image = Image.open("api/assets/fibonacci.png")
    image_tk = ImageTk.PhotoImage(image=image)

    p = tk.Label(fibonacci_window, image=image_tk)
    p.photo = image_tk
    p.grid(row=4, column=0, columnspan=2, sticky="nsew")
    get_back_button.grid(row=5, column=0, columnspan=2, sticky="nsew")

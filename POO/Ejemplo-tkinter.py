import tkinter as tk

WIDTH = 600
HEIGHT = 800


class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()

        # Este es un título que quiero cambiar luego, por eso
        # es importante crear un atributo para poder usarlo a lo
        # largo de toda la clase
        self.title = None

        # El orden importa, así que asegúrense que tiene un orden correcto
        self.create_attributes()
        self.create_title()
        self.create_buttons()

    def create_attributes(self):
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.resizable(False, False)

    def create_title(self):
        # Modificamos el título y le ponemos la label que es
        self.title = tk.Label(
            self, text="Este es un titulo para nuestro hermoso programa"
        )
        self.title.pack()

    def create_buttons(self):
        button_1 = tk.Button(
            self, text="Este boton hace algo", command=self.do_something
        )

        button_2 = tk.Button(self, text="Salir", command=self.destroy)

        button_1.pack()
        button_2.pack()

    def do_something(self):
        self.title["text"] = "hice algo!"

        # Llama a la función de undo_something
        # luego de 1.5 segundos (1500 milisegundos)
        self.after(1500, self.undo_something)

    def undo_something(self):
        self.title["text"] = "Este es un título para nuestro hermoso programa"


def main():
    root = Ventana()
    root.mainloop()


if __name__ == "__main__":
    main()

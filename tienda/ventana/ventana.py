import tkinter as tk
from .barrademenu.barrademenu import BarraDeMenu  # Importación absoluta
class Ventana:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("tienda v1")

        width = 900
        height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        position_right = int(screen_width / 2 - width / 2)
        position_down = int(screen_height / 2 - height / 2)

        # Configurar la geometría de la ventana con tamaño y posición
        self.root.geometry(f"{width}x{height}+{position_right}+{position_down}")

        # Inicializar la barra de menú
        self.barra_de_menu = BarraDeMenu(self)

    def mostrar(self):
        self.root.mainloop()
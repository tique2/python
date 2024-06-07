import tkinter as tk
from .occiones.occionesmenu import OpcionesMenu  # Importación absoluta

class BarraDeMenu:
    def __init__(self, ventana):
        self.root = ventana.root
        self.menu_bar = tk.Menu(self.root)
        self.submenu = OpcionesMenu(self.root)

        self.crear_menus()

    def crear_menus(self):
        menu_productos = self.crear_menu_productos()
        menu_proveedores = self.crear_menu_proveedores()
        menu_ventas = self.crear_menu_ventas()

        # Añadir los menús en orden alfabético
        self.menu_bar.add_cascade(label="Productos", menu=menu_productos)
        self.menu_bar.add_cascade(label="Proveedores", menu=menu_proveedores)
        self.menu_bar.add_cascade(label="Ventas", menu=menu_ventas)

        self.root.config(menu=self.menu_bar)

    def crear_menu_productos(self):
        menu_productos = tk.Menu(self.menu_bar, tearoff=0)
        menu_productos.add_command(label="Mostrar Productos", command=lambda: self.submenu.alternar_panel("productos"))
        menu_productos.add_command(label="Ocultar Productos", command=lambda: self.submenu.limpiar_panel())
        return menu_productos

    def crear_menu_proveedores(self):
        menu_proveedores = tk.Menu(self.menu_bar, tearoff=0)
        menu_proveedores.add_command(label="Mostrar Proveedores", command=lambda: self.submenu.alternar_panel("proveedores"))
        menu_proveedores.add_command(label="Ocultar Proveedores", command=lambda: self.submenu.limpiar_panel())
        return menu_proveedores

    def crear_menu_ventas(self):
        menu_ventas = tk.Menu(self.menu_bar, tearoff=0)
        menu_ventas.add_command(label="Mostrar Ventas", command=lambda: self.submenu.alternar_panel("ventas"))
        menu_ventas.add_command(label="Ocultar Ventas", command=lambda: self.submenu.limpiar_panel())
        return menu_ventas
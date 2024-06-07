import tkinter as tk
from .PanelProductos.PanelProductos import PanelProductos
from .PanelProveedores.PanelProveedores import PanelProveedores
from .PanelVentas.PanelVentas import PanelVentas
class OpcionesMenu:
    def __init__(self, root):
        self.root = root
        self.panel_actual = None
        self.ultimo_seleccionado = None
        self.paneles = {
            "productos": PanelProductos(self.root),
            "proveedores": PanelProveedores(self.root),
            "ventas": PanelVentas(self.root)
        }

    def alternar_panel(self, nombre_panel):
        if self.ultimo_seleccionado == nombre_panel:
            self.limpiar_panel()
            self.ultimo_seleccionado = None
        else:
            self.limpiar_panel()
            self.panel_actual = self.paneles[nombre_panel]
            self.panel_actual.mostrar()
            self.ultimo_seleccionado = nombre_panel

    def limpiar_panel(self):
        if self.panel_actual is not None:
            self.panel_actual.ocultar()
            self.panel_actual = None
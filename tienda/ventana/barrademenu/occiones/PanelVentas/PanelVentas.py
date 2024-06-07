import tkinter as tk

class PanelVentas:
    def __init__(self, root):
        self.root = root
        self.panel_principal = tk.Frame(self.root)
        
        # Panel secundario
        self.panel_secundario = tk.Frame(self.panel_principal, bg="blue")
        self.panel_secundario.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        self.titulo = tk.Label(self.panel_secundario, text="Ventas", bg="blue", fg="white", font=("Helvetica", 16))
        self.titulo.pack(fill='both', expand=True)
        
        # Botones de navegación
        self.panel_navegacion = tk.Frame(self.panel_secundario, bg="blue")
        self.panel_navegacion.pack(side="bottom", fill="x")
        self.btn_insertar = tk.Button(self.panel_navegacion, text="Insertar", command=self.mostrar_insertar)
        self.btn_insertar.pack(side="left", padx=10, pady=5)
        self.btn_actualizar = tk.Button(self.panel_navegacion, text="Actualizar", command=self.mostrar_actualizar)
        self.btn_actualizar.pack(side="left", padx=10, pady=5)
        self.btn_eliminar = tk.Button(self.panel_navegacion, text="Eliminar", command=self.mostrar_eliminar)
        self.btn_eliminar.pack(side="left", padx=10, pady=5)
        
        # Formulario de insertar
        self.panel_insertar = self.crear_formulario("Insertar Producto", self.guardar_producto)
        
        # Formulario de actualizar
        self.panel_actualizar = self.crear_formulario("Actualizar Producto", self.actualizar_producto)
        
        # Formulario de eliminar
        self.panel_eliminar = tk.Frame(self.panel_principal, bg="white")
        self.panel_eliminar.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.39)
        tk.Label(self.panel_eliminar, text="ID del producto a eliminar:").grid(row=0, column=0, sticky='e', pady=5, padx=10)
        self.entry_id_eliminar = tk.Entry(self.panel_eliminar)
        self.entry_id_eliminar.grid(row=0, column=1, pady=5, padx=10, sticky='we')
        tk.Button(self.panel_eliminar, text="Eliminar Producto", command=self.eliminar_producto).grid(row=1, column=0, columnspan=2, pady=10)
        self.panel_eliminar.grid_columnconfigure(1, weight=1)
        
        # Mostrar el panel principal
        self.mostrar_insertar()

    def crear_formulario(self, titulo, comando_guardar):
        panel = tk.Frame(self.panel_principal, bg="white")
        panel.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.29)
        tk.Label(panel, text=titulo, font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(panel, text="Nombre del producto:").grid(row=1, column=0, sticky='e', pady=5, padx=10)
        entry_nombre = tk.Entry(panel)
        entry_nombre.grid(row=1, column=1, pady=5, padx=10, sticky='we')
        tk.Label(panel, text="Cantidad:").grid(row=2, column=0, sticky='e', pady=5, padx=10)
        entry_cantidad = tk.Entry(panel)
        entry_cantidad.grid(row=2, column=1, pady=5, padx=10, sticky='we')
        tk.Label(panel, text="Precio:").grid(row=3, column=0, sticky='e', pady=5, padx=10)
        entry_precio = tk.Entry(panel)
        entry_precio.grid(row=3, column=1, pady=5, padx=10, sticky='we')
        tk.Label(panel, text="Total:").grid(row=4, column=0, sticky='e', pady=5, padx=10)
        label_total = tk.Label(panel, text="0")
        label_total.grid(row=4, column=1, sticky='e', pady=5, padx=10)
        tk.Button(panel, text="Calcular Total", command=lambda: self.calcular_total(entry_cantidad, entry_precio, label_total)).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(panel, text="Guardar", command=lambda: comando_guardar(entry_nombre, entry_cantidad, entry_precio, label_total)).grid(row=6, column=0, columnspan=2, pady=10)
        panel.grid_columnconfigure(1, weight=1)
        return panel

    def mostrar_insertar(self):
        self.panel_insertar.lift()

    def mostrar_actualizar(self):
        self.panel_actualizar.lift()

    def mostrar_eliminar(self):
        self.panel_eliminar.lift()

    def calcular_total(self, entry_cantidad, entry_precio, label_total):
        try:
            cantidad = int(entry_cantidad.get())
            precio = float(entry_precio.get())
            total = cantidad * precio
            label_total.config(text=str(total))
        except ValueError:
            label_total.config(text="Error: Ingresa números válidos")
    
    def guardar_producto(self, entry_nombre, entry_cantidad, entry_precio, label_total):
        nombre = entry_nombre.get()
        cantidad = entry_cantidad.get()
        precio = entry_precio.get()
        total = label_total.cget("text")
        print(f"Guardado: Nombre={nombre}, Cantidad={cantidad}, Precio={precio}, Total={total}")
    
    def actualizar_producto(self, entry_nombre, entry_cantidad, entry_precio, label_total):
        nombre = entry_nombre.get()
        cantidad = entry_cantidad.get()
        precio = entry_precio.get()
        total = label_total.cget("text")
        print(f"Actualizado: Nombre={nombre}, Cantidad={cantidad}, Precio={precio}, Total={total}")

    def eliminar_producto(self):
        id_producto = self.entry_id_eliminar.get()
        print(f"Eliminado: ID={id_producto}")

    def mostrar(self):
        self.panel_principal.pack(fill='both', expand=True)

    def ocultar(self):
        self.panel_principal.pack_forget()
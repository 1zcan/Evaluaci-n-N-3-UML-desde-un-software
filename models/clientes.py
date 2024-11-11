class clientes:
    def __init__(self, run, nombre, apellido, telefono, id_comuna, nombre_comuna):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.id_comuna = id_comuna
        self.nombre_comuna = nombre_comuna

    def __repr__(self):
        return f"Cliente({self.run}, {self.nombre}, {self.apellido}, {self.telefono}, {self.id_comuna}, {self.nombre_comuna})"

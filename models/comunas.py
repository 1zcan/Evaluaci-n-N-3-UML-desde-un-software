class comunas:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __repr__(self):
        return f"Departamento({self.id}, {self.nombre})"

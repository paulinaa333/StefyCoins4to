class beneficios():
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo

    def __str__(self):
        return f"{self.nombre} (Costo: {self.costo} coins)"

class cambiarFecha(beneficios):
    def __init__(self, nombre="Cambiar fecha de entrega", costo=50):
        super().__init__(nombre, costo)
        self.descripcion = "Permite cammbiar la fecha de entrega de una trabajo evaluativo"

class puntosExtra(beneficios):
    def __init__(self, nombre="Puntos extra", costo=80):
        super().__init__(nombre, costo)
        self.descripcion = "Suma puntos extra a una evaluación"

class tutorias(beneficios):
    def __init__(self, nombre="Tutorias", costo=30):
        super().__init__(nombre, costo)
        self.descripcion = "Permite cambiar la fecha o no asistir a una tutoria sin poner 1/2"
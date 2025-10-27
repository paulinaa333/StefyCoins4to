from tareas import trabajoPractico

class usuario():
    def __init__(self,id,nombre,apellido,password,correo,edad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.password = password
        self.correo = correo
        self.edad = edad

class profesor(usuario):
    def __init__(self,id,nombre,apellido,password,correo,edad,especialidad):
        super().__init__(id,nombre,apellido,password,correo,edad)
        self.especialidad = especialidad

    def asignarTarea(self,estudiante,tarea):
        estudiante.tareas.append(tarea)

    def chequearEntrega(self,estudiante,tarea):
        for t in estudiante.tareas:
            if t == tarea:
                print(f"La tarea '{t.descripcion}' ha sido marcada como entregada: {t.entrega}")
    def aprobarTarea(self,estudiante,tarea):
        for t in estudiante.tareas:
            if t == tarea:
                estudiante.coins=tarea.valor
                t.aprobado=True
            print(f"El estudiante {estudiante.nombre} posee {estudiante.coins} mondedas")
        
class estudiante(usuario):
    def __init__(self,id,nombre,apellido,password,correo,edad,curso,legajo,coins=0):
        super().__init__(id,nombre,apellido,password,correo,edad)
        self.curso = curso
        self.legajo = legajo
        self.coins = coins
        self.tareas = []

    def entregarTarea(self,tarea):
        for t in self.tareas:
            if t == tarea:
                t.entrega = True


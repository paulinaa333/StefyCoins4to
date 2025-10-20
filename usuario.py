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



        
class estudiante(usuario):
    def __init__(self,id,nombre,apellido,password,correo,edad,curso,legajo,coins=0):
        super().__init__(id,nombre,apellido,password,correo,edad)
        self.curso = curso
        self.legajo = legajo
        self.coins = coins
        self.tareas = []


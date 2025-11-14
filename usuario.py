from tareas import trabajoPractico
from emailTest import EmailSender, correo 
from beneficios import beneficios

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

    def asignarTarea(self,estudiante, tarea):
        estudiante.tareas.append(tarea)
        correo = EmailSender("programacion4to25@gmail", "vgao udel ynsg neii")
        correo.enviar_mail(
                destinatario=estudiante.correo,
                asunto="Tarea Asignada",
                mensaje=f"Hola {estudiante.nombre}, tu tarea '{tarea.descripcion}' ha sido aprobada. ¡Felicidades! Has ganado {tarea.valor} monedas."
            )

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

        correo = EmailSender("programacion4to26@gmail.com", "vgao udel ynsg neii")
        correo.enviar_mail(
            destinatario=estudiante.correo,
            asunto="Tarea Aprobada",
            mensaje=f"Hola {estudiante.nombre}, tu tarea '{tarea.descripcion}' ha sido aprobada. ¡Felicidades! Has ganado {tarea.valor} monedas."
        )

    def verBeneficios(self):
        for b in beneficios:
            print(f"Beneficio: {b.nombre}, Descripción: {b.descripcion}, Costo en StefyCoins: {b.costo}")


        
class estudiante(usuario):
    def __init__(self,id,nombre,apellido,password,correo,edad,curso,legajo,coins=0):
        super().__init__(id,nombre,apellido,password,correo,edad)
        self.curso = curso
        self.legajo = legajo
        self.coins = coins
        self.tareas = []
        self.beneficios = []
    def chequearTareas(self):
        for t in self.tareas:
            print(f"Tarea: {t.descripcion}, Entregada: {t.entrega}, Estado: {t.estado}")

    def entregarTarea(self,tarea):
        for t in self.tareas:
            if t == tarea:
                t.entrega = True

    def canjearBeneficios(self, beneficios, profesor):
        for b in self.beneficios:
            if b == beneficios:
                b.canjear = True

    def verBeneficios(self):
        for b in beneficios:
            print(f"Beneficio: {b.nombre}, Descripción: {b.descripcion}, Costo en StefyCoins: {b.costo}")
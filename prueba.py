from beneficios import tutorias, puntosExtra, cambiarFecha
from usuario import profesor, estudiante
from tareas import trabajoPractico

estudiante1 = estudiante(nombre="Stefi",
                          apellido="Lopez",
                            edad=22, 
                            legajo=1234, 
                            curso="4to A", 
                            correo="", 
                            password="", 
                            id=1)

profesor1 = profesor(nombre="Juan", 
                     apellido="Perez", 
                     edad=40, 
                     especialidad="Matematica", 
                     correo="", 
                     password="", 
                     id=1)

tarea1= trabajoPractico(consigna="esto es una consigna de Tarea1", 
                        fechaEntrega="12/10/2025", 
                        criterioEvaluacion="Hacer el trabajo Práctico")


profesor1.asignarTarea(estudiante1,tarea1)

print(estudiante1.tareas)

profesor1.chequearEntrega(estudiante1, tarea1)

estudiante1.entregarTarea(tarea1)

profesor1.chequearEntrega(estudiante1, tarea1)


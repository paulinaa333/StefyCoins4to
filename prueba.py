from beneficios import tutorias, puntosExtra, cambiarFecha
from usuario import profesor, estudiante
from tareas import trabajoPractico,proyectoExtra



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

tarea2= proyectoExtra(consigna="esto es una consigna de Tarea2", 
                        fechaEntrega="25/10/2025", 
                        criterioEvaluacion="Hacer el trabajo Práctico")


profesor1.asignarTarea(estudiante1,tarea1)

print(estudiante1.tareas)

profesor1.chequearEntrega(estudiante1, tarea1)

estudiante1.entregarTarea(tarea1)

#Clase Dia 27/10

profesor1.chequearEntrega(estudiante1, tarea1)

profesor1.aprobarTarea(estudiante1,tarea1)

profesor1.asignarTarea(estudiante1,tarea2)

print(estudiante1.tareas)

profesor1.aprobarTarea(estudiante1,tarea2)

#Cómo hacemos para que una tarea que no está asignada pueda avisar al querer aprobada?
#Cómo hago para visualizar TODOS los estados de las tareas del Estudiante?
#Si creo más estudiantes de un curso, poseen las mismas tareas asignadas? Cómo hago para que compartan las tareas asignadas?







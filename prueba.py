from beneficios import tutorias, puntosExtra, cambiarFecha
from usuario import profesor, estudiante
from tareas import trabajoPractico, proyectoExtra

print("StefyCoins")

estudiante1 = estudiante(nombre="Paulina",
                          apellido="Ramos",
                            edad=22, 
                            legajo=1234, 
                            curso="4to A", 
                            correo="piramosbobatto@escuelasproa.edu.ar", 
                            password="110809", 
                            id=1)

profesor1 = profesor(nombre="Ignacio", 
                     apellido="Sanchez", 
                     edad=40, 
                     especialidad="Programacion", 
                     correo="jisanchezsolano@escuelasproa.edu.ar", 
                     password="165533", 
                     id=1)

profesor1.estudiante1.append(estudiante1)

print("Tarea asignada")

tarea1= trabajoPractico(consigna="Entregar trabajos practicos en tiempo y forma", 
                        fechaEntrega="12/10/2025", 
                        criterioEvaluacion="Hacer el trabajo Práctico",
                        valor=200,)

tarea2= proyectoExtra(consigna="Entregar proyecto extra",
                        fechaEntrega="20/11/2025", 
                        criterioEvaluacion="Hacer el proyecto extra",
                        valor=1000,)


profesor1.asignarTarea(estudiante1,tarea1)
profesor1.asignarTarea(estudiante1,tarea2)

print("Mostrar tarea")
estudiante1.chequearTareas()

print("Entregar tarea")
estudiante1.entregarTarea(tarea1)

estudiante1.chequearTareas()

print("Aprobar tarea")
profesor1.aprobarTarea(estudiante1,tarea1)

estudiante1.chequearTareas()

print("Beneficios")

beneficios = [tutorias,
             puntosExtra, 
             cambiarFecha
             ]

estudiante1.verBeneficios(beneficios)

print("Canjear beneficio")

tutoria = tutorias()
estudiante1.canjearBeneficios(tutorias)

punto = puntosExtra()
estudiante1.canjearBeneficios(puntosExtra)

fecha = cambiarFecha()
estudiante1.canjearBeneficios(cambiarFecha)

print("El profesor ve los beneficios canjeados por el estudiante")
profesor1.verBeneficios(estudiante1)

estudiante1.chequearTareas()
print("Tarea finalizada")


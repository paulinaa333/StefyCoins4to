class Tarea():
    def __init__(self,valor,descripcion,consigna,fechaEntrega,criterioEvaluacion):
        self.valor = valor
        self.descripcion = descripcion
        self.consigna=consigna
        self.fechaEntrega=fechaEntrega
        self.criterioEvaluacion=criterioEvaluacion


class trabajoPractico(Tarea):
    def __init__(self,consigna,fechaEntrega,criterioEvaluacion):
        descripcion = "Trabajo Practico"
        valor = 200
        super().__init__(valor,descripcion,consigna,fechaEntrega,criterioEvaluacion)



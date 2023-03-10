from nodo import *
class ListaEnlazada:
    def __init__(self):
     self.primero = None
    

    def insertar(self, receta):
        if self.primero is None:
         self.primero = Nodo(receta)
         return
        actual = self.primero
        while actual.siguiente:
          actual = actual.siguiente
        actual.siguiente = Nodo(receta)


    def recorrer(self):
     actual = self.primero

     while actual != None:
         print('Paciente: ', actual.receta.paciente, '- Fecha de nacimiento: ', actual.receta.fecha_nac, '- Doctor: ', actual.receta.doctor, '- Colegiado: ', actual.receta.colegiado, '- Fecha de cita: ', actual.receta.fecha_cita, '- Hora de cita: ', actual.receta.hora_cita, '- Tipo de consulta: ', actual.receta.tipo_consulta, '- Tratamiento: ', actual.receta.tratamiento)
         actual = actual.siguiente


    def eliminar(self, colegiado, fechaCita, horaCita):
     actual = self.primero
     anterior = None

     while actual and actual.receta.colegiado != colegiado and actual.receta.fechaCita != fechaCita and actual.receta.horaCita != horaCita:
          anterior = actual
          actual = actual.siguiente

     if anterior is None:
          self.primero = actual.siguiente
          actual.siguiente = None
     elif actual:
         anterior.siguiente = actual.siguiente
         actual.siguiente = None 

 #hoja de trabajo 3
    def buscar_modificar(self, paciente, fechaCita, horaCita):
       actual = self.primero

       while actual != None:
          if actual.receta.paciente == paciente:
              actual.receta.fechaCita = fechaCita
              actual.receta.horaCita = horaCita
              return None
          actual = actual.siguiente
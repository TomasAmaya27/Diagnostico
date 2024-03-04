#Crear una clase llamada vehiculo capaz de procesar la informacion basica de los autos en una concecionaria debera tener constructor y los atributos de el vehiculo seran: patente,marca,modelo,kilometraje. crear metodos (de acceso) getter y (modificacion) setter. Mostrar en pantalla al menos un atributo y modificar el kilometraje

class vehiculo:
  def __int__ (self, patente, marca, modelo, kilometraje):
    self.patente = patente
    self.marca = marca
    self.modelo = modelo
    self.kiometraje = kilometraje

def get_patente (self):
  return self.patente

def get_marca (self):
  return self.marca

def get_modelo (self):
return self.modelo

def get_kilometraje (self):
  return self.kilometraje

def set_kilometraje (self, nuevo_kilometraje):
  self.kilometraje = nuevo kilometraje

mi_auto = Vehiculo("ABC123", "Renault", "12","30000")

print("Marca del vehiculo:", mi_auto.get_marca())

print("Kilometraje antes de la modificacion:", mi_auto_get_kilometraje())
mi_auto.set_kilometraje(55000)
print("Kilometraje despues de la modificacion:", mi_auto.get_kilometraje())


#Crear un programa que simule la entrada a un boliche. debe dejar ingresar la edad al usuario, si es mayor a 18 mostrar por pantalla "Puede ingresar", de lo contrario mostrar por pantalla "No puede ingresar"

edad =int(input("Ingrese su edad: "))

if edad  >= 18:
  print ("Puedo ingresar")
else:
  print("No puedo ingresar")

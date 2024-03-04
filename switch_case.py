def obtener_nombre_dia(numero):
  switcher =  {
    1: "Lunes",
    2: "Martes",
    3: "Miercoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sabado",
    7: "Domingo",

    }
return switcher.get(numero, "Numero de dia invalido")

def main()
try:
  numero_dia = int(input("Ingrese un numero del 1 al 7: "))
  nombre_dia = obtener_nombre_dia(numero_ dia)
  print("El dia correspondiente al numero", numero_dia, "es:", nombre_dia)
except ValueError:
  print("Error: Ingrese un numero valido del 1 al 7. ")

if __name__ == "__main__":
  main()
  

import os
from pinturas import Pintura

paintings = []

def cls():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    
def validacion_nombre():
  nombre = input("Introduzca el nombre de su pintura: \n")
  if len(nombre) <= 30:
     return nombre
  else: 
    print("Asegúrese de que la cantidad de caracteres no exceda de 30")
    validacion_nombre()

def validacion_cota():
  cota = input("Introduzca la Cota: \n")
  digitos = sum(c.isdigit() for c in cota)
  letras = sum(c.isalpha() for c in cota)
  if (digitos == 4) and (letras == 4): 
    cota = cota.upper()
    return cota
  else: 
    print("Asegúrese de que la cota contenga 4 letras y 4 dígitos.")
    validacion_cota()
    
def validacion_precio():
  try:
    precio = float(input("Introduzca el precio de la pintura: \n"))
    assert precio > 0
    
  except (ValueError, AssertionError):
    print("Introduzca un número valido.")
    validacion_precio()
    
 def validacion_status():
  status = input("Introduzca el status de la pintura: \n").upper()
  if status == "EN EXHIBICION" or status == "EN MANTENIMIENTO":
    return status
  else:
    print("Asegúrese de introducir un status válido. Hint: EN EXHIBICION/EN MANTENIMIENTO")
    validacion_status() 

def regPintura():
  name = validacion_nombre()
  cotaa = validacion_cota()
  price = validacion_precio()
  estado = validacion_status()
  creacion = Pintura(cotaa, name, price, estado)
  paintings.append(creacion)
    
def menu():
    print("===========================================================\nBienvenido al Sistema Manejador de Pinturas del Louvre\nCreado por Gabriella Suarez, Gabriel Useche y Roy Rodriguez\n===========================================================")
    selector = input("\nSeleccione una de las siguientes opciones:\n1. Registrar una nueva pintura.\n2. Buscar pintura por cota.\n3. Buscar pintura por nombre.\n4. Limpiar la papelera de reciclaje de pinturas.\n5. Para salir del programa.\n")
    cls()
    if selector == '1':
        regPintura()
    elif selector == '2':
        bCota()
    elif selector == '3':
        bNombre()
    elif selector == '4':
        bBasura()
    elif selector == '5':
        exit()
    else:
        input("Ha introducido un valor errado, por favor vuelva a intentarlo.\nPresione enter para reiniciar el programa...")
        cls()
        menu()


menu()

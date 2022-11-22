import os
from pinturas import Pinturas

paintings = []

def cls():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    
def validacion_nombre(nombre):
  if len(nombre) <= 30:
     return nombre
  else: 
    print("Asegúrese de que la cantidad de caracteres no exceda de 30")
    regPintura()
  

def regPintura():
  nombre = input("Introduzca el nombre de su pintura: \n")
  validacion_nombre(nombre)

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

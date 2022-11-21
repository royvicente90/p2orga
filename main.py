import os
from pathlib import Path


def regPintura(cota, nombre, precio, status):

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('db.txt')
    with p.open('a') as f:
        f.write('\n' + cota + ', ' + nombre + ', ' +
                precio + ', ' + status + ', ' + 'False')
        f.close()


def checkStatus(var):
    if var.isalpha() and (var.lower() == 'en exhibicion' or var.lower() == 'en exhibición' or var.lower() == 'en mantenimiento'):
        if var.lower() == 'en exhibición' or var.lower() == 'en exhibicion':
            return 'EN EXHIBICIÓN'
        else:
            return 'EN MANTENIMIENTO'
    else:
        return 'ERROR'


def checkNombre(var):
    if len(var) <= 30:
        return True
    else:
        return False


def checkCota(var):
    checker = True
    acum = ''
    for x in range(len(var)):
        if var[x].isalpha() and x >= 3:
            acum += var[x].upper()
        elif var[x].isnum() and (x > 3 and x <= 7):
            acum += var[x]
        else:
            checker = False
    if checker == False:
        acum = 'ERROR'
    return acum


def cls():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")


def menu():
    print("===========================================================\nBienvenido al Sistema Manejador de Pinturas del Louvre\nCreado por Gabriella Suarez, Gabriel Useche y Roy Rodriguez\n===========================================================")
    selector = input("\nSeleccione una de las siguientes opciones:\n1. Registrar una nueva pintura.\n2. Buscar pintura por cota.\n3. Buscar pintura por nombre.\n4. Limpiar la papelera de reciclaje de pinturas.\n5. Para salir del programa.\n")
    cls()
    if selector == '1':
        nuevaPintura()
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


# menu()
regPintura('AACC0011', 'El Alacran', '300', 'EN EXHIBICIÓN')

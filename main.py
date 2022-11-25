import os
from pathlib import Path


# Funcion de registrar en archivo nameIndex
def checkRegisters(name, cota):

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('cotaIndex.txt')
    with open(p) as f:
        g = f.readlines()
        l = []
        for x in g:

            l.append(x.split(';')[0])
        if cota in l:
            f.close()
            print("La cota que ha introducido ya existe. Por favor seleccione otro.\n A continuacion volvera al programa de adicion.")
            input("Presione enter para coninuar...")
            cls()
            nuevaPintura()
    f.close()

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('nameIndex.txt')
    with open(p) as f:
        g = f.readlines()
        l = []
        for x in g:

            l.append(x.split(';')[0])
        if name in l:
            f.close()
            print("El nombre que ha introducido ya existe. Por favor seleccione otro.\n A continuacion volvera al programa de adicion.")
            input("Presione enter para coninuar...")
            cls()
            nuevaPintura()

    f.close()

# Funcion de registrar en archivo nameIndex


def regIndexes(name, cota):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('nameIndex.txt')
    with p.open('a') as k:
        k.write(name + ';' + indexDB() + '\n')
    k.close()
    organizrName()

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('cotaIndex.txt')
    with p.open('a') as k:
        k.write(cota + ';' + indexDB() + '\n')
    k.close()
    organizrCota()


def organizrCota():

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('cotaIndex.txt')
    with p.open('r+') as f:
        g = sorted(f)
        f.seek(0)
        for h in g:
            f.write(h)
    f.close()


def organizrName():

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('nameIndex.txt')
    with p.open('r+') as f:
        g = sorted(f)
        f.seek(0)
        for h in g:
            f.write(h)
        f.close()


def indexDB():
    y = 1
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('db.txt')
    with p.open('r') as f:
        for x in f:
            y += 1
        f.close()
    return str(y)


# Funcion de registrar en archivo db
def regPintura(cota, nombre, precio, status):

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('db.txt')
    with p.open('a') as f:
        f.write(cota + ';' + nombre + ';' +
                precio + ';' + status + ';' + 'False' + '\n')
        f.close()

# Validador de Nombre


def checkNombre(var):
    if len(var) <= 30:
        return False
    else:
        return True

# Validador de Cota


def checkCota(var):
    checker = True
    acum = ''
    for x in range(len(var)):
        # print(checker)
        if var[x].isalpha() and x <= 3:
            acum += var[x].upper()
        elif var[x].isnumeric() and (x > 3 and x <= 7):
            acum += var[x]
        else:
            checker = False
    if checker == False:
        acum = 'ERROR'
    return acum

# Funcion input y registro de Pintura


def nuevaPintura():
    try:
        posible = ['1', '2']
        print("A continuación te pediremos los datos de la pintura a registrar:\n")
        cota = input(
            "Ingrese el codigo de la cota (Formato LLLLNNNN L=Letra N=Número): ")
        nombre = input("Ingrese el nombre de la obra (Max 30 caracteres): ")
        precio = input("Ingrese el precio de la obra: ")
        selectStatus = input(
            "Seleccione un status:\n1. EN EXHIBICIÓN.\n2. EN MANTENIMIENTO.\n")
        cls()
        cota = checkCota(cota)
        if (cota == 'ERROR') or (checkNombre(nombre)) or (int(precio) <= 0) or (selectStatus not in posible):
            print(
                "Ha cometido un error escribiendo algún dato, reiniciando el programa de adición...")
            input("Presione enter para continuar.")
            nuevaPintura()
        if selectStatus == '1':
            status = 'EN EXHIBICIÓN'
        elif selectStatus == '2':
            status = 'EN MANTENIMIENTO'
        else:
            print(
                "Ha cometido un error escribiendo algún dato, reiniciando el programa de adición...")
            input("Presione enter para continuar.")
            nuevaPintura()
    except ValueError:
        print("Ha cometido un error escribiendo algún dato, reiniciando el programa de adición...")
        input("Presione enter para continuar.")
        nuevaPintura()

    print(indexDB())
    input("presione enter para registrar")
    checkRegisters(nombre, cota)
    regIndexes(nombre, cota)
    regPintura(cota, nombre, precio, status)
    cls()
    input("La pintura ha sido agregada exitosamente.\nPresione enter para volver al menu...")
    menu()

# Funcion limpiar terminal


def cls():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

# Menu


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
        # bBasura()
        regName()
    elif selector == '5':
        exit()
    else:
        input("Ha introducido un valor errado, por favor vuelva a intentarlo.\nPresione enter para reiniciar el programa...")
        cls()
        menu()


# Funcion inicial main
menu()

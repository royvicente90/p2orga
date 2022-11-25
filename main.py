import os
from pathlib import Path



# Funcion de Restauracion Logica
def restLogic(line, index):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('db.txt')
    with open(p, 'r') as f:
        g = f.readlines()
        line = line.replace('True\n', 'False\n')
        g[index] = line
    with open(p, 'w') as h:
        h.writelines(g)

# Funcion de Borrado Logico
def borradoLogic(line, index):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('db.txt')
    with open(p, 'r') as f:
        g = f.readlines()
        line = line.replace('False\n', 'True\n')
        g[index] = line
    with open(p, 'w') as h:
        h.writelines(g)


# Funcion  de busqueda en archivo db.txt
def bDB(index):
    if index == '-1':
        print("No se ha encontrado la cota o nombre buscado.")
        input("Presione enter para volver al menu principal... ")
        cls()
        menu()
    else:
        cls()
        index = int(index.replace('\n', ""))
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        p = Path(__file__).with_name('db.txt')
        with open(p) as f:
            g = f.readlines()
            x = g[index].split(';')
            print('Cota: ' + x[0] + '\nNombre: ' + x[1] +
                  '\nPrecio: ' + x[2] + ' $\nEstatus: ' + x[3])
            if x[4].replace('\n', '') == 'True':
                print('BORRADA')
                submenu = input(
                    "\n¿Que desea hacer?\n1. Volver al menu principal.\n2. Restaurar la pintura.\n")
            else:
                submenu = input(
                    "\n¿Que desea hacer?\n1. Volver al menu principal.\n9. Borrar la pintura.\n")
            if submenu == '1':
                cls()
                menu()
            elif (submenu == '2') and (x[4].replace('\n', '') == 'True'):
                restLogic(g[index], index)
                cls()
                print("Pintura restaurada exitosamente")
                input("Presione enter para volver al menu principal...")
                menu()
            elif submenu == '9':
                print("¿Esta seguro que desea borrar la pintura?")
                x2 = input(
                    "Introduzca:\n1. Si esta de acuerdo en borrar la pintura.\n 2. Si desea volver al menu principal")
                if x2 == '2':
                    cls()
                    menu()
                elif x2 == '1':
                    borradoLogic(g[index], index)
                    cls()
                    print("Pintura borrada exitosamente")
                    input("Presione enter para volver al menu principal...")
                    menu()
                else:
                    input(
                        "Ha introducido una opción inválida, presione enter para volver al menu principal...")
                    menu()
            else:
                cls()
                input(
                    "Ha introducido una opción inválida, presione enter para volver al menu principal...")
                menu()

# Funcion de busqueda en archivo nameIndex


def bNombre():
    imp = input("Introduzca el nombre que desea buscar: ").upper()
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('nameIndex.txt')
    with open(p) as f:
        g = f.readlines()
        l = []
        for x in g:
            l.append(x.split(';'))
        # Comienzo busqueda binaria
        pasos = 0
        izq = 0
        der = len(l) - 1
        while izq <= der:
            pasos += 1
            medio = (izq + der) // 2

            if l[medio][0].upper() == imp:
                return l[medio][1]
            elif l[medio][0].upper() > imp:
                der = medio - 1
            else:
                izq = medio + 1
        return str(-1)

# Funcion de busqueda en archivo cotaIndex


def bCota():
    imp = input("Introduzca la cota que desea buscar: ").upper()
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('cotaIndex.txt')
    with open(p) as f:
        g = f.readlines()
        l = []
        for x in g:
            l.append(x.split(';'))
        # Comienzo busqueda binaria
        pasos = 0
        izq = 0
        der = len(l) - 1
        while izq <= der:
            pasos += 1
            medio = (izq + der) // 2

            if l[medio][0] == imp:
                return l[medio][1]
            elif l[medio][0] > imp:
                der = medio - 1
            else:
                izq = medio + 1
        return str(-1)

# Funcion de revisar si estan repetidos en archivo nameIndex y cotaIndex


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

            l.append(x.split(';')[0].upper())
        if name.upper() in l:
            f.close()
            print("El nombre que ha introducido ya existe. Por favor seleccione otro.\n A continuacion volvera al programa de adicion.")
            input("Presione enter para coninuar...")
            cls()
            nuevaPintura()

    f.close()

# Funcion de registrar en archivo nameIndex y cotaIndex


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

# Funcion reorganizar archivo cotaIndex


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


# Funcion reorganizar archivo nameIndex
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

# Archivo que devuelve el index donde se agregará la pintura


def indexDB():
    y = 0
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
    if (len(var) <= 30) and (';' not in var):
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
        nombre = input(
            "Ingrese el nombre de la obra (Max 30 caracteres, no puede utilizar el simbolo ;): ")
        precio = input("Ingrese el precio de la obra: ")
        selectStatus = input(
            "Seleccione un status:\n1. EN EXHIBICIÓN.\n2. EN MANTENIMIENTO.\n")
        cls()
        cota = checkCota(cota)
        if (cota == 'ERROR') or (checkNombre(nombre)) or (int(precio) <= 0) or (selectStatus not in posible):
            print(
                "Ha cometido un error escribiendo algún dato, reiniciando el programa de adición...")
            input("Presione enter para continuar.")
            cls()
            nuevaPintura()
        if selectStatus == '1':
            status = 'EN EXHIBICIÓN'
        elif selectStatus == '2':
            status = 'EN MANTENIMIENTO'
        else:
            print(
                "Ha cometido un error escribiendo algún dato, reiniciando el programa de adición...")
            input("Presione enter para continuar.")
            cls()
            nuevaPintura()
    except ValueError:
        print("Ha cometido un error escribiendo algún dato, reiniciando el programa de adición...")
        input("Presione enter para continuar.")
        cls()
        nuevaPintura()

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
    cls()
    print("===========================================================\nBienvenido al Sistema Manejador de Pinturas del Louvre\nCreado por Gabriella Suarez, Gabriel Useche y Roy Rodriguez\n===========================================================")
    selector = input("\nSeleccione una de las siguientes opciones:\n1. Registrar una nueva pintura.\n2. Buscar pintura por cota.\n3. Buscar pintura por nombre.\n4. Limpiar la papelera de reciclaje de pinturas.\n5. Para salir del programa.\n")
    cls()
    if selector == '1':
        nuevaPintura()
    elif selector == '2':
        bDB(bCota())
    elif selector == '3':
        bDB(bNombre())
    elif selector == '4':
        bBasura()
    elif selector == '5':
        exit()
    else:
        input("Ha introducido un valor errado, por favor vuelva a intentarlo.\nPresione enter para reiniciar el programa...")
        cls()
        menu()


# Funcion inicial main
menu()

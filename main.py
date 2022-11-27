import os
from pathlib import Path

# Funcion Wipe todos los index

paintings = []


def indexWipe():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('nameIndex.txt')
    b = ''
    with p.open('w') as f:
        f.seek(0)
        f.writelines(b)

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('cotaIndex.txt')
    with p.open('w') as f:
        f.seek(0)
        f.writelines(b)

# Funcion Compactador


def bBasura():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('db.txt')
    with open(p) as f:
        g = f.readlines()
        l = []
        ln = []
        for x in g:
            if x.split(';')[4] == 'False\n':
                l.append(x.split(';'))
        indexWipe()
        contador = 0
        for x in l:
            ln.append(x[0] + ';' + x[1] + ';' + x[2] + ';' + x[3] + ';' + x[4])
            regIndexes(x[1], x[0], str(contador))
            contador += 1

    with open(p, 'w') as h:
        h.seek(0)
        for a in ln:
            h.write(a)
    f.close()
    input("Base de datos compactada exitosamente.\nPresione enter para volver al menu principal...")
    menu()

# Funcion cambiar estatus para mantenimiento o en exhibicion


def changeState(line, index, mode):
    if mode == 0:
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        p = Path(__file__).with_name('db.txt')
        with open(p, 'r') as f:
            g = f.readlines()
            line = line.replace('EN EXHIBICIÓN', 'EN MANTENIMIENTO')
            g[index] = line
        with open(p, 'w') as h:
            h.writelines(g)
    elif mode == 1:
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        p = Path(__file__).with_name('db.txt')
        with open(p, 'r') as f:
            g = f.readlines()
            line = line.replace('EN MANTENIMIENTO', 'EN EXHIBICIÓN')
            g[index] = line
        with open(p, 'w') as h:
            h.writelines(g)


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
                if x[3] == 'EN MANTENIMIENTO':
                    submenu = input(
                        "\n¿Que desea hacer?\n1. Volver al menu principal.\n3. Cambiar estatus a EN EXHIBICIÓN\n9. Borrar la pintura.\n")
                elif x[3] == 'EN EXHIBICIÓN':
                    submenu = input(
                        "\n¿Que desea hacer?\n1. Volver al menu principal.\n3. Cambiar estatus a EN MANTENIMIENTO\n9. Borrar la pintura.\n")
            if submenu == '1':
                cls()
                menu()
            elif (submenu == '2') and (x[4].replace('\n', '') == 'True'):
                restLogic(g[index], index)
                cls()
                print("Pintura restaurada exitosamente")
                input("Presione enter para volver al menu principal...")
                menu()
            elif submenu == '3':
                if x[3] == 'EN EXHIBICIÓN':
                    changeState(g[index], index, 0)
                    cls()
                    print("Cambio de estatus exitoso")
                    input("Presione enter para volver al menu principal...")
                    menu()
                elif x[3] == 'EN MANTENIMIENTO':
                    changeState(g[index], index, 1)
                    cls()
                    print("Cambio de estatus exitoso")
                    input("Presione enter para volver al menu principal...")
                    menu()
            elif submenu == '9' and (x[4].replace('\n', '') == 'False'):
                cls()
                print("¿Esta seguro que desea borrar la pintura?")
                x2 = input(
                    "Introduzca:\n1. Si esta de acuerdo en borrar la pintura.\n2. Si desea volver al menu principal.\n")
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
def regIndexes(name, cota, indice):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('nameIndex.txt')
    with p.open('a') as k:
        k.write(name + ';' + indice + '\n')
    k.close()
    organizrName()

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    p = Path(__file__).with_name('cotaIndex.txt')
    with p.open('a') as k:
        k.write(cota + ';' + indice + '\n')
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

# Funcion de validacion de nombre
def validacion_nombre():
  nombre = input("Introduzca el nombre de su pintura: \n")
  if len(nombre) <= 30:
    return nombre
  else:
    print("Asegúrese de que la cantidad de caracteres no exceda de 30")
    validacion_nombre()


# Funcion de validacion de cota
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
    
# Funcion de validacion de precio
def validacion_precio():
  try:
    precio = float(input("Introduzca el precio de la pintura: \n"))
    assert precio > 0
    return precio

  except (ValueError, AssertionError):
    print("Introduzca un número valido.")
    validacion_precio()


# Funcion input y registro de Pintura
def nuevaPintura():
    print("A continuación te pediremos los datos de la pintura a registrar:\n")
  cota = validacion_cota()
  nombre = validacion_nombre()
  precio = str(validacion_precio())
  selectStatus = input(
            "Seleccione un status:\n1. EN EXHIBICIÓN.\n2. EN MANTENIMIENTO.\n")
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
  checkRegisters(nombre, cota)
  regIndexes(nombre, cota, indexDB())
  regPintura(cota, nombre, precio, status)
  cls()
  input("La pintura ha sido agregada exitosamente.\nPresione enter para volver al menu...")
  menu()


# Funcion limpiar terminal
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
        print(
            "Asegúrese de introducir un status válido. Hint: EN EXHIBICION/EN MANTENIMIENTO")
        validacion_status()

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

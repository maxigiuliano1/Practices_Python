import Comidas
import random
tipos = ['Entrada ', 'Principal ', 'Postre ']
clase = ['Estandar ', 'Sin TACC ', 'Vegentariana/s ','Light ']
entrada = ['ENSALADA','RABAS', 'BASTONES DE QUESO', 'FIAMBRES AL PLATO', 'PICADA MIXTA']
princ = ['PIZZA', 'EMPANADAS', 'PASTA', 'CARNE AL PLATO', 'ENSALADA CESAR']
postre = ['HELADO', 'TIRAMISU', 'CHEES CAKE', 'FLAN', 'BUDIN DE PAN']

def opcion2(com):
    ac = 0
    ct = 0
    agregar = 0
    print('0 = ENTRADA | 1 = PRINCIPAL | 2 = POSTRE')
    x = int(input('Elija tipo de comida que quiere consultar: '))
    n = len(com)
    for i in range(n):
        if com[i].tipo == x:
            ac += com[i].precio
            ct += 1
    if ct != 0:
        prom = ac // ct
        if prom < 100:
            for i in range(n):
                if com[i].tipo == x:
                    agregar = com[i].precio * .10
                    com[i].precio += agregar

        display(com ,tipos, clase)
        print('\nPRECIOS ACTUALIZADOS')
    else:
        print('No hay este tipo de comida en la carta')
    ac = 0
    ct = 0

def opcion3(com):
    n = len(com)
    print(n)
    for i in range(n-1):
        for j in range(i+1,n):
            if com[i].tiempo > com[j].tiempo:
                com[i], com[j] = com[j], com[i]
    print(Comidas.to_string(com[0], tipos, clase))
    for i in range(n-1):
        for j in range(i+1,n):
            if com[i].tiempo == com[j].tiempo:
                print(Comidas.to_string(com[j], tipos, clase))
            else:
                 break
        break
def opcion4(com):
    ct = 3
    c = ct * [0]
    print('Elija la clasificacion que quiere consultar: ')
    x = 7
    x = valclas(x)
    n = len(com)
    for i in range(n):
            if com[i].clasificacion == x:
                c[com[i].tipo] += 1
                print(Comidas.to_string(com[i],tipos, clase))
    print('Se han encontrado:')
    for i in range(ct):
        print(str(c[i])+' Comidas '+ clase[x] +' de tipo '+ tipos[i])

    print()
def opcion5(com):
    sugerir = []
    x = 0
    ok = False
    exist = False
    name = input('Ingrese nombre de Plato Principal para sugerencias: ')
    name = name.upper()
    n = len(com)
    for i in range(n):
        if com[i].nombre == name:
            exist = True
            if com[i].tipo == 1:
                x = com[i].clasificacion
                print(Comidas.to_string(com[i],tipos, clase))
                ok = True
    if exist:
        if ok:
            for i in range(n):
                if com[i].clasificacion == x and com[i].tipo != 1:
                    sugerir.append(com[i])
            print()
            print('\nSugerencias de Entradas y Postres')
            display(sugerir, tipos, clase)
        else:
            print('NO ES UN PLATO PRINCIPAL')
    else:
        print('no existe esta comida')

    if sugerir == [] and ok == True:
        print('No hay sugerencias para este plato')

def opcion6(com):
    menudia = []
    print('-------ELIJA UNA CLASIFICACIÓN ARMAR MENU DEL DÍA------- ')
    x = int(input('0 = ESTANDAR | 1 = SIN TACC | 2 = VEGETARIANA | 3 = LIGHT'))
    print('\nMENU DEL DÍA '+ str(clase[x].upper()))
    n = len(com)
    aux = 0
    aux2 = 0
    timer = 0
    cash = 0
    agregar = False
    for i in range(n):
        if com[i].clasificacion == x:
            if menudia == []:
                menudia.append(com[i])
            else:
                aux = len(menudia)
                for j in range(aux):
                    if menudia[j].tipo != com[i].tipo:
                        agregar = True
                    else :
                        agregar = False
                        break
        if agregar:
            menudia.append(com[i])
            agregar = False
    if menudia != []:
        k = len(menudia)
        for g in range(k-1):
            for h in range(g+1,k):
                if menudia[g].tipo > menudia[h].tipo:
                    menudia[g], menudia[h] = menudia[h], menudia[g]
        for l in range(k):
            if menudia[l].tipo == aux2:
                print(Comidas.to_string(menudia[l],tipos, clase))
                aux2 += 1
            else:
                print('No hay '+ tipos[l] + clase[x] + ' en el menu del día')
                print(Comidas.to_string(menudia[l],tipos, clase))
                aux2 += 2
            timer += menudia[l].tiempo
            cash += menudia[l].precio
        print('\nTIEMPO DE PREPARACIÓN: '+ str(timer) + ' min. ---- PRECIO TOTAL DEL MENU DEL DÍA: $ '+ str(cash))
    else:
        print('No hay menu del dia'+ clase[x])

def display(com, tip, cla):
    print(' ______________________________________________________________'
              '_______________________________________________________________'
              '___')
    for v in com:
        print('|______________________________________________________________'
              '_______________________________________________________________'
              '___|')
        print(Comidas.to_string(v,tip, cla))
    print('|______________________________________________________________'
              '_______________________________________________________________'
              '___|')
    return

def opcion1(com):
    n = len(com)
    for i in range(n-1):
        for j in range(i+1,n):
            if com[i].nombre > com[j].nombre:
                com[i], com[j] = com[j], com[i]
    print('--------------\|||CARTA DEL RESTAURANTE|||/--------------\n')
    display(com, tipos, clase)

def menu(a):
    n = len(a)
    op = 0
    while op != 7:
        print('\nQUE ACCIÓN DESEA REALIZAR?')
        print('\n1 - Mostrar Carta')
        print('2 - Precio Promedio')
        print('3 - Menor tiempo de Coccion')
        print('4 - Comidas por Tipo')
        print('5 - Buscar y Sugerir')
        print('6 - Menu del Día')
        print('7 - Salir')
        op = int(input())

        if op == 1:
            opcion1(a)
        elif op == 2:
            opcion2(a)
        elif op == 3:
            opcion3(a)
        elif op == 4:
            opcion4(a)
        elif op == 5:
            opcion5(a)
        elif op == 6:
            opcion6(a)
        elif op == 7:
            print('Programa Finalizado')
        elif op < 0 or op >7:
            print('entre 1 y 7')

def valtipo(tipo):
    while tipo < 0 or tipo > 2:
            print('0 = ENTRADA | 1 = PRINCIPAL | 2 = POSTRE')
            tipo = int(input('Tipo de Comida: '))
            if tipo < 0 or tipo > 2:
                print('mal')
    return tipo
def valclas(clasif):
    print(('0 = ESTANDAR | 1 = SIN TACC | 2 = VEGETARIANA | 3 = LIGHT'))
    while clasif < 0 or clasif > 3:
            clasif = int(input(" "))
            if clasif < 0 or clasif > 3:
                print("No es una clasificacion.")
    return clasif
def read(comida):
    n = len(comida)
    for i in range(n):
        nom = input('Ingrese nombre de comida: ')
        nom = nom.upper()
        print()
        tipo = 4
        tipo = valtipo(tipo)
        print()
        print("Tipo de clasificacion: ")
        clasif = 5
        clasif = valclas(clasif)
        print()
        print('Tiempo de Cocción(en minutos por favor )')
        time = validation(0)
        print()
        print('Precio del Plato')
        prec = validation2(0)

        comida[i] = Comidas.Comida(tipo, nom, clasif, time, prec)
        print()



# Validación de Carga
def validation(val):
    n = int(input('Valor mayor a ' + str(val) + ' porfavor:'))
    while n <= val:
        n = int(input('Se pidio valor mayor a ' + str(val) + ' porfavor:'))
    return n

def validation2(val):
    n = float(input('Valor mayor a ' + str(val) + ' porfavor:'))
    while n <= val:
        n = int(input('Se pidio valor mayor a ' + str(val) + ' porfavor:'))
    return n

# Carga Automática
def autoread(com):
    n = len(com)
    nom = ' '
    ant = 0
    ant2 = 0
    tipo = 0
    call = 0
    vce = 5 * [0]
    vcp = 5 * [0]
    vcpp = 5 * [0]
    for i in range(n):
        while ant == call:
            call = random.randint(0, 4)
        ant = call
        while ant2 == tipo:
            tipo = random.randint(0, 2)
        ant2 = tipo
        if tipo == 0:
            if vce[call] == 0:
                nom = entrada[call]
                vce[call] += 1
            else:
                nom = entrada[call] + str(vce[call])
                vce[call] += 1
        elif tipo == 1:
            if vcp[call] == 0:
                nom = princ[call]
                vcp[call] += 1
            else:
                nom = princ[call] + str(vcp[call])
                vcp[call] += 1
        elif tipo == 2:
            if vcpp[call] == 0:
                nom = postre[call]
                vcpp[call] += 1
            else:
                nom = postre[call] + str(vcpp[call])
                vcpp[call] += 1
        clasif = random.randint(0, 3)
        time = random.randint(0,40)
        prec = random.randint(0,130)
        com[i] = Comidas.Comida(tipo, nom, clasif, time, prec)

    print()

def auto():
    print('Ingrse la cantidad de comidas a registrar')
    n = validation(0)
    comida = n * [None]
    autoread(comida)
    return comida
def manual():
    print('Ingrse la cantidad de comidas a registrar')
    n = validation(0)
    comida = n * [None]
    print('Cargue los datos de las comidas')
    read(comida)
    print()
    return comida
# Inicio
def inicio():
    print('-------------------------------FOOD FAST CHARGER---------------------------------------------------\n')
    print('Bienvenido al asistente de carga de comidas del Restaurante. A continuación elija si desea realizar ')
    print('una carga manual o automática de las mismas y luego el menú principal lo guiará a través del sistema. ')
    print('Muchas gracias\n')
    op1 = 0
    while op1 != 1 and op1 != 2:
        print('Decea realizar la carga manual o automática de las comidas?')
        print('1 - Carga Automática')
        print('2 - Carga Manual')
        op1 = int(input())

    if op1 == 1:
        arr = auto()
    elif op1 == 2:
        arr = manual()
    menu(arr)


# Script Principal
if __name__ == '__main__':
    inicio()

import Series
from ArchivoSerie import *
import pickle
import os
gen = ['Infantil', 'Comedia', 'Romántico', 'Drama', 'Ciencia Ficción', 'Otros']
idioma = ['Español', 'Inglés', 'Francés', 'Portugués','Otros']
fd = 'series.dat'


def mostrar(v):
    for i in v:
        print(Series.to_string(i,gen[i.genero],idioma[i.idioma]))



def write():
    vseries = []
    n = len(vseries)
    m = open(fd , 'rb')
    t = os.path.getsize(fd)
    while m.tell()< t:
        serie = pickle.load(m)
        pos = n
        for i in range(n):
            if serie.titulo < vseries[i].titulo:
                pos = i
                break
        vseries[pos:pos] = [serie]
        n = len(vseries)
    m.close()
    mostrar(vseries)
    return vseries


def validar_genero(g):
    a = 0,1,2,3,4,5
    while not g in a :
        print('Ingrese un género entre 0 y 5 por favor')
        g = int(input())
    return g
def validar_idioma(g):
    a = 0,1,2,3,4
    while not g in a :
        print('Ingrese un idioma entre 0 y 4 por favor')
        g = int(input())
    return g
def calculo_tiempo(serie):
    dura = serie.minutos_x_capitulos * serie.capitulos_x_temporada * serie.cantidad_temporadas
    return dura

def horas(d):
    h = d // 60
    m = d % 60
    hms = [h ,m]
    return hms

def seriesxgenero(v):
    ctg = 0
    d = 0
    dura = 0
    print('¿Que género desea buscar?')
    print ("[0]Infantil, [1]Comedia, [2]Romántico, [3]Drama, [4]Ciencia Ficción, [5]Otros")
    g = int(input())
    g = validar_genero(g)
    print('¿Cuantas series de '+ gen[g] + ' desea mostrar?')
    n = int(input())

    x = len(v)
    for i in range(x):
        if v[i].genero == g:
            ctg += 1
            if ctg <= n:
                print(Series.to_string(v[i],gen[v[i].genero],idioma[v[i].idioma]))
                d += calculo_tiempo(v[i])
    dura = horas(d)
    if ctg < n :
        print('\nNO HAY UN TOTAL DE',n,'SERIES DE',gen[g])
        print('SE HAN MOSTRADO LAS', ctg ,'SERIES DE',gen[g],'EXISTENTES')

    print('\nDuración de la lista de', gen[g],':',dura[0],'hs.',dura[1],'min.\n')


def cant_idioma_genero(v):
    ct_idioma_gen= [[0] * 6 for f in range(5)]
    n = len(v)
    for i in range(n):
        idi = v[i].idioma
        gen = v[i].genero
        ct_idioma_gen[idi][gen] += 1
    display_mat(ct_idioma_gen)

def display_mat(ct):
     filas, columnas = len(ct), len(ct[0])
     print()
     print('Series por idioma y genero')
     print('SE ENCONTRARON:')
     for f in range(filas):
        for c in range(columnas):
            if ct[f][c] != 0:
                print(ct[f][c],'Series en ', idioma[f] , '\tde', gen[c])


def buscar_serie(v):
    print('Ingrese el nombre de la serie a buscar: ')
    x = input()
    n = len(v)
    exist = False
    for i in range(n):
        if x.upper() == v[i].titulo.upper():
            exist = True
            if v[i].ultima_temp_vista == 7 and v[i].ultimo_cap_visto == 25:
                print('YA HAS VISTO LA SERIE COMPLETA\n')
            else:
                print('AUN NO HAS VISTO LA SERIE COMPLETA\n')
            break
    if not exist:
        print('NO SE ENCUENTRA LA SERIE\n')


def series_unseen(v):
    print("\nSERIES QUE AUN NO HAS VISTO\n")
    n = len(v)
    d = 0
    nuevo_vec = []
    x = len(nuevo_vec)
    for i in range(n):
        if v[i].ultima_temp_vista == 0:
            pos = x
            for j in range(x):
                if v[i].titulo < nuevo_vec[j].titulo:
                    pos = i
                    break
            nuevo_vec[pos:pos] = [v[i]]
            x = len(nuevo_vec)
    mostrar(nuevo_vec)
    for k in nuevo_vec:
        d += calculo_tiempo(k)
    dura = horas(d)
    print('\nDuración de la lista de series sin ver:',dura[0],'hs.',dura[1],'min.\n')


def series_x_idioma(v):
    print('\nCrearás un archivo con series de un idioma en especifico\n')
    print ("[0]Español, [1]Inglés, [2]Francés, [3]Portugués, [4]Otros")
    x = int(input('¿Que idioma deseas utilizar?'))
    x = validar_idioma(x)
    n = len(v)
    fd2 = "SeriesIdioma"+idioma[x]+".dat"
    m = open(fd2 , 'wb')
    for i in range(n):
        if v[i].idioma == x:
            pickle.dump(v[i], m)
    m.close()
    m = open(fd2 , 'rb')
    t = os.path.getsize(fd2)
    while m.tell()< t:
        serie = pickle.load(m)
        g = serie.genero
        i = serie.idioma
        print(Series.to_string(serie,gen[g],idioma[i]))
    m.close()

def script():
    generar()
    op = -1
    v = []
    opciones = ["1","2","3","4","5","6","7"]
    print ("\t\t\tBienvenido al gestor de series")
    while op != "7":
        print ("*"*60)
        print("Menu de opciones!!")
        print("1.Mostrar lista de series.")
        print("2.Generar una cantidad de series de un determinado genero.")
        print("3.Determinar la cantidad de series por genero e idioma.")
        print("4.Buscar una serie por titulo.")
        print("5.Generar una lista de series que aun no ha empezado a ver.")
        print("6.Generar un archivo con series de un determinado idioma.")
        print("7.Salir.")
        op =(input("Seleccione la opcion que desee realizar: "))

        if op in opciones:
            if op == "1":
                v = write()
            if v != []:
                if op == "2":
                    seriesxgenero(v)
                elif op == "3":
                    cant_idioma_genero(v)
                elif op == "4":
                    buscar_serie(v)
                elif op == "5":
                    series_unseen(v)
                elif op == "6":
                    series_x_idioma(v)
            else:
                print('Aun no ha cargado el vector')
            if op == "7":
                print('Programa Finalizado')

        else:
            print ("\nError!!! elija una opcion [entre 1 al 7, no caracter]\n")
if __name__ == "__main__":
    script()
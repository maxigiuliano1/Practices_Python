__author__ = 'Lautaro Zurita'

class Comida:
    def __init__(self, tipe, nom, clas, time, prec):
        self.tipo = tipe
        self.nombre = nom
        self.clasificacion = clas
        self.tiempo = time
        self.precio = prec

def to_string(comida, tip, cla):
    r = ''
    r += '{:<35}'.format('|  Nombre: ' + comida.nombre)
    r += '{:<20}'.format('|  Tipo: ' + str(tip[comida.tipo]))
    r += '{:<35}'.format('|  Clasificación: ' + str(cla[comida.clasificacion]))
    r += '{:<20}'.format('|  Tiempo: ' + str(comida.tiempo) + ' min.')
    r += '{:<20}'.format('|  Precio: $ ' + str(comida.precio))
    return r

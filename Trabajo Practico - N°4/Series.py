__author__ = 'Zurita'
import random
import pickle

fd = 'series.dat'
nom = ['Taked', 'Walking 22XT', 'Viking', 'Games of Orus', 'Path of Ades']

class Serie:
    def __init__(self, tit, gen, idi, ctemp, captemp, dura, utv, ucv):
        self.titulo = tit
        self.genero = gen
        self.idioma = idi
        self.cantidad_temporadas = ctemp
        self.capitulos_x_temporada = captemp
        self.minutos_x_capitulos = dura
        self.ultima_temp_vista = utv
        self.ultimo_cap_visto = ucv

def to_string(serie,genero,idioma):
    r = ''
    r += '{:<25}'.format('Titulo: ' + serie.titulo)
    r += '{:<30}'.format('Genero: ' + genero)
    r += '{:<25}'.format('Idioma: ' + idioma)
    r += '{:<30}'.format('Cantidad de Temporadas: ' + str(serie.cantidad_temporadas))
    r += '{:<30}'.format('Capítulos por Temporada: ' + str(serie.capitulos_x_temporada))
    r += '{:<35}'.format('Duración de cada capítulo: ' + str(serie.minutos_x_capitulos))
    r += '{:<35}'.format('Última temporada vista: ' + str(serie.ultima_temp_vista))
    r += '{:<30}'.format('Último capítulo visto: ' + str(serie.ultimo_cap_visto))
    return r



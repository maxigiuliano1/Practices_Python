from Series import *
import random
import pickle

fd = 'series.dat'
nom = ['Taked', 'Walking 22XT', 'Viking', 'Games of Orus', 'Path of Ades']

def generar():
    m = open(fd, 'w+b')
    n = 50
    ant = 0
    gen = 0
    idi = 0
    ant2 = 0
    ctn = [0] * 5
    for i in range(n) :
        a = random.randint(0,4)
        tit = nom[a]
        if ctn[a] != 0:
            if ctn[a] <= 9:
                tit = tit + ' 0' +str(ctn[a])
            else:
                tit = tit + ' ' +str(ctn[a])
        ctn[a] +=1
        while ant == gen:
            gen = random.randint(0,5)
        ant = gen
        while ant2 == idi:
            idi = random.randint(0,4)
        ant2 = gen
        ctemp = random.randint(1,7)
        cxtmp = random.randint(10,25)
        dura = random.randint(21,25)
        utv = random.randint(0, ctemp)
        if utv == 0:
            ucv = 0
        else:
            ucv = random.randint(0 ,cxtmp)

        s = Serie(tit, gen, idi, ctemp, cxtmp, dura, utv, ucv)

        pickle.dump(s , m)
    m.close()


#Test case for manually computing gaussian line parameters. 

import numpy
import math

def redshifted(wavelength, z):
    return z * wavelength

w = open("jph_mod_test.bands",'r')
f = open("0093.txt",'r')
r = open("0093.bands",'w')

for line in f:
    list = line.split()
    if list[0] == 'VELOCITY=':
        z = float(list[1]) / (3 * 10**5) + 1
        break

f.close()    
print z

w.readline()

for line in w:
    list = line.split()
    l = len(list)
#    print list
    lbc = float(list[1]) * z
    ubc = float(list[2]) * z
    ll = float(list[3]) * z
    ul = float(list[4]) * z
    lrc = float(list[5]) * z
    urc = float(list[6]) * z
    r.write("%s %f %f %f %f %f %f\n" % (list[0], lbc, ubc, ll, ul, lrc, urc))
    
w.close()
r.close()

f = open("0093.txt",'r')
g = open("0093.lines",'w') 
#print f.readline()   

r = open("0093.bands", 'r')

for line in r:
    band = line.split()
#    print band
    bc = 0
    rc = 0
    l = 0
    f.seek(0)
    i = 0
    bcn = 0
    ln = 0
    rcn = 0
    while i<=141:
        f.readline()
        i += 1
    for row in f:
        col = row.split()
        if float(band[1]) <= float(col[0]) <= float(band[2]):
            bc = bc + float(col[1])       
            bcn += 1
            print col[0], col[1]
        elif float(band[3]) <= float(col[0]) <= float(band[4]):
            l = l + float(col[1])
            ln += 1
            print col[0], col[1]
        elif float(band[5]) <= float(col[0]) <= float(band[6]):
            rc = rc + float(col[1])
            rcn += 1
            print col[0], col[1]
        elif float(col[0]) > float(band[6]):
            print col[0]
            break
    width = (float(band[4]) - float(band[3])) * (1 - (l / ln) * 2/(rc/rcn + bc/bcn))
    g.write("%f %f %f %f %f %f %f %f\n" % (bc, bcn, l, ln, rc, rcn, width, math.sqrt(ln/l + rcn/rc + bcn/bc)))
     
 
f.close()
r.close()    
     

import math
import numpy
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplot, savefig

fig = subplot(111)
fig.set_title("SDSS-AGN")
fig.set_xlabel(r'log(NII/H$\alpha$)')
fig.set_ylabel(r'log(OIII/H$\beta)$')
#fig.set_yscale('log')
#fig.set_xscale('log')
data = open("SDSS_ratios.txt", 'r')
data.seek(0)
AGN = 0
non = 0
kewley = 0
kauffmann = 0

for line in data:
    line = line.rstrip()
    columns = line.split(' ')
    yc = float(columns[1])
    xc = float(columns[2])
    id1 = columns[5]
    id2 = columns[6]
    if xc >=1. or xc <= -2.0:
#        print columns[0], xc, yc
         continue
    if yc >= 1.5 or yc <=-1.5:
#        print columns[0], xc, yc
         continue
    if id1 == 'AGN' and id2 == 'AGN':
        fig.plot(xc, yc, marker = "o", ms = 3, mfc = 'red')
        AGN += 1
    elif id1 == 'not' and id2 == 'not':
        fig.plot(xc, yc, marker = "s", ms = 3, mfc = 'black')
        non += 1
    elif id1 == 'AGN' and id2 == 'not':
        fig.plot(xc, yc, marker = "^", ms = 3, mfc = 'magenta')
        kewley += 1
    elif id1 == "not" and id2 == 'AGN':
        fig.plot(xc, yc, marker = "^", ms = 3, mfc = 'green')
        kauffmann += 1


x_kew = numpy.linspace(-1.5, -0.16, 100)
y_kew = (0.61 / (x_kew - 0.05)) + 1.30

x_kauf = numpy.linspace(-1.5, 0.24, 100)
y_kauf = (0.61 / (x_kauf - 0.47)) + 1.19

fig.plot(x_kew, y_kew, 'g-', linestyle = "--")
fig.plot(x_kauf, y_kauf, 'b-', linestyle = "-")


print AGN, non, kewley, kauffmann
savefig('SDSS-agn.png')
    
import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig

#I am going to run this program for FAST and SDSS data
#for FAST, the file names will be 
#f = open("FAST.5.out",'r')
#g = open("Fast_ratios.txt",'w')
#for SDSS, 
#f = open("sdss.em.5.out",'r')
#g = open("SDSS_ratios.txt",'w')

# the ratios are between
#   1            HbB       none  4821.3300 -  5000.0000\n
#   7     [OIII]5007       none  4996.8400 -  5016.8400\n
#   11           HaE       none  6552.8200 -  6572.8200\n
#   18     [NII]6584       none  6573.5700 -  6593.5700\n

def sig3(a,a_err):
    if math.fabs(a) >= 2 * math.fabs(a_err) and a < 0:
        return 1
    else:
        return 0
        
f = open("FAST.5.out",'r')

f.seek(0)

maximum = 0.0
minimum = 1.0
counts_list = []


for line in f:
    list = line.split('\t')
    Hbeta = float(list[1])
    counts_list.append(Hbeta)
#    Hbeta = 0.9613*Hbeta_uncorr - 2.435
    if Hbeta >= maximum:
        maximum = Hbeta
    if Hbeta <= minimum:
        minimim = Hbeta
    
print maximum, minimum



m = max(counts_list)
n = min(counts_list)

counts_list.sort()

length = len(counts_list)

bin1 = counts_list[0:2000:1]
p1 = counts_list[1999]
bin2 = counts_list[2000:4000]
p2 = counts_list[3999]
bin3 = counts_list[4000:6000]
p3 = counts_list[5999]
bin4 = counts_list[6000:8000]
p4 = counts_list[7999]
bin5 = counts_list[8000:10000]
p5 = counts_list[9999]
bin6 = counts_list[10000:]
p6 = m

plt.hist(counts_list, bins = 25, log = True, range = (-20, 20),normed = False, cumulative = False, color = None)

print m, n

f.close()

savefig("hist.pdf")


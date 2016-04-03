import math

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
    if math.fabs(a) >= 3 * math.fabs(a_err) and a < 0:
        return 1
    else:
        return 0
        
f = open("sdss.em.5.out",'r')
g = open("SDSS_ratios.txt",'w')
t = open("test-sdss", "w")

f.seek(0)
i = 0
d = 0
hb = 0
o3 = 0
n2 = 0
ha = 0
o3hb = 0
n2ha = 0
o3ha = 0
n2hb = 0
hbha = 0
o3n2 = 0
o3hbn2 = 0
o3han2 = 0
hbn2ha = 0
o3hahb = 0
o3hbn2ha = 0
all = 0
truth = [0,0,0,0]
j = 0
for line in f:
    list = line.split('\t')
#    Hbeta = float(list[1])
    Hbeta_uncorr = float(list[1])
    Hbeta = 0.9613 * Hbeta_uncorr - 2.435
    Hbeta_err = float(list[2])
    OIII = float(list[7])
    OIII_err = float(list[8])
    Halpha = float(list[11])
    Halpha_err = float(list[12])
    NII = float(list[17])
    NII_err = float(list[18])
    numerr = 0
    denerr = 0
    OIII_Hbeta = "False"
    NII_Halpha = "False"
    truth[0] = sig3(Hbeta, Hbeta_err)
    truth[1] = sig3(OIII, OIII_err)
    truth[2] = sig3(NII, NII_err)
    truth[3] = sig3(Halpha, Halpha_err)
    t.write("%d %d %d %d %d\n" % (i, truth[0], truth[1], truth[2], truth[3]))
    i += 1
    if truth == [0,1,1,1]: 
        hb += 1                  #2323 to 408    1915     7 these refer to fast data
    elif truth == [1,0,1,1]:     #0,0,1,1
        o3 += 1                  #200 to 1490    -1290    4
    elif truth == [1,1,0,1]:     #0,1,0,1
        n2 += 1                  #9 to 98        -89    1
    elif truth == [1,1,1,0]:     #0,1,1,0
        ha += 1                  #50 to 1021     -971   2
    elif truth == [0,0,1,1]:     
        o3hb += 1                #1758 to 468    1290    4
    elif truth == [0,1,0,1]:     
        n2hb += 1                #116 to 27      89     1
    elif truth == [1,0,0,1]:     #0,0,0,1
        o3n2 += 1                #12 to 168      -156    8
    elif truth == [1,0,1,0]:     #0,0,1,0
        o3ha += 1                #85 to 1962     -1877   3
    elif truth == [1,1,0,0]:     #0,1,0,0
        n2ha += 1                #70 to 546      -476    5
    elif truth == [0,1,1,0]:     
        hbha += 1                #1344 to 373    971     2
    elif truth == [0,0,0,1]: 
        o3hbn2 += 1              #211 to 55      156     8
    elif truth == [1,0,0,0]:     #0,0,0,0
        o3han2 += 1              #64 to 1500      -1436  6
    elif truth == [0,1,0,0]: 
        hbn2ha += 1              #709 to 233     476     5
    elif truth == [0,0,1,0]: 
        o3hahb += 1              #2647 to 770    1877     3
    elif truth == [0,0,0,0]:
        o3hbn2ha += 1            #2101 to 665    -1436    6
    elif truth == [1,1,1,1]:     #0,1,1,1
        all += 1                 #836 to 2751    -1915     7
    if sig3(Hbeta, Hbeta_err) == 1 and sig3(OIII, OIII_err) == 1:
        ratio = OIII / Hbeta
        if ratio > 0:
              OIII_Hbeta = math.log10(ratio)
              if OIII_Hbeta >= 0:
                  print i, OIII_Hbeta
        else:
              OIII_Hbeta = "False"
    else:
        OIII_Hbeta = "False"
    if sig3(Halpha, Halpha_err) == 1 and sig3(NII, NII_err) == 1:
        ratio = NII / Halpha
        if ratio > 0:
              NII_Halpha = math.log10(ratio)
        else:
              NII_Halpha = "False"
    else:
        NII_Halpha = "False"

    if NII_Halpha == "False" or OIII_Hbeta == "False":
        j += 1 
    else:
        if  OIII_Hbeta >1.0 or NII_Halpha > 0.2:
            kewley = 'AGN'
        elif OIII_Hbeta > (0.61/(NII_Halpha - 0.47)) + 1.19:
            kewley = 'AGN'
        else: 
            kewley = 'not'
        if OIII_Hbeta >1.0 or NII_Halpha >-0.2:
            kauffmann = 'AGN'    
        elif OIII_Hbeta > (0.61/(NII_Halpha - 0.05)) +1.30:
            kauffmann = 'AGN'
        else:
            kauffmann = 'not'
        g.write("%d %f %f %f %f %s %s \n" % (i, OIII_Hbeta, NII_Halpha,  numerr, denerr, kewley, kauffmann))
    if NII_Halpha == "False":
        if OIII_Hbeta != "False" and OIII_Hbeta > 0:
            print i, OIII_Hbeta
            d += 1

print "o3", o3
print "n2", n2
print "hb", hb
print "ha", ha
print "o3hb", o3hb
print "o3ha", o3ha
print "n2hb", n2hb
print "n2ha", n2ha
print "hbha", hbha
print "o3n2", o3n2
print "o3hbn2", o3hbn2
print "o3han2", o3han2
print "hbn2ha", hbn2ha
print "o3hahb", o3hahb
print "o3hbn2ha", o3hbn2ha
print "all", all
print "j", j
print "d", d
f.close()
g.close()   
t.close()
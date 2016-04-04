#Compares two test cases, one where the header was fixed, one where it wasn't.  We were trying to quantify the possible discrepancy introduced by manually entering header information



f = open("test", 'r')
g = open("test-uncorr", 'r')

t = open("change", 'w')

f.seek(0)
g.seek(0)

for i in range(0,12535):
    line1 = f.readline()
    line2 = gq.readline()
    truth1 = line1.split()
    truth2 = line2.split()
    a = int(truth1[1]) - int(truth2[1])
    b = int(truth1[2]) - int(truth2[2])
    c = int(truth1[3]) - int(truth2[3])
    d = int(truth1[4]) - int(truth2[4])
    t.write("%d %d %d %d %d\n" % (i, a, b, c, d))

f.close()
g.close()
t.close()
